import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Variável de ambiente GEMINI_API_KEY não está definida")
os.environ["GOOGLE_API_KEY"] = api_key

client = genai.Client()
chat = client.chats.create(model="gemini-3-flash-preview")

prompt = input("Digite sua pergunta: ")
while prompt != "sair":
    response = chat.send_message(prompt)
    print(response.text)
    print("\n")

    history = chat.get_history()
    print(f"[Histórico até agora: {len(history)} mensagens]\n")

    prompt = input("Digite sua pergunta: ")
