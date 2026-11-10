
import os
import re

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

model = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-120b"
)

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. Check your .env file."
    )

client = Groq(api_key=api_key)


def ask_ai(system_prompt, user_prompt):

    response = client.chat.completions.create(

        model=model,

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],

        temperature=0.3,

        # Limit generated tokens to reduce TPM usage
        max_completion_tokens=1000,

        # Use less reasoning to reduce token consumption
        reasoning_effort="low"

    )

    return response.choices[0].message.content.strip()


def clean_code(text):

    text = re.sub(
        r"^```(?:python)?\s*",
        "",
        text.strip()
    )

    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    return text.strip()
