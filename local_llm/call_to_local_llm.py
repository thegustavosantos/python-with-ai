from openai import OpenAI

client_openai = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="llm-studio"
)

llm_response = client_openai.chat.completions.create(
    model="python.exe -m pip install --upgrade pip",
    messages=[
        {
            "role": "system",
            "content": "Você é um assistente de IA que sempre responde de maneira lúdica para que até crianças de 5 anos entendam."
        },
        {
            "role": "user",
            "content": "O que é uma IA Generativa?"
        }
    ],
    temperature=1.0
)

print(llm_response.choices[0].message.content)