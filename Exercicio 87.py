pares = 0
total_c3 = 0
maior_l2 = list()
# RECEBENDO OS DADOS
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Fale os valores para a posição [{l},{c}]'))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            total_c3 += matriz[l][2]
        if matriz[l][c] == matriz[1][c]:
            maior_l2.append(matriz[l][c])
# RESULTADO
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4d}]', end='')
    print()
# OPERAÇÕES
print('=^'*25)
print(f'A soma dos números pares é {pares}')
print(f'A soma dos números na terceira coluna é {total_c3}')
print(f'O maior valor na 2ª linha é {max(maior_l2)}')