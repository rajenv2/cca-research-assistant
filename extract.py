import json
from anthropic import Anthropic
from pydantic import BaseModel, ValidationError
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

MODEL = "claude-sonnet-4-6"


class Contact(BaseModel):
    name: str
    email: str
    phone: str
    company: str


SYSTEM = (
    "You extract contact details from messy text. "
    "Return ONLY a single JSON object with keys: name, email, phone, company. "
    "No prose, no markdown, no code fences."
)

# Few-shot example: teaches the model the exact output shape we want.
FEWSHOT_IN = "reach me — jordan lee, jordan@acme.io, ph 555-0100, at Acme Corp"
FEWSHOT_OUT = '{"name": "Jordan Lee", "email": "jordan@acme.io", "phone": "555-0100", "company": "Acme Corp"}'

MESSY = (
    "hey it's Priya Nair from Globex... easiest is email "
    "priya.nair@globex.com or call 555-0199. talk soon!"
)


def build_prompt(text):
    return (
        f"Example input: {FEWSHOT_IN}\n"
        f"Example output: {FEWSHOT_OUT}\n\n"
        f"Now extract from this input:\n{text}"
    )


def extract(text, max_attempts=3):
    messages = [{"role": "user", "content": build_prompt(text)}]
    for attempt in range(1, max_attempts + 1):
        resp = client.messages.create(
            model=MODEL, max_tokens=300, system=SYSTEM, messages=messages
        )
        raw = resp.content[0].text.strip()
        print(f"\n--- attempt {attempt} raw output ---\n{raw}")
        try:
            contact = Contact(**json.loads(raw))
            print(f"\n[OK] valid structured output:\n{contact.model_dump_json(indent=2)}")
            return contact
        except (json.JSONDecodeError, ValidationError) as e:
            print(f"\n[RETRY] validation failed: {e}")
            messages.append({"role": "assistant", "content": raw})
            messages.append({
                "role": "user",
                "content": f"That was not valid. Error: {e}. Return ONLY corrected JSON.",
            })
    raise RuntimeError("Failed to get valid output after retries")


if __name__ == "__main__":
    extract(MESSY)
