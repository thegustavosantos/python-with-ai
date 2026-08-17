# 1. read the file reviews.csv with pandas and store it in a DataFrame called df_reviews
# 2. show the dataframe
# 3. call an external API model such as Gemini or Groq to say if is Positivo, Negative or Neutral the review in the column "reviewText"
# 4. create a new column called "sentiment" in the DataFrame with the result of the API call
# 5. show the new DataFrame with the new column "sentiment"
# 6. Filter negative reviews and store them in a new DataFrame called df_negative_reviews
# 7. Find distinct categories for the negative reviews using an external API model such as Gemini or Groq

import os
import json
import pandas as pd
from groq import Groq

#1.
df_reviews = pd.read_csv("data/reviews.csv")

#2. 
print(df_reviews.head())

#3.

def get_sentiment(review_text):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("Variável de ambiente GROQ_API_KEY não está definida")
    client = Groq()
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": f"Classify the following review as Positive, Negative or Neutral: {review_text}, return only de pure text, unformatted"
            }
        ],
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )
    return completion.choices[0].message.content.strip()

#4.
df_reviews["sentiment"] = df_reviews["reviewText"].apply(get_sentiment)

#5.
print(df_reviews.head())

#6.
df_negative_reviews = df_reviews[df_reviews["sentiment"] == "Negative"]
negative_reviews = df_negative_reviews["reviewText"]

negative_reviews_str = "#####".join(negative_reviews)

#7. 
def get_reason_for_negative_review(negative_reviews_str):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("Variável de ambiente GROQ_API_KEY não está definida")
    client = Groq()
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": 
                    f"""OUTPUT ONLY VALID JSON. 
                    You are a data specialist.

                    You will receive a single string that contains many reviews separated by the token '#####'. 
                    Here is the data:
                    {negative_reviews_str}

                    Task:
                    1️⃣ Identify up to **5** thematic categories that explain why the reviews are negative.  
                    2️⃣ For **each** selected review, return an **object** with **exactly** three keys:
                    - "origin_review": the original review **exactly as it appears** in the input (preserve punctuation, keep the original language).
                    - "origin_review_translated": a Portuguese translation of that review (keep the same meaning, no paraphrasing).
                    - "category": a short, lower‑case label (max 1 word) that groups the review with others.

                    Output **ONLY** a **single JSON array** that contains **all** objects (no extra text, no markdown, no explanations).  
                    If you cannot produce a valid JSON array, respond with an **empty array**: []  

                    **IMPORTANT RULES**  
                    - The response must start with the character `[` and end with the character `]`.  
                    - Do **not** add any whitespace or newline before the opening bracket or after the closing bracket.  
                    - Do **not** wrap the array in code fences (```) or any other markup.  
                    - Use **double quotes** for every string and key.  
                    - Do **not** add trailing commas.  

                    Example of a correct output (the model must follow **exactly** this shape):
                    [
                    {{
                        "origin_review": "I did not like the color of the product",
                        "origin_review_translated": "Eu não gostei da cor do produto",
                        "category": "design"
                    }},
                    {{
                        "origin_review": "The battery died after one week",
                        "origin_review_translated": "A bateria morreu depois de uma semana",
                        "category": "bateria"
                    }}
                    ]

                    The whole response **must be** valid JSON. Do not include any other text."""
            }
        ],
        temperature=0, #(ou 0.1) reduz a criatividade e aumenta a aderência ao formato.
        max_completion_tokens=2048,
        top_p=1,
        reasoning_effort="medium",
        stream=False,
        stop=None
    )
    # AI Response
    response_text = completion.choices[0].message.content.strip()
    print("AI return: " + response_text)
    return json.loads(response_text)

negative_review_categories = get_reason_for_negative_review(negative_reviews_str)
print(negative_review_categories)