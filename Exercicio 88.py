from random import sample
# lista de 0 a 60
lista_opcoes = []
for c in range(0, 60):
    lista_opcoes.append(c)
lista_resultado = list()
# QUANTIA DE PALPITES
quantidade = int(input('Quantos palpites você quer que eu faça?'))
# PALPITES SENDO FEITOS
for jogos in range(0, quantidade):
    print(f'Jogo {jogos+1}.')
    for numeros in range(0, 6):
        escolha = sample(lista_opcoes, k=1)
        lista_resultado.append(escolha)
    for c in lista_resultado:
        print(c, end=' ')
    lista_resultado.clear()
    print()
