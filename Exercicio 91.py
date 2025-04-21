from random import randint
jogadores = dict()
jogadores['jogador1'] = randint(1, 10)
jogadores['jogador2'] = randint(1, 10)
jogadores['jogador3'] = randint(1, 10)
jogadores['jogador4'] = randint(1, 10)
for resultados in sorted(jogadores, key=jogadores.get, reverse=True):
    print(resultados, jogadores[resultados])
print(jogadores)