import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("Variável de ambiente GROQ_API_KEY não está definida")
os.environ["GROQ_API_KEY"] = api_key

client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "user",
        "content": "O que é o Python?"
      }
    ],
    temperature=1, # 0 menos criativo possível, 2 mais criativo possível
    max_completion_tokens=2048,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")