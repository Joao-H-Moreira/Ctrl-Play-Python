N = int(input())

total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0

for _ in range(N):
# Primeiro registrar quantidade de Experimentos
# Depois o numero de cobaias seguido das letras 
    
    quantia, tipo = input().split()
    quantia = int(quantia)
    total_cobaias += quantia
    if tipo == 'C':
        total_coelhos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'S':
        total_sapos += quantia

percentual_coelhos = (total_coelhos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_ratos = (total_ratos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_sapos = (total_sapos / total_cobaias) * 100 if total_cobaias > 0 else 0

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
