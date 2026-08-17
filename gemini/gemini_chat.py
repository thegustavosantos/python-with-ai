import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Variável de ambiente GEMINI_API_KEY não está definida")
os.environ["GOOGLE_API_KEY"] = api_key

client = genai.Client()
chat = client.chats.create(model="gemini-3-flash-preview")

response = chat.send_message("Conte quais são as melhores cidades de São Paulo para morar.")
print(response.text)

history = chat.get_history();
print(history)