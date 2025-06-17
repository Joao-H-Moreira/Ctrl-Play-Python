print("===== CONTROLE DE EXPERIMENTOS COM COBA3IAS =====")
N = int(input("Quantos experimentos serão registrados? "))

total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0

print("\nDigite os dados no formato: quantidade tipo (ex: 10 C)")
print("Tipos válidos: C = Coelho | R = Rato | S = Sapo\n")

for i in range(1, N + 1):
    entrada_valida = False
    while not entrada_valida:
        try:
            dados = input(f"Experimento #{i}: ").strip().upper().split()
            if len(dados) != 2:
                raise ValueError("Formato inválido. Digite no formato: número tipo (ex: 10 C).")
            
            quantia = int(dados[0])
            tipo = dados[1]

            if tipo not in ['C', 'R', 'S']:
                raise ValueError("Tipo inválido. Use apenas C, R ou S.")

            total_cobaias += quantia
            if tipo == 'C':
                total_coelhos += quantia
            elif tipo == 'R':
                total_ratos += quantia
            elif tipo == 'S':
                total_sapos += quantia

            entrada_valida = True
        except ValueError as e:
            print(f"Erro: {e}\nTente novamente.")

# Cálculo de percentuais
def percentual(parcial):
    return (parcial / total_cobaias) * 100 if total_cobaias > 0 else 0

print("\n===== RELATÓRIO FINAL =====")
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual(total_coelhos):.2f} %")
print(f"Percentual de ratos: {percentual(total_ratos):.2f} %")
print(f"Percentual de sapos: {percentual(total_sapos):.2f} %")
