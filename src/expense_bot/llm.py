import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

def parse_expense(text: str) -> dict:
    prompt = f"""
    Extract the expense from this message.
    Return JSON with these keys:
    - "amount": the number spent (a number)
    - "category": a short category such as "food", "transport", "shopping"
    - "note": any extra context the user gave, or null if none

    Message: {text}
    """
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json"),
    )

    return json.loads(response.text)