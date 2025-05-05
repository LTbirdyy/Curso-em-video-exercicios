def contador():
    cont = 0
# CONTADOR DE 1 ATÉ 10
    for numeros in range(1, 11):
        cont += 1
        if cont != 10:
            print(numeros, end=' ')
        else:
            print(numeros)

    borda()
    cont = 0

# CONTANDO DE 10 ATE 1
    for numeros in range(10, 0, -2):
        cont += 1
        # METADE DE 10 POR ESTAR PULANDO DE 2 EM 2
        if cont != 5:
            print(numeros, end=' ')
        else:
            print(numeros)

    borda()

# CONTAGEM PERSONALIZADA
    print('Agora é sua vez de fazer a contagem:')

# COLETA DE DADOS
    inicio = int(input('Qual o primeiro número:'))
    fim = int(input('Qual o outro número:'))
    passo = int(input('A contagem será em quanto em quanto:'))
    ordem = str(input('Contagem deve ser: [Regressiva/Progressiva]')).upper().strip()[0]

# ORDEM REGRESSIVA MUDEI O FIM PELO INCIO E TROCOU O SINAL DA ORDEM
    if ordem == 'R':
        troca = 0
        troca = inicio
        inicio = fim
        fim = troca
        passo *= -1
        borda()
        for numeros in range(inicio,  1 - fim, passo):
            print(numeros, end=' ')

# ORDEM PROGRESSIVA MANTIVE NORMAL
    else:
        for numeros in range(inicio, 1 + fim, passo):
            print(numeros, end=' ')


def borda():
    print('-' * 15)


contador()
