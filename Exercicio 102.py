def fatorial(num, show=False):
    # CALCULANDO FATORIAL
    resposta = 1
    for i in range(num, 0, -1):
        resposta *= i

    # FAZENDO PASSO A PASSO

    if show:
        print('O paso a paso ficaria:')
        for i in range(num, 0, -1):
            if i != 1:
                print(i, end=' * ')
            else:
                print(i, end=' = ')

        return resposta

    # RETORNANDO CASO NAO QUEIRA PASSO A PASSO

    else:
        return f'O fatorial de {num} é {resposta}.'


# CÓDIGO PRINCIPAL

resultado = fatorial(num=int(input('Fale um número para eu calcular seu fatorial')),
                     show=bool(input('Deseja ver o passo a passo(caso não de enter)')))

print(resultado)
