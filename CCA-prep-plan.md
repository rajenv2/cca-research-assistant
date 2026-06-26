# Claude Certified Architect (CCA-F) — Full-Coverage Prep Plan

*Comprehensive version: covers all 5 exam domains end to end, regardless of current strength.* *Pace: 10–12 hrs/week → ~11–12 weeks.* *Last updated: June 25, 2026*

---

## How to read this plan

This replaces the earlier weak-area-only plan. The strategy is the same spine — **one build project that forces you through every domain** — but here every domain gets full treatment, including the ones you're already "ok" at, because the exam is closed-book and tests judgment across all five areas.

The operating loop for each phase is the same three beats:

> **Course → Build → Study & self-quiz.** Take the relevant course for vocabulary, immediately build the matching piece, then consolidate with notes and timed questions.

Do **not** finish all the courses first. Only ~5 of Anthropic's courses map to this 301 exam, and recall-only study doesn't transfer to an implementation exam. Interleave.

---

## The exam, confirmed

| Item | Detail |
| :---- | :---- |
| Name | Claude Certified Architect — Foundations (CCA-F) |
| Level | 301 / advanced — assumes you already build with Claude |
| Format | 60 questions (multiple-choice + multi-select), 120 minutes, online webcam proctor |
| Scoring | Scaled 100–1000; **pass = 720** |
| Closed-book | No Claude, no docs, no external tools during the exam |
| Scenarios | 4 drawn from a pool of 6: support-resolution agent, multi-agent research system, Claude Code in CI/CD, structured data extraction, developer-productivity tools, conversational AI patterns |
| Cost | $99/attempt (retakes also $99). Free for the first 5,000 attempts from Claude Partner Network member companies |
| Access | Currently gated behind Partner Network access; public access signaled, no date yet |
| Prereqs (recommended, not enforced) | 200-level courses + ~6 months hands-on with Claude API, Agent SDK, Claude Code, MCP |

**Two practical notes:**

1. Partner Network membership is free for any company that declares interest in building with Claude — that's the path to a free attempt and to access while it's gated. Worth checking if your employer can register, and submitting the [access request form](https://anthropic.skilljar.com/claude-certified-architect-foundations-access-request) early since it's the long pole.
2. Nothing blocks you from building toward it now. "Recommended" prereqs are not gates.

---

## Domain weights — and why full coverage matters

| # | Domain | Weight | Covered in phase |
| :---- | :---- | :---- | :---- |
| 1 | Agentic Architecture & Orchestration | 27% | Phase 3 |
| 2 | Claude Code Configuration & Workflows | 20% | Phase 4 |
| 3 | Prompt Engineering & Structured Output | 20% | Phases 1 & 5 |
| 4 | Tool Design & MCP Integration | 18% | Phase 2 |
| 5 | Context Management & Reliability | 15% | Phases 4 & 5 |

Even your stronger domains (3 at 20%, parts of 2) are nearly as heavily weighted as your weak ones. At a 720 pass bar with no open book, you can't afford to leave the "ok-ish" areas unrehearsed. This plan rehearses all five.

---

## The build project (the spine)

**A multi-agent research assistant with a custom MCP backend, shipped through CI.**

- **Orchestrator agent** delegating to **subagents** (searcher, summarizer, fact-checker) → Domain 1
- **One MCP server you write yourself** exposing tools + a resource the agents call → Domain 4
- **Structured output** everywhere — validated JSON schemas for extraction and agent handoffs → Domain 3
- **GitHub Actions CI** running Claude Code for automated review + test generation on every PR → Domain 2
- **Error handling + human-in-the-loop escalation** when an agent is low-confidence or a tool fails → Domain 5
- **Context strategy** — long-document handling, passing context between agents without blowing the window → Domain 5

Everything you need to learn has a home in this one build.

---

## The course track (exam-relevant only)

Take these five, interleaved as noted. Skip the AI Fluency tracks — they're general-audience and won't appear on a 301 exam.

| Course | Maps to | Take during |
| :---- | :---- | :---- |
| [Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api) | API, tool use, structured output, batches | Phase 1 |
| [Intro to Model Context Protocol](https://anthropic.skilljar.com/introduction-to-model-context-protocol) | MCP servers/clients | Phase 2 |
| [MCP: Advanced Topics](https://anthropic.skilljar.com/model-context-protocol-advanced-topics) | Sampling, transport, FS access, production MCP | Phase 2 |
| [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) | Claude Code config + CI workflows | Phase 4 |
| [Introduction to Agent Skills](https://anthropic.skilljar.com/introduction-to-agent-skills) | Skills in Claude Code | Phase 4 |

There is no standalone Agent SDK course — Phase 3 is docs- and build-driven (Anthropic Agent SDK docs + the community guide's Chapter 3).

---

## Week 0 — Pre-flight (do this now, ~2 hrs)

- Submit the Partner Network / exam access request; it gates your eventual booking, so start it early.
- Set up your dev environment: Claude API key, Python 3.11+ (FastMCP) or Node (MCP SDK), Claude Code installed, a fresh GitHub repo for the project.
- Skim the community study guide's table of contents so you know where to look later. Treat it as a study aid; cross-check load-bearing claims against the official docs it cites.

---

## Phase 1 — API + tool use + structured output foundations (Weeks 1–2)
**Domain 3 (part 1), foundation for everything**

- **Course:** Building with the Claude API — finish it end to end. It sets the request/response vocabulary the exam uses.
- **Study:** Request structure, message roles, `stop_reason`, system prompts, the context window. Then `tool_use`: tool definitions, the `tool_choice` parameter, JSON Schema for structured output, and syntax-vs-semantic tool errors. Also skim the **Message Batches API** (when batch vs synchronous, `custom_id`, failure handling, SLA) — it's a small but testable corner.
- **Build:** A single-call app, then add function calling, then structured JSON output validated against a schema.
- **Deliverable:** A script that extracts structured data from a messy document into validated JSON, with at least one tool call in the loop.
- **Exam focus:** `tool_choice` modes, `stop_reason` values, schema design for reliable structured output, syntax vs semantic errors.
- **Self-check:** Can you explain, from memory, every field in a tool-use request/response cycle?

---

## Phase 2 — Tool design & MCP integration (Weeks 3–4)
**Domain 4 — 18%**

- **Courses:** Intro to MCP, then MCP: Advanced Topics.
- **Study:** Tools **vs** resources (know the distinction cold — common trap), server configuration, the `isError` flag, and MCP resources. From the advanced course: sampling, notifications, transport options, and what changes for a production server.
- **Build:** Your own MCP server (FastMCP in Python or the Node SDK). Expose 2–3 tools and 1 resource. Connect it to Claude Code and to your Phase 1 app; watch how the model decides which tool to call.
- **Deliverable:** A working MCP server (the agents will use it later) + a short README on your tool-design choices: naming, descriptions, error returns, tool vs resource.
- **Exam focus:** tool-description quality, tool vs resource, `isError` semantics, auth/error handling at the tool boundary.
- **Self-check:** Given a capability, can you decide tool vs resource and justify it in one sentence?

---

## Phase 3 — Agentic architecture & orchestration (Weeks 5–7)
**Domain 1 — 27%, the heaviest domain**

- **Source:** Anthropic Agent SDK docs + community guide Chapter 3 (no dedicated course).
- **Study:** The agentic loop, `AgentDefinition` config, the **hub-and-spoke** coordinator/subagent model, the `Task` tool for spawning subagents (coordinator's `allowedTools` must include `Task`; subagents need full context in the prompt — they don't inherit it), parallel vs sequential subagents, and **hooks** (PreToolUse / PostToolUse — e.g. normalizing tool output, blocking disallowed actions). Add **task decomposition** strategies (fixed pipelines / prompt chaining vs dynamic adaptive decomposition) and multi-pass review patterns.
- **Build:** The orchestrator + 2–3 subagents. Make them call your MCP server. Deliberately practice context passing: what the orchestrator hands down, what comes back, how to avoid context bloat. Add a hook.
- **Deliverable:** A working multi-agent flow + a written list of 3 tradeoffs you hit (one big agent vs many small; parallel vs sequential; what to isolate per subagent).
- **Exam focus:** when to use multi-agent vs single agent, delegation boundaries, context isolation, hooks, the `Task` tool contract.
- **Self-check:** Can you explain when *not* to use multi-agent, and why a subagent fails without context in its prompt?

---

## Phase 4 — Claude Code, CI/CD & reliability (Weeks 8–9)
**Domain 2 — 20% + Domain 5 (part 1) — 15%**

- **Courses:** Claude Code in Action, Introduction to Agent Skills.
- **Study (Domain 2):** the `CLAUDE.md` hierarchy, `@path` file imports, the `.claude/rules/` directory, custom slash commands and Skills (`.claude/skills/`), planning mode vs direct execution, `/compact`, `/memory`, `fork_session`/session management, and the **Claude Code CLI for CI/CD**.
- **Study (Domain 5):** error categories and anti-patterns in multi-agent systems, structured subagent errors, coverage annotations in synthesis (FULL/PARTIAL coverage), and human-in-the-loop — when to escalate, escalation patterns, structured handoff protocols, confidence calibration.
- **Build:** Add `CLAUDE.md` + configure MCP servers and Skills for the repo. Wire a GitHub Actions pipeline running Claude Code on each PR for review and/or test generation (this *is* one of the six exam scenarios). Add retries, graceful tool-failure handling, and a human-in-the-loop escalation path on low confidence.
- **Deliverable:** A green CI pipeline + a documented escalation/error-handling design.
- **Exam focus:** CLAUDE.md mechanics, planning mode, CI integration patterns, error-handling anti-patterns, when to escalate.
- **Self-check:** Can you sketch the CLAUDE.md resolution order and name three things that belong in CI vs local?

---

## Phase 5 — Prompt engineering, structured output & context management (Week 10)
**Domain 3 (part 2) — 20% + Domain 5 (part 2)**

This is a full domain, not just "polish." Give it real time.

- **Study (Domain 3):** few-shot prompting, explicit criteria vs vague instructions, prompt chaining, the "interview" pattern, validation and retry-with-feedback, self-correction. Tighten every prompt and schema across the project.
- **Study (Domain 5):** extract facts into a separate block, trimming tool results (PostToolUse hooks), position-aware input, scratchpad files, delegating to subagents to protect context, structured state persistence for crash recovery, and **provenance** (attribution-loss problem, handling conflicting data, including dates, rendering by content type).
- **Build/refine:** Apply few-shot + retry-with-feedback to your extraction and agent handoffs; add a scratchpad + state-persistence step to the orchestrator.
- **Exam focus:** few-shot design, structured-output reliability, context boundaries, provenance, retry/self-correction patterns.
- **Self-check:** Can you name three context-management tactics and the failure each one prevents?

---

## Week 11 — Practice exams + gap hunt

- Take questions under timed, closed-book conditions — use the repo's `practical_test_en.html` and any other banks you can find. Treat it like the real thing.
- Log every miss **by domain**. Re-study only what you miss; your misses are your real syllabus now.
- Re-run the readiness checklist below honestly.

---

## Week 12 — Mock + register

- Full 120-min timed mock. If you're consistently clearing ~720-equivalent across all five domains, register.
- Confirm Partner Network access / free-attempt eligibility before booking (you started this in Week 0).

---

## Full domain-coverage checklist

Tick every box before booking — this is the "irrespective of strengths" guarantee.

**Domain 1 — Agentic Architecture (27%)**
- [ ] Agentic loop + `AgentDefinition`
- [ ] Hub-and-spoke coordinator/subagent
- [ ] `Task` tool contract + context passing
- [ ] Hooks (PreToolUse / PostToolUse)
- [ ] Parallel vs sequential; when NOT to use multi-agent
- [ ] Task decomposition: fixed vs dynamic

**Domain 2 — Claude Code Workflows (20%)**
- [ ] CLAUDE.md hierarchy + `@path` imports
- [ ] `.claude/rules/`, slash commands, Skills
- [ ] Planning mode, `/compact`, `/memory`, `fork_session`
- [ ] Claude Code CLI in CI/CD

**Domain 3 — Prompt Engineering & Structured Output (20%)**
- [ ] Few-shot, explicit criteria, prompt chaining, interview pattern
- [ ] Validation, retry-with-feedback, self-correction
- [ ] JSON Schema for structured output
- [ ] Batches API basics

**Domain 4 — Tool Design & MCP (18%)**
- [ ] Tools vs resources
- [ ] Server config + `isError`
- [ ] Tool naming/description quality
- [ ] Auth/error handling at the boundary; production concerns

**Domain 5 — Context Management & Reliability (15%)**
- [ ] Error categories + anti-patterns
- [ ] Human-in-the-loop / escalation / structured handoff
- [ ] Context tactics: fact extraction, trimming, scratchpads, state persistence
- [ ] Provenance + conflicting-data handling

---

## Readiness checkpoints

Don't book until you can honestly say:

- I've built and deployed a multi-agent app with subagents, not just read about one.
- I wrote an MCP server from scratch and can explain tool-vs-resource and tool-description tradeoffs.
- I have Claude Code running in a CI pipeline doing review or test gen.
- I can produce reliable structured output and explain few-shot + retry-with-feedback.
- I can explain when *not* to use multi-agent, and when to escalate to a human.
- I can name concrete context-management tactics and the failure each prevents.
- I'm scoring around the 720 threshold on timed, closed-book practice **across all five domains**.

From "just getting started," a realistic window is 3–6 months. This plan is ~11–12 weeks at 10–12 hrs/week — the focused end. If a domain is shakier than expected at its phase's self-check, slow down rather than push ahead; the build carries forward.

---

## Resources

- Community study guide (treat as aid, cross-check against official docs): [paullarionov/claude-certified-architect](https://github.com/paullarionov/claude-certified-architect) — see `guide_en.MD` and `practical_test_en.html`
- Anthropic Academy courses: linked inline in the course track above

## Sources

- [Claude Certified Architect Exam: Cost, Format, Pass Rate (2026) — FindSkill.ai](https://findskill.ai/blog/claude-certified-architect-exam-cost-format-pass-rate/)
- [Inside Anthropic's Claude Certified Architect Program — DEV Community](https://dev.to/mcrolly/inside-anthropics-claude-certified-architect-program-what-it-tests-and-who-should-pursue-it-1dk6)
- [The Claude Certified Architect Exam: 5 Domains, 6 Scenarios — DEV Community](https://dev.to/aws-builders/the-claude-certified-architect-exam-5-domains-6-scenarios-and-everything-you-need-to-know-4le3)
- [Claude Certified Architect: Anthropic's First Official Certification — Zen van Riel](https://zenvanriel.com/ai-engineer-blog/claude-certified-architect-anthropic-certification-guide/)
- [Claude Certified Architect — Foundations study materials (community)](https://github.com/paullarionov/claude-certified-architect)
