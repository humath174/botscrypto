import openai
from src.config import CHATGPT_API_KEY

openai.api_key = CHATGPT_API_KEY

def get_chatgpt_insight(prompt):
    """
    Obtient des insights de ChatGPT basés sur un prompt.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
    )
    return response.choices[0].text.strip()