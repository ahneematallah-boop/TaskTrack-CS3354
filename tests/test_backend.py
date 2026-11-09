"""API integration tests use real SQLite files and a fixed deadline clock."""
import sqlite3
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from backend.app import create_app


class BackendTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.config = {"TESTING": True, "DATABASE": str(Path(self.directory.name) / "tasks.sqlite3"),
                       "TIMEZONE": "America/Chicago",
                       "NOW": lambda: datetime(2026, 11, 8, 18, tzinfo=timezone.utc)}
        self.app = create_app(self.config)
        self.client = self.app.test_client()
        self.course = self.client.post('/api/courses', json={"name": "Software Engineering", "code": "CS3354"}).json['data']

    def create(self, **changes):
        body = {"title": "Worksheet", "course_id": self.course['id'], "due_date": "2026-11-09"}
        body.update(changes)
        response = self.client.post('/api/assignments', json=body)
        self.assertEqual(response.status_code, 201, response.json)
        return response.json['data']

    def test_persistence_across_app_restart(self):
        task = self.create()
        self.client.patch(f"/api/assignments/{task['id']}/status", json={"status": "Completed"})
        restarted = create_app(self.config).test_client()
        saved = restarted.get(f"/api/assignments/{task['id']}").json['data']
        self.assertEqual(saved['status'], 'Completed')
        self.assertEqual(saved['course_name'], 'Software Engineering')
        self.assertEqual(saved['due_at'], '2026-11-10T05:59:00Z')

    def test_validation_does_not_create_partial_records(self):
        for change in ({"title": "  "}, {"course_id": 999}, {"course_id": True},
                       {"due_date": "2026-02-30"}, {"due_date": "20261108"},
                       {"due_time": "25:00"}, {"description": []}, {"status": "Completed"},
                       {"due_date": "2026-03-08", "due_time": "02:30"}):
            body = {"title": "Task", "course_id": self.course['id'], "due_date": "2026-11-08", **change}
            response = self.client.post('/api/assignments', json=body)
            self.assertEqual(response.status_code, 400, response.json)
            self.assertTrue(response.json['error']['fields'])
        self.assertEqual(self.client.get('/api/assignments').json['data'], [])

    def test_invalid_edit_keeps_original_and_valid_edit_retains_status(self):
        task = self.create()
        path = f"/api/assignments/{task['id']}"
        self.client.patch(path + '/status', json={"status": "Completed"})
        response = self.client.put(path, json={"title": ""})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.client.get(path).json['data']['title'], 'Worksheet')
        response = self.client.put(path, json={"title": "Changed", "course_id": self.course['id'], "due_date": "2026-11-10"})
        self.assertEqual(response.json['data']['id'], task['id'])
        self.assertEqual(response.json['data']['status'], 'Completed')
        self.assertEqual(len(self.client.get('/api/assignments').json['data']), 1)

    def test_course_rename_and_restrict_delete(self):
        task = self.create()
        path = f"/api/courses/{self.course['id']}"
        renamed = self.client.put(path, json={"name": "SE"})
        self.assertEqual(renamed.status_code, 200)
        self.assertEqual(self.client.get(f"/api/assignments/{task['id']}").json['data']['course_name'], 'SE')
        self.assertEqual(self.client.delete(path + '?confirmed=true').status_code, 409)
        self.assertEqual(len(self.client.get('/api/assignments').json['data']), 1)
        self.client.delete(f"/api/assignments/{task['id']}?confirmed=true")
        self.assertEqual(self.client.delete(path + '?confirmed=true').status_code, 204)

    def test_delete_confirmation_and_missing_record(self):
        task = self.create()
        path = f"/api/assignments/{task['id']}"
        self.assertEqual(self.client.delete(path).status_code, 400)
        self.assertEqual(self.client.get(path).status_code, 200)
        self.assertEqual(self.client.delete(path + '?confirmed=true').status_code, 204)
        self.assertEqual(self.client.get(path).status_code, 404)

    def test_counts_reopen_and_filters(self):
        old = self.create(due_date='2026-11-01')
        future = self.create(due_date='2026-11-10')
        dashboard = self.client.get('/api/dashboard').json['data']
        self.assertEqual((dashboard['pending'], dashboard['completed'], dashboard['overdue']), (2, 0, 1))
        path = f"/api/assignments/{old['id']}/status"
        for _ in range(2):
            self.assertEqual(self.client.patch(path, json={"status": "Completed"}).status_code, 200)
        dashboard = self.client.get('/api/dashboard').json['data']
        self.assertEqual((dashboard['pending'], dashboard['completed'], dashboard['overdue']), (1, 1, 0))
        self.client.patch(path, json={"status": "Pending"})
        overdue = self.client.get('/api/assignments?status=Overdue').json['data']
        self.assertEqual([row['id'] for row in overdue], [old['id']])
        self.assertEqual(self.client.patch(path, json={"status": "Overdue"}).status_code, 400)
        other = self.client.post('/api/courses', json={"name": "Physics"}).json['data']
        self.assertEqual(self.client.get(f"/api/assignments?course_id={other['id']}").json['data'], [])
        self.assertEqual(self.client.get('/api/assignments?course_id=999').status_code, 404)
        self.assertEqual(self.client.get('/api/assignments?status=bogus').status_code, 400)
        self.assertEqual(self.client.get('/api/assignments?sort=bogus').status_code, 400)
        self.assertEqual(self.client.get('/api/assignments?course_id=bad').status_code, 400)
        self.assertNotEqual(old['id'], future['id'])

    def test_deadline_boundary_dst_and_title_tie_break(self):
        # 12:00 Chicago = 18:00 UTC after DST ends. Equal is not overdue.
        self.create(title='Zulu', due_date='2026-11-08', due_time='12:00')
        self.create(title='Alpha', due_date='2026-11-08', due_time='12:00')
        rows = self.client.get('/api/assignments').json['data']
        self.assertEqual([row['title'] for row in rows], ['Alpha', 'Zulu'])
        self.assertFalse(any(row['overdue'] for row in rows))
        self.app.config['NOW'] = lambda: datetime(2026, 11, 8, 18, 0, 0, 1, tzinfo=timezone.utc)
        self.assertTrue(all(row['overdue'] for row in self.client.get('/api/assignments').json['data']))
        summer = self.create(due_date='2026-07-01', due_time='12:00')
        self.assertEqual(summer['due_at'], '2026-07-01T17:00:00Z')
        ambiguous = self.create(due_date='2026-11-01', due_time='01:30')
        self.assertEqual(ambiguous['due_at'], '2026-11-01T06:30:00Z')

    def test_storage_failure_returns_error_and_rolls_back(self):
        task = self.create()
        with sqlite3.connect(self.config['DATABASE']) as db:
            db.execute("CREATE TRIGGER fail_update BEFORE UPDATE ON assignments BEGIN SELECT RAISE(ABORT, 'test failure'); END")
        # Simulate a write failure after reaching a real transaction.
        response = self.client.patch(f"/api/assignments/{task['id']}/status", json={"status": "Completed"})
        self.assertEqual(response.status_code, 503)
        self.assertEqual(self.client.get(f"/api/assignments/{task['id']}").json['data']['status'], 'Pending')
        with patch('backend.service.database', side_effect=sqlite3.OperationalError('disk unavailable')):
            response = self.client.get('/api/dashboard')
        self.assertEqual(response.status_code, 503)
        self.assertNotIn('data', response.json)

    def test_json_security_and_error_envelopes(self):
        for value in ([], None, "bad"):
            response = self.client.post('/api/courses', data=__import__('json').dumps(value), content_type='application/json')
            self.assertEqual(response.status_code, 400)
        self.assertEqual(self.client.post('/api/courses', data='{', content_type='application/json').status_code, 400)
        self.assertEqual(self.client.post('/api/courses', data='name=x').status_code, 415)
        self.assertEqual(self.client.get('/api/health', headers={"Host": "attacker.example"}).status_code, 403)
        self.assertEqual(self.client.post('/api/courses', json={"name": "x"}, headers={"Origin": "https://attacker.example"}).status_code, 403)
        name = "Robert'); DROP TABLE courses;--"
        self.assertEqual(self.client.post('/api/courses', json={"name": name}).status_code, 201)
        self.assertEqual(len(self.client.get('/api/courses').json['data']), 2)
        self.assertEqual(self.client.get('/api/missing').status_code, 404)
        self.assertEqual(self.client.post('/api/courses', data='x' * 70000, content_type='application/json').status_code, 413)
        self.assertEqual(self.client.get('/api/health').headers['Cache-Control'], 'no-store')

    def test_empty_dashboard(self):
        data = self.client.get('/api/dashboard').json['data']
        self.assertEqual((data['pending'], data['completed'], data['overdue'], data['next_due']), (0, 0, 0, []))


if __name__ == '__main__':
    unittest.main()
