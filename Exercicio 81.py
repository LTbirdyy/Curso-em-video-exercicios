cont = 0
lista = []
while True:
    cont += 1
    numero = int(input('Fale alguns números:'))
    lista.append(numero)
    continuar = ' '
    if cont == 4:
        while continuar not in 'YN':
            cont = 0
            continuar = input('Deseja continuar[Y/N]').upper().strip()[0]
        if continuar == 'N':
            break
print(f'Foram escritos {len(lista)} números')
print('Ela escrita na order decrescente ficaria:')
lista.sort(reverse=True)
for c in lista:
    print(c, end=' ')
if 5 in lista:
    print(f'\nO valor 5 apareceu {lista.count(5)}.')
else:
    print('\nO valor 5 não apareceu.')
