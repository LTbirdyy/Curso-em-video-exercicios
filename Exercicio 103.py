def ficha(nome, gols):
    if nome == '':
        nome = '<Jogador_Desconhecio>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'{nome} marcou {gols} gol(s)'


print(ficha(nome=str(input('Fale o nome do jogador:')),
            gols=str(input('Fale quantos gols ele marcou:'))))
