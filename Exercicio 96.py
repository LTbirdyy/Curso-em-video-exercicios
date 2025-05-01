def area(largura, comprimento):
    separador()
    resposta = largura * comprimento
    print(f'A área do seu terreno de dimensões {largura} m e {comprimento} m resulta em {resposta} m²')


def separador():
    print('-'*30)


# CODIGO PRINCIAL
while True:
    N1 = float(input('Fale a largura do terreno em metros: '))
    N2 = float(input('Fale o comprimento do terreno em metros: '))
    area(largura=N1, comprimento=N2)
    separador()
    cont = str(input('Deseja continuar[S/N]')).upper().strip()[0]
    if cont == 'N':
        break
    separador()
print('Programa finalizado.')
