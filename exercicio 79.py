lista = []
cont = 0
while True:
    cont += 1
    numeros = int(input('Fale alguns valores:'))
    if numeros not in lista:
        lista.append(numeros)
    if cont >= 3:
        continuar = input('Deseja continuar[Y/N]').strip().upper()[0]
        cont -= 3
        if continuar == 'N':
            break
print(sorted(lista))
