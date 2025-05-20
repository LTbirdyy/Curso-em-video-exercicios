def lerint(num):
    while True:
        if num.isnumeric():
            num = int(num)
            break

        else:
            print('\033[31mValor fornecido não é um número\033[0m')
            num = input('Fale algum número:')
    return num


resposta = lerint(num=input('Fale algum número:'))
print(f'Você digitou {resposta}')
