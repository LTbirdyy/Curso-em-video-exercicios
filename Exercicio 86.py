# RECEBENDO DADOS
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Fale o valor para [{l},{c}]'))
# ESCREVENDO DADOS
for l in range(0, 3):
    for c in range(0, 3):
            print(f'[{matriz[l][c]:^4d}]', end=' ')
    print()
