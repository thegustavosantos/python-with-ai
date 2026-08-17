import pandas as pd
import numpy as np

# Configurar a semente do gerador de números aleatórios
np.random.seed(42)

# Gerar 50 nomes de produtos
product_names = [f"Produto {i+1}" for i in range(50)]

# Categorias de exemplo
categories = ['Eletrônicos', 'Casa', 'Beleza', 'Esportes', 'Brinquedos', 'Alimentos', 'Moda', 'Automotivo']
categoria_produto = [np.random.choice(categories) for _ in range(50)]

# Preços entre R$5,00 e R$500,00
preco_produto = np.round(np.random.uniform(5.0, 500.0, size=50), 2)

# Quantidade de itens vendidos (inteiros)
itens_vendidos = np.random.randint(1, 1000, size=50)

# Avaliação do produto de 1.0 a 5.0 com uma casa decimal
avaliacao_produto = np.round(np.random.uniform(1.0, 5.0, size=50), 1)

# Montar DataFrame
df = pd.DataFrame({
    'nome produto': product_names,
    'categoria produto': categoria_produto,
    'preço produto': preco_produto,
    'itens vendidos': itens_vendidos,
    'avaliação do produto': avaliacao_produto,
})

if __name__ == '__main__':
    # Mostrar todas as 50 linhas
    pd.set_option('display.max_rows', 60)
    #print(df.to_string(index=False))
    #print(df)

    # Resumo estatístico (colunas numéricas)
    #print(df.describe())

    # Mostrar as categorias
    # print(df["categoria produto"])

    # Mostrar as categorias únicas
    # print(df["categoria produto"].unique())
    # print(set(df["categoria produto"]))

    # Filtrando elementros do DataFrame
    # df_filtrado = df[df["categoria produto"] == "Eletrônicos"]
    # df_filtrado = df[df["avaliação do produto"] < 2.0]
    # df_filtrado = df[(df["categoria produto"] == "Eletrônicos") & (df["preço produto"] >= 350.0)]
    # print(df_filtrado)

    # Saber o tamanho retorna (linhas, colunas) do DataFrame
    # print(df_filtrado.shape)  

    # Acessando uma linha específica do DataFrame
    # print(df.iloc[15])  # Acessando a linha de índice 15    
    # print(df.iloc[1: 15])  # Acessando as linhas de índice 1 a 14 (15 não incluso)

    # Criar um novo DataFrame com índice sendo os itens da coluna 'nome produto'
    df_indexed = df.set_index("nome produto")
    # print(df_indexed.head(10))

    # Exemplo de acesso usando o novo índice
    # print(df_indexed.loc["Produto 1"])

    # Exemplo de acesso a um intervalo de produtos usando o novo índice
    # print(df_indexed.loc["Produto 1":"Produto 5"])

    # Acessando múltiplas linhas e colunas específicas usando o novo índice
    # print(df_indexed.loc[["Produto 45", "Produto 40", "Produto 35"], ["preço produto", "categoria produto"]])  # Acessando o preço do Produto 45

    # Acessando o preço e avaliação dos produtos da categoria Eletrônicos
    # df_eletronicos = df_indexed[df_indexed["categoria produto"] == "Eletrônicos"]
    # print(df_eletronicos.loc[df_eletronicos.index, ["preço produto", "avaliação do produto"]])

    # Alterando a categoria dos produtos da categoria Brinquedos para Infanto-juvenil
    df_brinquedos = df_indexed[df_indexed["categoria produto"] == "Brinquedos"]
    # Consulta anterior
    print(df_indexed.loc[df_brinquedos.index, "categoria produto"])
    # Alteração da categoria 
    df_indexed.loc[df_brinquedos.index, "categoria produto"] = "Infanto-juvenil"
    # Consulta após alteração
    print(df_indexed.loc[df_brinquedos.index, "categoria produto"])
    print(df_indexed["categoria produto"].unique())