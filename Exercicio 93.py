dados = {'jogador': str(input('Fale o nome do jogador:')),
         'partidas': int(input('Fale quantas partidas ele jogou:'))
         }
gols_part = list()
# CASO NENHUM GOL
if dados['partidas'] == 0:
    print('Jogador que não jogou não tem como ter algum gol.')
# COLETA DE GOLS POR PARTIDA
acumulador = 0
if dados['partidas'] != 0:
    for partidas in range(1, 1 + dados['partidas']):
        # GOLS NO CAMPEONATO
        gols = int(input(f'Quantos gols na {partidas}º partida: '))
        acumulador += gols
        dados['gols'] = acumulador
        gols_part.append(gols)
# ADD NO DICT A LISTA DE GOLS TOTAL
    dados['gols no camp'] = gols_part
# Respondendo total de gols
    print(f'O jogador {dados['jogador']} fez \033[32m{dados['gols']}\033[0m gols em todo o campeonato.')
    print('-' * 25)
# GOLS POR PARTIDA
    for jogo, gol in enumerate(gols_part):
        print(f'Na {jogo + 1}º partida fez \033[32m{gol}\033[0m gols')
        print('-'*25)
