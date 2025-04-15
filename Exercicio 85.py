numeros = [[], []]
print('Escreva 7 números para eu ordená-los e separar em par ou impar')
# RECEBER VALORES
for c in range(1, 8):
    valor = int(input(f'Fale o {c}ª número:'))
# SEPARAR LISTA EM PARES
    if valor % 2 == 0:
        numeros[0].append(valor)
# SEPARAR LISTA EM IMPARES
    else:
        numeros[1].append(valor)
print(f'Os números pares são {sorted(numeros[0])} e os impares são {sorted(numeros[1])}')
