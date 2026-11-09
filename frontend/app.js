"use strict";
// All student text is rendered with textContent (NFR-12). Calls relative /api URLs (see dev_server.py).
const $ = (s, r = document) => r.querySelector(s);
const state = { courses: [], assignments: [], dashboard: null, view: "dashboard" };

function el(tag, props = {}, ...kids) {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(props)) {
    if (k === "class") n.className = v; else if (k === "text") n.textContent = v;
    else if (k.startsWith("on")) n.addEventListener(k.slice(2), v); else n.setAttribute(k, v);
  }
  n.append(...kids);
  return n;
}

async function api(method, path, body) {
  try {
    const res = await fetch("/api" + path, {
      method, headers: body ? { "Content-Type": "application/json" } : {}, body: body ? JSON.stringify(body) : undefined,
    });
    if (res.status === 204) return { ok: true };
    const json = await res.json();
    return res.ok ? { ok: true, data: json.data } : { ok: false, status: res.status, error: json.error };
  } catch (e) {
    return { ok: false, status: 0, error: { message: "Cannot reach the server. Your data is safe; try again.", fields: {} } };
  }
}

function banner(msg) { const b = $("#banner"); b.textContent = msg || ""; b.hidden = !msg; }
function showErrors(form, error) {
  form.querySelectorAll(".err").forEach(p => (p.textContent = ""));
  const fields = (error && error.fields) || {};
  let general = error ? error.message : "";
  for (const [f, m] of Object.entries(fields)) {
    const p = form.querySelector(`[data-err="${f}"]`);
    if (p) { p.textContent = m; general = ""; }
  }
  const g = form.querySelector('[data-err="_"]'); if (g) g.textContent = general || "";
}

// ---------- loading ----------
async function refresh() {
  const course = $("#f-course").value, status = $("#f-status").value;
  const q = new URLSearchParams(); if (course) q.set("course_id", course); if (status) q.set("status", status);
  const [c, a, d] = await Promise.all([api("GET", "/courses"), api("GET", "/assignments" + (q.size ? "?" + q : "")), api("GET", "/dashboard")]);
  if (a.status === 404 && course) { $("#f-course").value = ""; return refresh(); } // stale course filter
  const failed = [c, a, d].find(r => !r.ok);
  if (failed) { banner((failed.error && failed.error.message) || "Could not refresh."); return; } // keep old data on screen
  banner("");
  state.courses = c.data; state.assignments = a.data; state.dashboard = d.data;
  render();
}

// ---------- rendering ----------
function render() {
  renderCourseFilter(); renderDashboard(); renderAssignments(); renderCourses();
}
function renderCourseFilter() {
  const sel = $("#f-course"), cur = sel.value;
  sel.replaceChildren(el("option", { value: "", text: "All courses" }), ...state.courses.map(c => el("option", { value: c.id, text: courseLabel(c) })));
  sel.value = state.courses.some(c => String(c.id) === cur) ? cur : "";
}
const courseLabel = c => (c.code ? c.code + " – " : "") + c.name;
const fmtDue = a => a.due_date + (a.due_time ? " " + a.due_time : "");

function renderDashboard() {
  const d = state.dashboard;
  const box = (label, n, cls, status) => el("button", { class: cls, onclick: () => { $("#f-status").value = status; $("#f-course").value = ""; show("assignments"); refresh(); } },
    el("b", { text: String(n) }), label);
  $("#counts").replaceChildren(box("Pending", d.pending, "pending", "Pending"), box("Completed", d.completed, "completed", "Completed"), box("Overdue", d.overdue, "overdue", "Overdue"));
  const ul = $("#next-due");
  ul.replaceChildren(...(d.next_due.length ? d.next_due.map(a => item(a, false)) : [el("li", { class: "empty", text: "Nothing pending. Add an assignment to get started." })]));
}
function renderAssignments() {
  const ul = $("#assignment-list");
  ul.replaceChildren(...(state.assignments.length ? state.assignments.map(a => item(a, true)) : [el("li", { class: "empty", text: "No assignments match. Change the filters or add one." })]));
}
function item(a, actions) {
  const done = a.status === "Completed";
  const li = el("li", { class: "item" + (a.overdue ? " overdue" : "") + (done ? " done" : "") });
  const info = el("div", {}, el("div", { class: "t", text: a.title }),
    el("div", { class: "m", text: `${courseLabel({ code: a.course_code, name: a.course_name })} · ${a.task_type} · due ${fmtDue(a)}` }));
  const tags = el("span", { class: "tag" + (a.overdue ? " bad" : ""), text: a.overdue ? "Overdue" : a.status });
  li.append(info, tags);
  if (actions) {
    li.append(el("div", { class: "row" },
      el("button", { text: done ? "Reopen" : "Mark complete", onclick: () => setStatus(a, done ? "Pending" : "Completed") }),
      el("button", { text: "Edit", onclick: () => openAssignment(a) }),
      el("button", { text: "Delete", onclick: () => confirmDelete(`Delete "${a.title}"? This cannot be undone.`, () => remove(`/assignments/${a.id}`)) })));
  }
  return li;
}
function renderCourses() {
  $("#course-list").replaceChildren(...(state.courses.length ? state.courses.map(c => el("li", { class: "item" },
    el("div", { class: "t", text: courseLabel(c) }),
    el("div", { class: "row" },
      el("button", { text: "Edit", onclick: () => editCourse(c) }),
      el("button", { text: "Delete", onclick: () => confirmDelete(`Delete course "${c.name}"?`, () => remove(`/courses/${c.id}`)) })))) : [el("li", { class: "empty", text: "No courses yet. Add one above." })]));
}

// ---------- actions ----------
async function setStatus(a, status) {
  const r = await api("PATCH", `/assignments/${a.id}/status`, { status });
  if (!r.ok) banner(r.error.message); await refresh();
}
function confirmDelete(text, onYes) {
  const d = $("#confirm-dialog"); $("#confirm-text").textContent = text;
  d.onclose = () => { if (d.returnValue === "ok") onYes(); };
  d.returnValue = ""; d.showModal();
}
async function remove(path) {
  const r = await api("DELETE", path + "?confirmed=true");
  banner(r.ok ? "" : r.status === 409 ? "This course still has assignments. Move or delete them first." : r.error.message);
  await refresh();
}

function openAssignment(a) {
  const f = $("#assignment-form"); f.reset(); showErrors(f, null);
  f.course_id.replaceChildren(...state.courses.map(c => el("option", { value: c.id, text: courseLabel(c) })));
  $("#assignment-title-h").textContent = a ? "Edit assignment" : "Add assignment";
  f.id.value = a ? a.id : "";
  if (a) { f.title.value = a.title; f.course_id.value = a.course_id; f.due_date.value = a.due_date; f.due_time.value = a.due_time || ""; f.task_type.value = a.task_type; f.description.value = a.description; }
  if (!state.courses.length) showErrors(f, { message: "Add a course first (Courses tab).", fields: {} });
  $("#assignment-dialog").showModal();
}
$("#assignment-form").addEventListener("submit", async e => {
  e.preventDefault();
  const f = e.target, btn = f.querySelector(".primary"); btn.disabled = true;
  const body = { title: f.title.value, course_id: Number(f.course_id.value) || 0, due_date: f.due_date.value,
    due_time: f.due_time.value || null, task_type: f.task_type.value, description: f.description.value };
  const r = f.id.value ? await api("PUT", "/assignments/" + f.id.value, body) : await api("POST", "/assignments", body);
  btn.disabled = false;
  if (!r.ok) return showErrors(f, r.error); // keep the form content
  $("#assignment-dialog").close(); await refresh();
});
$("#assignment-cancel").onclick = () => $("#assignment-dialog").close();
$("#add-assignment").onclick = () => openAssignment(null);

function editCourse(c) {
  const f = $("#course-form"); f.id.value = c.id; f.name.value = c.name; f.code.value = c.code; $("#course-cancel").hidden = false; f.name.focus();
}
function resetCourseForm() { const f = $("#course-form"); f.reset(); f.id.value = ""; $("#course-cancel").hidden = true; showErrors(f, null); }
$("#course-cancel").onclick = resetCourseForm;
$("#course-form").addEventListener("submit", async e => {
  e.preventDefault();
  const f = e.target, btn = f.querySelector(".primary"); btn.disabled = true;
  const body = { name: f.name.value, code: f.code.value };
  const r = f.id.value ? await api("PUT", "/courses/" + f.id.value, body) : await api("POST", "/courses", body);
  btn.disabled = false;
  if (!r.ok) return showErrors(f, r.error);
  resetCourseForm(); await refresh();
});

// ---------- navigation and refresh ----------
function show(view) {
  state.view = view;
  for (const v of ["dashboard", "assignments", "courses"]) $("#view-" + v).hidden = v !== view;
  document.querySelectorAll("nav button").forEach(b => b.dataset.view === view ? b.setAttribute("aria-current", "page") : b.removeAttribute("aria-current"));
}
document.querySelectorAll("nav button").forEach(b => b.onclick = () => show(b.dataset.view));
$("#f-course").onchange = $("#f-status").onchange = refresh;
window.addEventListener("focus", refresh);
setInterval(refresh, 60000);
refresh();
