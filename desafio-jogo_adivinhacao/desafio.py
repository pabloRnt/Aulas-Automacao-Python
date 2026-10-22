import re

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
        "O Poderoso Chefao",
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
        "Japao",
        "Canada",
        "França",
        "Australia",
        "Italia",
        "Egito",
        "Argentina",
        "Alemanha",
        "India",
        "Mexico",
        "Espanha",
    ],
    "adjetivos": [
        "feliz",
        "rapido",
        "inteligente",
        "corajoso",
        "forte",
        "bonito",
        "calmo",
        "engracado",
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
        "relogio",
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

while True:

    try: 
        categoria_index = int(input("Digite a opção: ")) - 1

        if categoria_index < 0 or categoria_index > len(index_categorias.keys()) - 1:
            continue

        categoria = index_categorias[categoria_index]
        break

    except:
        continue

print(f"A categoria \"{categoria}\" possui {len(banco_palavras[categoria])} palavras\n")

while True:

    try:

        posicao_palavra = int(input("Escolha a posição da palavra: "))

        if posicao_palavra < 1 or posicao_palavra > len(banco_palavras[categoria]):
            raise ValueError

        break

    except:
        print(f"Escolha uma posição entre 1 e {len(banco_palavras[categoria])}")
        continue

print()

palavra = banco_palavras[categoria][posicao_palavra]
tamanho_palavra = len(banco_palavras[categoria][posicao_palavra])

print("Você terá 6 tentativas para descobrir a palavra.")

texto = "_" * tamanho_palavra 
print(texto)
print()

print(f"Tentativas restantes: {tries}")

while True:

    letra = (input("Digite uma letra: ")).lower()

    if letra.lower() == "sair":

        print("Saindo...")
        break

    if not re.match(r"^[a-z]$", letra):

        continue

    letra_repetida = 0

    posicoes = []
    posicao = palavra.lower().find(letra)

    while posicao != -1:

        posicoes.append(posicao)
        # Procura a próxima ocorrência avançando uma posição
        posicao = palavra.find(letra, posicao + 1)

    if len(posicoes) == 0:
        tries -= 1

        if tries < 1:
            print(f"Suas {total_tries} terminaram! \nA palavra era {palavra}")
            break

        print(f"Você errou!")

    else: 

        if letra not in acertos_letras and not letra_repetida:

            acertos += 1
            letra_repetida = not letra_repetida
            acertos_letras.append(letra)

            #print(acertos)

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

    print(f"Tentativas restantes: {tries}")

#Adicionar espaços nos sublinhados para palavras compostas (Resident Evil)