lista_dados = list()
lista_mulheres = list()
lista_velhos = list()
contador_pessoas = 0
# COLETA DE DADOS DE N PESSOAS
while True:
    contador_pessoas += 1
    print(f'Dados da {contador_pessoas}º pessoa')
    dados = {'nome': str(input('Fale o nome da pessoa:')),
             'idade': int(input('Fale a idade da pessoa:')),
             'sexo': str(input('Fale o sexo da pessoa[M/F]')).upper().strip()[0]
             }
    # SALVANDO NA LISTA geral
    lista_dados.append(dados)

    # SALVANDO NA LISTA MULHERES
    if dados['sexo'] == 'F':
        lista_mulheres.append(dados['nome'])

    # CALCULANDO MÉDIA
    acumulador_idade = 0
    for posicao in range(0, contador_pessoas):
            idade = lista_dados[posicao]['idade']
            acumulador_idade += idade
            media = acumulador_idade/contador_pessoas

    # SALVANDO NA LISTA PESSOAS COM IDADE ACIMA DE MÉDIA
    if dados['idade'] > media:
        lista_velhos.append(dados['nome'])

    # CONFIRMAÇÃO DE MAIS PESSOAS
    continuar = str(input('Deseja cadastrar mais pessoas[S/N]?')).upper().strip()[0]
    # CASO DA PRIMEIRA PESSOA
    if lista_dados[0]['idade'] > media and continuar == 'N':
        lista_velhos.append(lista_dados[0]['nome'])
    if continuar == 'N':
        break

# RESPONDENDO QUANTIDADE DE PESSOAS E MÉDIA
print('-'*30)
print(f'Ao todo tivemos \033[32m{contador_pessoas}\033[0m pessoas cadastradas.\n'
      f'Sendo a média da idade do grupo \033[32m{media:.2f}\033[0m.')

# REPPONDENDO MULHERES
if len(lista_mulheres) > 0:
    print('-'*30)
    print('As mulheres cadastradas foram:')
    for mulheres in lista_mulheres:
        print(f'\033[32m{mulheres}\033[0m', end=' ')

# RESPONDENDO PESSOAS COM IDADE ACIMA DA MÉDIA
if len(lista_velhos) > 0:
    print('\n'+'-'*30)
    print('As pessoas que são mais velhas que a média das idades do grupo são:')
    for velhos in lista_velhos:
        print(f'\033[32m{velhos}\033[0m', end=' ')
