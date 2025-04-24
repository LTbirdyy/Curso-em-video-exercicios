lista_dados_geral = list()
lista_gols = list()
total_gols = 0
# SEMPRE COMEÇA COM UM JOGADOR
total_jogadores = 1
while True:
    dados = {'jogador': str(input('Fale o nome do jogador:')),
             'partidas': int(input('Fale quantas partidas ele jogou:'))
             }
    # CONTAR GOLS OR PARTIDA
    print(f'Diga quantos gols por partida o jogador {dados['jogador']} fez.')
    for n_partida in range(1, 1 + dados['partidas']):
        gols = int(input(f'Quantos gols foram feitos na {n_partida}º partida:'))
        total_gols += gols
        # SALVANDO GOLS POR PARTIDA DE CADA JOGADOR
        lista_gols.append(gols)
        dados['total de gols'] = total_gols
        dados['gols por partida'] = lista_gols[:]
    # SALVANDO TODOS DADOS DOS JOGADORES CADASTRADOS
    lista_dados_geral.append(dados)
    # LIMPANDO LISTA DE GOLS e total de gols
    lista_gols.clear()
    total_gols = 0

    # PARAR LOOP INFINITO
    continuar = str(input('Deseja adicionar outro jogador?[S/N]')).upper().strip()[0]
    if continuar != 'N':
        total_jogadores += 1
    print('-' * 50)
    if continuar == 'N':
        break

# GOLS POR PARTIDA
for n_jogadores in range(0, total_jogadores):
    print('-' * 50)
    for partida, gols_feitos in enumerate(lista_dados_geral[n_jogadores]['gols por partida']):
        print(f'Na \033[32m{1 + partida}º\033[0m partida do \033[32m{1 + n_jogadores}º\033[0m jogador '
              f'foram feitos \033[32m{gols_feitos}\033[0m')
    print(f'Ficando com um total de \033[32m{lista_dados_geral[n_jogadores]['total de gols']}\033[0m gols.')
print('-' * 50)
