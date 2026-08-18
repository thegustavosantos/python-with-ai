#ok  1 - Carregar um arquivo .txt, onde cada linha será um elemento de uma lista do Python
#ok 2 - Mandá-la ao modelo que você está rodando localmente para extrair, em formato JSON, onde cada item terá "usuário", "resenha_original", "resenha_pt", "avaliação (Positiva, Negativa, Neutra)
#ok 3 - Transformar a resposta do modelo em uma lista de dicionários Python
# 4 - Criar uma função que, dada uma lista de dicionários, percorre a lista faz 2 coisas:
# a) conta a quantidade de avaliações positivas, negativas e neutras;
# b) une cada item dessa lista em uma variável do tipo string com algum separador.

import json
import pandas as pd
from openai import OpenAI

df_feedbacks = pd.read_csv("data/feedbacks.csv", 
                        sep="$",
                        header=None,
                        names=["id", "user", "feedback"])
print(df_feedbacks.shape)



client_openai = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="llm-studio"
)

def clean_llm_response(response):
    return response.strip().removeprefix("```json").removesuffix("```").strip()

def parse_llm_json(raw_json):
    return json.loads(raw_json)

def get_sentiment_with_local_llm(feedbacks):
    llm_response = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            {
                "role": "system",
                "content": """
                                Você é um assistente especializado em análise de avaliações de usuários.
                                IMPORTANTE:
                                - A resposta deve começar com [ e terminar com ].
                                - Retorne somente um JSON válido.
                                - Não use markdown ou blocos de código.
                            """
            },
            {
                "role": "user",
                "content": f"""
                
                                Analise as seguintes avaliações:
                                {feedbacks}

                                Para cada avaliação recebida:
                                1. Identifique o usuário.
                                2. Mantenha a avaliação original exatamente como foi recebida.
                                3. Traduza a avaliação para português brasileiro.
                                4. Classifique a avaliação como "Positiva", "Negativa" ou "Neutra".

                                Não invente informações e retorne somente o JSON solicitado.

                                - Cada objeto deve possuir exatamente:
                                    "user" (string)
                                    "feedback" (string)
                                    "feedback_ptbr" (string)
                                    "sentiment" (string)
                                    - "feedbacks" deve ser exatamente: ("Positiva", "Negativa" ou "Neutra").
                                - IMPORTANTE: se o texto de "feedback" ou "feedback_ptbr" contiver aspas duplas ("),
                                  escape cada uma delas como \\" para manter o JSON válido.
                                Exemplo: [{{user:"4490351",feedback:"I did noit like this product",feedback_ptbr:"Eu não gostei desse produto",sentiment:"Negativo"}}]
                            """
            }
        ],
        temperature=0.0,
        max_tokens=50000
    )
    print(llm_response.choices[0].message.content)
    return clean_llm_response(llm_response.choices[0].message.content)

def final_output(feedbacks_with_sentiment):
    positive = 0;
    negative = 0;
    neutral = 0;
    sum_feedbacks = [];

    for feedback in feedbacks_with_sentiment:
        if feedback["sentiment"] == "Positivo":
            positive+=1
        elif feedback["sentiment"] == "Negativo":
            negative+=1
        elif feedback["sentiment"] == "Neutra":
            neutral+=1
        sum_feedbacks.append(str(feedback))

    print("total de feedbacks: ", len(sum_feedbacks))
    sum_feedbacks = ";".join(sum_feedbacks)
    print(sum_feedbacks)

    print(f"Positivas: {positive}")
    print(f"Negativas: {negative}")
    print(f"Neutras: {neutral}")
    print(f"Feedbacks: {sum_feedbacks}")


feedbacks_records = df_feedbacks[["user", "feedback"]].to_dict("records")
feedbacks_with_sentiment = parse_llm_json(get_sentiment_with_local_llm(feedbacks_records))
final_output(feedbacks_with_sentiment)