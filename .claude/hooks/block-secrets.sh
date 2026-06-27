#!/bin/bash
input=$(cat)
query=$(printf '%s' "$input" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('query', ''))")
if printf '%s' "$query" | grep -qi 'password'; then
  echo "Blocked by guardrail: searching for credentials is not allowed." >&2
  exit 2
fi
exit 0
