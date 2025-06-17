def prepara_acai(tamanho="medio", ingredientes=[]):
    print("\nPreparando um Açaí", tamanho, "com os seguintes ingredientes:")
    if ingredientes:
        for ingrediente in ingredientes:
            print("-", ingrediente)
    else:
        print("- Nenhum ingrediente escolhido.")

# Interface interativa
def escolher_acai():
    print("Bem-vindo à Acaiteria!")

    tamanhos_disponiveis = ["pequeno", "medio", "grande"]
    tamanho = input("Escolha o tamanho do Açaí (pequeno, medio, grande): ").strip().lower()
    if tamanho not in tamanhos_disponiveis:
        print("Tamanho inválido. Usando tamanho padrão: medio.")
        tamanho = "medio"

    ingredientes_disponiveis = ["granola", "banana", "paçoca", "morango", "kiwi", "leite em pó", "manga"]
    print("\nIngredientes disponíveis:")
    for i, ing in enumerate(ingredientes_disponiveis, 1):
        print(f"{i}. {ing}")

    ingredientes = []
    print("\nDigite os números dos ingredientes desejados (um por vez). Pressione Enter sem digitar nada para finalizar.")
    while True:
        escolha = input("Ingrediente nº: ").strip()
        if escolha == "":
            break
        if escolha.isdigit():
            indice = int(escolha) - 1
            if 0 <= indice < len(ingredientes_disponiveis):
                ingrediente = ingredientes_disponiveis[indice]
                if ingrediente not in ingredientes:
                    ingredientes.append(ingrediente)
                else:
                    print("Ingrediente já adicionado.")
            else:
                print("Número inválido. Tente novamente.")
        else:
            print("Entrada inválida. Digite apenas o número do ingrediente.")

    prepara_acai(tamanho=tamanho, ingredientes=ingredientes)

# Executa a função
escolher_acai()

