banco_palavras = {
    "jogos": [
        "Minecraft",
        "The Witcher 3",
        "Grand Theft Auto V",
        "Counter-Strike",
        "League of Legends",
        "The Legend of Zelda",
        "Elden Ring",
        "Fortnite",
        "Valorant",
        "God of War",
        "FIFA",
        "Resident Evil",
    ],
    "filmes": [
        "O Poderoso Chefão",
        "Titanic",
        "Avatar",
        "Interestelar",
        "Matrix",
        "Gladiador",
        "Vingadores",
        "Jurassic Park",
        "A Origem",
        "Coringa",
        "Toy Story",
        "Pulp Fiction",
    ],
    "paises": [
        "Brasil",
        "Japão",
        "Canadá",
        "França",
        "Austrália",
        "Itália",
        "Egito",
        "Argentina",
        "Alemanha",
        "Índia",
        "México",
        "Espanha",
    ],
    "adjetivos": [
        "feliz",
        "rápido",
        "inteligente",
        "corajoso",
        "forte",
        "bonito",
        "calmo",
        "engraçado",
        "generoso",
        "misterioso",
        "criativo",
        "sincero",
    ],
    "objetos": [
        "cadeira",
        "mesa",
        "computador",
        "telefone",
        "caneta",
        "livro",
        "espelho",
        "relógio",
        "mochila",
        "janela",
        "chave",
        "garrafa",
    ],
}

index_categorias = {
    0: "jogos",
    1: "filmes",
    2: "paises",
    3: "adjetivos",
    4: "objetos"
}

tries = 6
total_tries = tries
acertos = 0
acertos_letras = []

print("Escolha uma categoria: ")
print("1 - Jogos")
print("2 - Filmes")
print("3 - Países")
print("4 - Adjetivos")
print("5 - Objetos")

categoria_index = int(input("Digite a opção: ")) - 1
categoria = index_categorias[categoria_index]

print(f"A categoria possui {len(banco_palavras[categoria])} palavras\n")

posicao_palavra = int(input("Escolha a posição da palavra: "))
print()

palavra = banco_palavras[categoria][posicao_palavra]
tamanho_palavra = len(banco_palavras[categoria][posicao_palavra])

print("Você terá 6 tentativas para descobrir a palavra.")

texto = "_" * tamanho_palavra 
print(texto)
print()

print(f"Tentativas restantes: {tries}")

while True:

    letra = input("Digite uma letra: ")

    posicoes = []
    posicao = palavra.find(letra)

    while posicao != -1:

        posicoes.append(posicao)
        # Procura a próxima ocorrência avançando uma posição
        posicao = palavra.find(letra, posicao + 1)

    if len(posicoes) == 0:
        tries -= 1

        if tries < 1:
            print(f"Suas {total_tries} terminaram! \nA palavra era {palavra}")
            break

        print(f"Você errou! Tentativas restantes: {tries}")

    acertos_letras.append(letra)

    if letra not in acertos_letras:
        acertos += 1

    if acertos == tamanho_palavra:
        print(f"Parabéns! Você descobriu a palavra: {palavra}")
        break

    inserir = letra

    # Fatiamento e concatenação
    for posicao in posicoes:
        novo_texto = texto[:posicao] + inserir + texto[posicao+1:]

    texto = novo_texto

    print(f"Tentativas restantes: {tries}")
    print(novo_texto)

# Ver por que dá erro se errar primeira letra
# Para de imprimir mensagem de tentativas restantes repetidas quando errar