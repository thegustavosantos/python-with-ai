import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Variável de ambiente GEMINI_API_KEY não está definida")
os.environ["GOOGLE_API_KEY"] = api_key

client = genai.Client()
response = client.models.generate_content(model="gemini-3-flash-preview", 
                               contents="Conte quais são as principais cidade de São Paulo.")
print(response)