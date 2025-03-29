lista = []
lista_impar = []
lista_par = []
cont = 0
while True:
    cont += 1
    numeros = int(input('Fale alguns números:'))
    lista.append(numeros)
#   LISTA PAR
    if numeros % 2 == 0:
        lista_par.append(numeros)
#   LISTA IMPAR
    else:
        lista_impar.append(numeros)
    continuar = ' '
    if cont == 4:
        cont = 0
        while continuar not in 'YN':
            continuar = input('Deseja continuar[Y/N]').upper().strip()[0]
    if continuar == 'N':
        break
print(f'A lista completa ficou:')
for c in lista:
    print(c, end=' ')
print('\nA lista dos números pares ficou:')
for p in lista_par:
    print(p, end=' ')
print('\nJá a lista dos impares ficou:')
for i in lista_impar:
    print(i, end=' ')
