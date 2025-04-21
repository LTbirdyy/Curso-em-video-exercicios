cadastro = {'Nome': input('Fale o nome do trabalhador'),
            'CTPS': int(input('Forneça a carteira de trabalho(0 = não tem):')),
            'Idade': 2025 - int(input('Fale seu nascimento'))}
# CASO JA TENHA CLT
if cadastro['CTPS'] != 0:
    cadastro['Ano de contratação'] = int(input('Forneça o ano de contração:'))
    cadastro['Salario'] = int(input('Forneça o salário do funcionário'))
# RESPOSTA
for k, v in cadastro.items():
    print(f'{k} = {v}')
    if cadastro['CTPS'] != 0:
        if v == cadastro['Ano de contratação']:
            print(f'Ele se aposentará em {cadastro['Ano de contratação'] + 35} ')
