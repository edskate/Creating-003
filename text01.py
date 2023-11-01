# Criando uma lista de dados
pessoas = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 30},
    {"nome": "Pedro", "idade": 20}
]

# Acessando os dados da lista
print(pessoas[0]["nome"])  # Imprime "João"
print(pessoas[1]["idade"])  # Imprime 30

# Adicionando um novo item à lista
novo_pessoa = {"nome": "Ana", "idade": 28}
pessoas.append(novo_pessoa)

# Removendo um item da lista
pessoas.remove(pessoas[2])

# Iterando sobre a lista
for pessoa in pessoas:
    print(pessoa["nome"], pessoa["idade"])