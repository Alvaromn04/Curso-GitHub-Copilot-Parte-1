# OctoAcme Project Management Handbook

This handbook is the entry point to OctoAcme's delivery methodology. OctoAcme uses a five-phase lifecycle—**Initiation, Planning, Execution, Release, and Close & Retrospective**—to move work from idea to measurable outcome. Each phase has clear goals, standard artifacts, and explicit exit criteria so teams can deliver consistently while adapting to change.

Delivery ownership is intentionally shared across well-defined roles. **Project Managers (PMs)** manage timelines, dependencies, risks, and communication flow; **Product Managers (PdMs)** own product outcomes, prioritize value, and define acceptance outcomes; **Developers** design, build, and maintain implementation quality; and **QA/Testing** validates quality gates before release. This separation of responsibilities reduces ambiguity and improves accountability across handoffs.

Communication follows a predictable cadence to keep execution transparent: daily standups for immediate coordination, weekly delivery syncs for plan health, and weekly stakeholder updates for business visibility. Risks and blockers follow a three-level escalation path (**Team → PM/Product Lead → Sponsor**) and are tracked in a **Risk Register** reviewed weekly, ensuring issues are surfaced early and resolved quickly.

Quality is built into the workflow rather than deferred to the end. OctoAcme uses layered validation (unit, integration, and end-to-end smoke testing), explicit acceptance criteria on backlog items, and pull request controls (small PRs, CI checks, and required review approval). Combined with a shared Definition of Done, these practices ensure releases are reliable, auditable, and aligned with customer value.

## Lifecycle Phases

| Phase | Purpose | Detailed Process |
| --- | --- | --- |
| Initiation | Confirm problem, goals, stakeholders, and business alignment before committing implementation effort. | [Initiation process](./process/initiation.md) |
| Planning | Convert approved scope into prioritized, estimated, testable delivery plans and release targets. | [Planning process](./process/planning.md) |
| Execution | Deliver iteratively through active development, reviews, QA validation, and blocker management. | [Execution process](./process/execution.md) |
| Release | Validate readiness, deploy safely, and monitor outcomes with rollback preparedness. | [Release process](./process/release.md) |
| Close & Retrospective | Capture outcomes, lessons learned, and process improvements for the next cycle. | [Close & Retrospective process](./process/close-and-retrospective.md) |

## Key Roles and Responsibilities

- **Project Manager (PM)**
  - Owns project plan integrity, milestones, cross-team dependencies, and risk management.
  - Maintains delivery cadence and stakeholder communication schedule.
  - Facilitates escalations and drives mitigation follow-through.
- **Product Manager (PdM)**
  - Defines success metrics and outcome targets.
  - Prioritizes backlog according to customer and business value.
  - Approves scope trade-offs and validates acceptance readiness.
- **Developers**
  - Implement prioritized backlog items with maintainable, reviewed code.
  - Collaborate on solution design, estimation, and technical risk reduction.
  - Ensure automated test coverage and production readiness.
- **QA/Testing**
  - Validates features against acceptance criteria and regression expectations.
  - Coordinates integration and end-to-end test validation.
  - Confirms release gate quality signals and defect closure status.

## Communication Structure and Escalation

### Operating cadence

- **Daily standup (15 minutes):** progress, next steps, blockers.
- **Weekly delivery sync:** sprint/iteration health, timeline drift, dependency updates.
- **Weekly stakeholder update:** status, milestones, risks, decisions, and support needed.
- **Ad-hoc incident/risk syncs:** triggered by critical blockers or release-impacting issues.

### Escalation path

1. **Team level:** resolve directly within delivery squad when possible.
2. **PM/Product Lead level:** escalate unresolved blockers, dependency conflicts, or scope risk.
3. **Sponsor level:** escalate strategic risks, timeline threats, or major trade-off decisions.

### Risk management

- Maintain a **Risk Register** with: ID, description, impact, likelihood, owner, mitigation, and status.
- Review and refresh risks weekly.
- Tie mitigation actions to owners and due dates to avoid stale high-risk items.

## Quality Standards and Acceptance Criteria

- Every backlog item must include clear, testable **acceptance criteria** before implementation starts.
- Teams apply a shared **Definition of Done** covering code quality, review completion, tests, and documentation updates.
- Testing strategy is multi-layered:
  - **Unit tests** for component-level behavior.
  - **Integration tests** for service interactions and data flow.
  - **End-to-end smoke tests** prior to release.
- Pull request workflow expectations:
  - Keep PRs focused and small (target ≤ 400 lines changed when practical).
  - Pass all CI checks (tests/lint/build gates configured for the repository).
  - Require at least one reviewer approval before merge.

## Related Process Documentation

- [Initiation](./process/initiation.md)
- [Planning](./process/planning.md)
- [Execution](./process/execution.md)
- [Release](./process/release.md)
- [Close & Retrospective](./process/close-and-retrospective.md)
