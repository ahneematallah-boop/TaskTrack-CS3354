# Contributing to TaskTrack

All changes reach `main` through a pull request. Direct pushes to `main` are blocked. This satisfies NFR-14 (version control and review before merging).

## Workflow

1. Create a branch from `main`: `git checkout -b <your-name>/<short-topic>`.
2. Commit your changes and push the branch.
3. Open a pull request into `main` and complete the checklist in the template.
4. The **Docs Review** workflow runs three checks:
   - **Markdown lint**: heading structure, list formatting, and table syntax.
   - **Relative link check**: every link between repository files resolves.
   - **Requirements traceability**: every FR / NFR ID cited in `docs/` is defined in `docs/Requirements.md`.
5. The final reviewer approves the pull request. Merge after all checks pass and one approval is recorded.

## Running the checks locally

```sh
npx markdownlint-cli2 "**/*.md"
python3 scripts/check_traceability.py
```

## Roles

| Member | Responsibility |
|---|---|
| Ahmed | Problem, stakeholders, feasibility, and scope |
| Taha | Functional and nonfunctional requirements |
| Matthew | Use cases and traceability |
| Jackie | Team plan, milestones, and risks |
| Karim | Repository organization and final review (required approver) |
