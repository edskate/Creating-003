def main():
    score = 0

    print("Bem-vindo ao Quiz de Dança!")

    # Pergunta 1
    print("1. Qual é a principal parte do balé?")
    print("A. Pés")
    print("B. Mãos")
    print("C. Peitor")
    answer1 = input("Digite a letra da resposta: ")
    if answer1.lower() == "b":
        score += 1

    # Pergunta 2
    print("2. Qual é a principal técnica de dança em um balé?")
    print("A. Flexibilidade")
    print("B. Coordenação")
    print("C. Força")
    answer2 = input("Digite a letra da resposta: ")
    if answer2.lower() == "b":
        score += 1

    # Pergunta 3
    print("3. Qual é o nome do movimento em que as pernas se curvam para dentro?")

