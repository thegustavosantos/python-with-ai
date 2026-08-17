import os

import pandas as pd
from google import genai

questions = [
    "Qual é a maior cidade de São Paulo?",
    "Qual é a menor cidade de São Paulo?",
    "Quantos habitantes tem a cidade de São Paulo?",
    "Qual é a cidade mais populosa do Brasil?",
    "Qual a cidade com mais segura do Brasil?"
]

def create_file_with_questions():
    with open("data/questions.txt", "w", encoding="utf-8") as file:
        for question in questions:
            file.write(question + "\n")

def read_questions_from_file():
    with open("data/questions.txt", "r", encoding="utf-8") as file:
        questions_from_file = [line.strip() for line in file]
    return questions_from_file

def get_answers_from_gemini(questions_from_file):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Variável de ambiente GEMINI_API_KEY não está definida")
    os.environ["GOOGLE_API_KEY"] = api_key

    client = genai.Client()
    answers = []

    for question in questions_from_file:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"Por favor, responda de maneira resumida em no máximo uma linha ou 10 palavras à seguinte pergunta: {question}"
        )
        answers.append(response.text)

    return answers

def save_questions_and_answers_to_csv(questions_list, answers_list):
    df = pd.DataFrame({
        "Pergunta": questions_list,
        "Resposta": answers_list
    })
    df.to_csv("data/questions_and_answers.csv", index=False, encoding="utf-8")
    print("Arquivo data/questions_and_answers.csv criado com sucesso!")
    print(df)  # Mostrar o DataFrame no console


create_file_with_questions();
questions_from_file = read_questions_from_file();
answers = get_answers_from_gemini(questions_from_file);
save_questions_and_answers_to_csv(questions_from_file, answers);