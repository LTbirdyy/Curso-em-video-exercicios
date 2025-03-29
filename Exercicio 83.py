lista = []
parentese = parentese_1 = parentese_2 = 0
expressao = list(input('Escreva alguma expressão, exemplo (3+2), entre parentese:'))
for c in expressao:
    print(c)
    if c == '(':
        parentese_1 += 1
    if c == ')':
        parentese_2 += 1
    parentese = parentese_1 + parentese_2
if parentese_1 != parentese_2:
    print('EXPRESSÃO INVÁLIDA')
else:
    print('EXPRESSÃO VÁLIDA')
