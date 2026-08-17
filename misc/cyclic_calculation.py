lista = ['a', 'b', 'c', 'd']
for i in range(10):
    print(i)
    print(lista[i % len(lista)])  # Acessa sempre um índice válido na lista