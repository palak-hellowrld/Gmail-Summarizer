from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

from google import genai

def summarizer(emails):
    client = genai.Client()
    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=f"Summarize the following emails for me {emails}. Ignore the links... I just want you to summarize all my emails into one big paragraph that is about 100 words max."
    )
    return (interaction.output_text)
