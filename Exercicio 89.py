lista_temp = []
lista_final = []
quantidade = int(input('Quantos alunos você quer colocar na lista:'))
# COLETA DE DADOS DOS ALUNOS
for alunos in range(1, quantidade+1):
    for dados in range(0, 3):
        if dados == 0:
            lista_temp.append(input(f'Fale o nome do {alunos}º aluno:'))
        if dados == 1:
            n1 = float(input(f'Fale a primeira nota do {alunos}º aluno:'))
            lista_temp.append(n1)
        if dados == 2:
            n2 = float(input(f'Fale a segunda nota do {alunos}º aluno:'))
            lista_temp.append(n2)
# CALCULANDO MÉDIA
    lista_temp.append((n1 + n2) / 2)
    lista_final.append(lista_temp[:])
    lista_temp.clear()
print('=+'*24)
# RESPOSTAS
for resultados in lista_final:
    print(f'Notas de {resultados[0]}:'
          f'\nNota 1: {resultados[1]}'
          f'\nNota 2: {resultados[2]}'
          f'\nMédia final: {resultados[3]}')
    print('-'*20)
