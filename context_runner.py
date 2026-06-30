import json
import os

STATE_FILE = "run_state.json"
SCRATCHPAD = "scratchpad.md"

# Simulated verbose tool results — like a real fetch/API would return.
SOURCES = [
    {"id": "src-1", "title": "MCP overview",
     "body": "MCP exposes tools and resources to a model. " * 20,
     "metadata": {"bytes": 5000, "raw_html": "<html>" + "x" * 500 + "</html>"},
     "confidence": 0.92},
    {"id": "src-2", "title": "Tools vs resources",
     "body": "A tool performs an action; a resource provides read-only context. " * 20,
     "metadata": {"bytes": 4200, "raw_html": "<html>" + "y" * 500 + "</html>"},
     "confidence": 0.88},
    {"id": "src-3", "title": "Unverified blog claim",
     "body": "Some say MCP replaces all APIs. " * 20,
     "metadata": {"bytes": 3100, "raw_html": "<html>" + "z" * 500 + "</html>"},
     "confidence": 0.30},
    {"id": "src-4", "title": "isError semantics",
     "body": "isError signals a tool failure back to the model. " * 20,
     "metadata": {"bytes": 2800, "raw_html": "<html>" + "w" * 500 + "</html>"},
     "confidence": 0.81},
]


def trim_result(raw):
    """Keep only what the coordinator needs; drop bulk html/metadata."""
    return {
        "id": raw["id"],
        "title": raw["title"],
        "summary": raw["body"][:60].strip() + "...",
        "confidence": raw["confidence"],
    }


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"processed": [], "findings": 0}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def append_scratchpad(line):
    with open(SCRATCHPAD, "a") as f:
        f.write(line + "\n")


def run():
    state = load_state()
    if state["processed"]:
        print(f"Resuming — already processed: {state['processed']}")
    processed_this_run = 0
    for raw in SOURCES:
        if raw["id"] in state["processed"]:
            print(f"  skip {raw['id']} (already done)")
            continue
        trimmed = trim_result(raw)
        raw_size = len(json.dumps(raw))
        trim_size = len(json.dumps(trimmed))
        print(f"  {raw['id']}: tool result {raw_size} chars -> {trim_size} kept in context")
        if trimmed["confidence"] < 0.5:
            print(f"     low confidence ({trimmed['confidence']}) -> ESCALATE to human")
            append_scratchpad(f"- ESCALATE: {trimmed['title']} (confidence {trimmed['confidence']})")
        else:
            append_scratchpad(f"- {trimmed['title']}: {trimmed['summary']}")
            state["findings"] += 1
        state["processed"].append(raw["id"])
        save_state(state)  # persist after EVERY step -> crash-safe
        processed_this_run += 1
        if os.environ.get("CRASH") == "1" and processed_this_run == 2:
            raise RuntimeError("simulated crash after 2 items")
    print(f"Done — {state['findings']} findings in {SCRATCHPAD}")


if __name__ == "__main__":
    run()
