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

def classify_intent(text: str) -> str:
    prompt = f"""
    Decide if this message is LOGGING a new expense or ASKING a question about spending.
    Reply with exactly one word: "log" or "ask".

    Message: {text}
    """
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )
    return response.text.strip().lower()


def answer_question(question: str, expenses: list) -> str:
    prompt = f"""
    You are a helpful personal finance assistant.
    Here are the user's logged expenses (id, amount, category, note, date):
    {expenses}

    Answer the user's question using these expenses. Be concise and specific with numbers.
    If they ask for advice, give practical, friendly suggestions based on their spending.

    Question: {question}
    """
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
    )
    return response.text