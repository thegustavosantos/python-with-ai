
import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Variável de ambiente GEMINI_API_KEY não está definida")
os.environ["GOOGLE_API_KEY"] = api_key

mensagens_emails = [
    "Olá Carlos, identificamos uma tentativa de acesso não autorizada à sua conta a partir de um novo dispositivo. Se não foi você, redefina sua senha imediatamente.",
    "Mariana, informamos que sua solicitação de férias para o período de 10/09 a 25/09 foi aprovada pela gestão. Bom descanso!",
    "Lucas, sua transferência Pix no valor de R$ 250,00 para João Santos foi realizada com sucesso. Chave de autenticação: 9f8e7d6c.",
]

client = genai.Client()

def resumidor_de_emails(lista_de_emails):
    lista_de_resumos = []

    for numero, email in enumerate(lista_de_emails):
        resposta = client.models.generate_content(
            model="gemini-3-flash-preview", 
            contents=f"""Vou te mandar o corpo de um e-mail. Quero que você o resuma em apenas 1 linha,
                    passando o intuito daquele e-mail. Segue o e-mail: {email}"""
        )
        #print(resposta.text)
        print(f"Email {numero + 1}: {resposta.text}")
        lista_de_resumos.append(f"Email {numero + 1}: {resposta.text}")
        print("-" * 50)

    return lista_de_resumos

resume_list = resumidor_de_emails(mensagens_emails)

with open("data/lista-de-resumos.txt", "w", encoding="utf-8") as file:
    file.writelines("\n".join(resume_list))

nova_lista_de_resumos = []
# leitura da lista com for
with open("data/lista-de-resumos.txt", "r", encoding="utf-8") as file:
    for line in file:
        nova_lista_de_resumos.append(line.strip())


# leiura da lista com read
conteudo = ""
with open("data/lista-de-resumos.txt", "r", encoding="utf-8") as file:
    nova_lista_de_resumos = file.read();

# leiura da lista com readlines
nova_lista_de_resumos_dois = []
with open("data/lista-de-resumos.txt", "r", encoding="utf-8") as file:
    nova_lista_de_resumos_dois = file.readlines()