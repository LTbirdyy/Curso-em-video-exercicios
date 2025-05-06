def voto(ano):
    idade = 2025 - ano
    if idade < 16:
        return f'Negado, a pessoa tem {idade} anos'
    if idade >= 18:
        return f'Voto obrigatório, a pessoa tem {idade} anos'
    if idade >= 16 or idade >= 70:
        return f'Voto facultativo, a pessoa tem {idade} anos'


# CÓDIGO PRINCIPAL
lista_resultados = []
while True:
    resposta = voto(int(input('Fale o ano do seu nascimento: ')))
    lista_resultados.append(resposta)

    # PARAR LOOP
    continuar = str(input('Deseja adicionar mais uma pessoa[S/N]')).upper().strip()[0]
    if continuar == 'N':
        break

# RESULTADOS
for pessoa, texto in enumerate(lista_resultados):
    print(f'A {pessoa + 1}º pessoa: {texto}')
    # ESPAÇAMENTO
    print('-'*53)
