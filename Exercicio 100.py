import random
# CRIANDO LISTA DE 1 ATÉ 10
numeros = []
for c in range(1, 11):
    numeros.append(c)


# SORTEAR DA LISTA

def sortear():
    lista_temp = random.sample(numeros, k=5)
    numeros.clear()
    numeros.append(lista_temp[:])
    print(f'Os números sorteados foram {lista_temp}')


# SOMAR NÚMEROS PARES
def somarpar():
    acumulador = 0
    for l in numeros:
        for i in l:
            if i % 2 == 0:
                acumulador += i
    print(f'A soma dos números pares aanteriores é {acumulador}')


# CÓDIGO PRINCIPAL

sortear()

somarpar()
