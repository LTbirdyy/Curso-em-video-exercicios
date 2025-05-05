def maior(*num):
    maior = num[0]
    menor = num[0]

    for contador in range(1, len(num)):
        if maior < num[contador]:
            maior = num[contador]
        if menor > num[contador]:
            menor = num[contador]

    print(f'Dentre os {len(num)} números {num} o maior é {maior} e o menor é {menor}')


# Caso queira tornar personalizado os valores colocados
# lista_respostas = []
# cont = 0
# while True:
    # lista_respostas.append(int(input('Fale alguns numeros')))
    # if cont > 3:
        # continuar = str(input('Deseja adicionar mais algum número: ')).upper().strip()[0]
        # if continuar == 'N':
            # break
    # cont += 1

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
