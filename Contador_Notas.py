# Adicionei a nota de 200 que não estava presente no exercicio anterior
# funcionamento igual a retirada de um caixa 24hrs

valor = int(input())

print(valor)
notas = [200, 100, 50, 20, 10, 5, 2, 1]
for nota in notas:
    quantidade = valor // nota
    print(f"{quantidade} nota(s) de R$ {nota},00")
    valor %= nota
