from google import genai
from google.genai import errors

from app.config import GEMINI_API_KEY, DEFAULT_MODEL


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_text(prompt: str) -> str:

    try:

        response = client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=prompt,
        )

        return response.text

    except errors.ServerError as e:

        print("\n[WARNING] Gemini AI is currently unavailable.")
        print("[WARNING] Continuing without AI-generated analysis.")
        print(f"[WARNING] Gemini error: {e}")

        return (
            "AI analysis is currently unavailable because "
            "the Gemini API returned a temporary server error (503). "
            "Please retry the AI analysis later."
        )

    except Exception as e:

        print(f"\n[ERROR] Gemini API error: {e}")

        return (
            "AI analysis could not be generated because of an API error."
        )