import os
import anthropic

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("Variável de ambiente ANTHROPIC_API_KEY não está definida")

client = anthropic.Anthropic(api_key=api_key)

# Diferente do genai.Client(), a API da Anthropic não guarda o histórico
# pra você — cada chamada é stateless. Por isso mantemos a lista de
# mensagens na mão e reenviamos ela inteira a cada turno.
history = []

prompt = input("Digite sua pergunta: ")
while prompt != "sair":
    history.append({"role": "user", "content": prompt})

    response = client.messages.create(
        model="claude-opus-5",
        max_tokens=1024,
        messages=history,
    )

    reply = next(block.text for block in response.content if block.type == "text")
    print(reply)
    print("\n")

    history.append({"role": "assistant", "content": response.content})

    print(f"[Histórico até agora: {len(history)} mensagens]\n")

    prompt = input("Digite sua pergunta: ")
