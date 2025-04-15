lista_temp = list()
lista_final = list()
contador = 0
maior_kg = 0
menor_kg = 0
# COLETA DE DADOS
while True:
    contador += 1
    nome = input(f'Fale o nome da {contador}ª pessoa:')
    peso = float(input(f'Fale o peso da {contador}ª pessoa em kg:'))
# ADICIONAR DADOS NAS LISTAS
    lista_temp.append(nome)
    lista_temp.append(peso)
    if contador == 1:
        maior_kg = lista_temp[1]
        menor_kg = lista_temp[1]
    if contador > 1:
        if maior_kg < lista_temp[1]:
            maior_kg = lista_temp[1]
        if menor_kg > lista_temp[1]:
            menor_kg = lista_temp[1]
    lista_final.append(lista_temp[:])
    lista_temp.clear()
# TERMINAR LOOP
    continuar = input('Deseja colocar mais alguém?[S/N]').upper().strip()[0]
    if continuar == 'N':
        break
# VER QUEM TEM OS MAIORES PESOS
print('As pessoas com maiores pesos foram:')
for pessoa in lista_final:
    if pessoa[1] == maior_kg:
        print(f'{pessoa[0]}', end=', ')
print('\nAs pessoas com menores pesos foram:')
for pessoa in lista_final:
    if pessoa[1] == menor_kg:
        print(f'{pessoa[0]}', end=', ')
# RESPOSTA
print(f'\nAo todo você cadastrou {contador} pessoas e o maior peso foi {maior_kg} kg e o menor peso foi {menor_kg} kg')
