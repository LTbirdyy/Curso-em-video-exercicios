def titulo(texto):
    tamanho = len(texto) + 2
    print('-' * tamanho)
    print(f'{texto:^{tamanho}}')
    print('-' * tamanho)


# Código principal
resposta = str(input('Fale alguma coisa:'))
titulo(texto=resposta)
