lista = []
lista_maior = []
lista_menor = []
for c in range(0, 5):
    valor = int(input(f'Fale um para posição {c} número:'))
    lista.append(valor)
for posição, v in enumerate(lista):
    if v == max(lista):
        lista_maior.append(posição)
    if v == min(lista):
        lista_menor.append(posição)
print(f'O maior valor é {max(lista)} e ele aparece nas posições {lista_maior}\n'
      f'O menor valor aé {min(lista)} e ele aparece nas posições {lista_menor}')
