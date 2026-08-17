# python-with-ai

Coleção de scripts em Python usados para estudar integração com diferentes APIs de LLM (Google Gemini, Anthropic Claude, Groq e um modelo local via LM Studio), além de exercícios de manipulação de dados com pandas.

## Estrutura

```
python-with-ai/
├── gemini/              # Exemplos com a API do Google Gemini
├── claude/              # Exemplo de chatbot com a API da Anthropic
├── groq/                # Exemplo de streaming com a API da Groq
├── local_llm/           # Exemplo chamando um modelo local (LM Studio) via SDK da OpenAI
├── pandas_exercises/     # Exercícios de pandas, incluindo análise de sentimento com IA
├── misc/                # Scripts soltos de estudo (lógica geral de Python)
└── data/                # Arquivos de entrada/saída (CSV/TXT) usados pelos scripts
```

## Pré-requisitos

- Python 3.10+
- Uma ou mais chaves de API, dependendo dos scripts que forem executados

## Instalação

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Configuração

Os scripts leem as chaves de API a partir de variáveis de ambiente — nenhuma chave fica no código. Defina apenas as que forem necessárias para os scripts que você for rodar:

| Variável            | Usada em          |
|---------------------|--------------------|
| `GEMINI_API_KEY`     | scripts em `gemini/` |
| `ANTHROPIC_API_KEY`  | `claude/claude_chatbot.py` |
| `GROQ_API_KEY`       | `groq/` e `pandas_exercises/pandas_review_with_ai_challenge.py` |

`local_llm/call_to_local_llm.py` espera um servidor local compatível com a API da OpenAI rodando em `http://localhost:1234/v1` (ex.: LM Studio).

## Como rodar

Os scripts que leem/gravam arquivos em `data/` assumem que são executados a partir da raiz do repositório, por exemplo:

```bash
python pandas_exercises/pandas_files.py
python gemini/gemini_chatbot.py
```
