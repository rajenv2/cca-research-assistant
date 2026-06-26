# CCA Research Assistant — Project Context

## What this is
A hands-on learning project for the Claude Certified Architect — Foundations
(CCA-F) exam. One app that exercises all five exam domains:
- MCP server with tools + resources (Domain 4) — DONE
- Multi-agent orchestrator + subagents (Domain 1) — IN PROGRESS
- GitHub Actions CI running Claude Code (Domain 2) — planned
- Error handling + human-in-the-loop escalation (Domain 5) — planned
- Prompt engineering + structured output (Domain 3) — planned

## My level
Just getting started. Explain the "why" behind each step, tie choices back to
the relevant exam domain, and prefer small, verifiable increments.

## Repo layout
- server.py — FastMCP server (search_notes, word_count, get_note). get_note
  raises ToolError to demonstrate the isError path.
- .claude/agents/ — subagents for the orchestrator (researcher so far)
- .venv — Python 3.12 virtual env (gitignored)

## Conventions
- Never commit secrets; API keys go in .env (gitignored)
- Commit in small steps with clear messages
- The MCP server is registered with Claude Code as "research-assistant"
