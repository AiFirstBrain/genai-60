from dotenv import load_dotenv
from google import genai
load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain what an API is to a 10 year old boy, in maximum 5 sentences."
)
print(response.text)