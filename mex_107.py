def dobro(numero):
    """
    :param numero: Recebe o valor para dobrar
    :return: Devolve o dobro
    """
    return numero * 2


def aumentar(numero, porcentagem):
    """
    :param numero: Número a sofrer aumento
    :param porcentagem: Valor em % do aumento
    :return: Valor final com a modificação
    """
    # Transformando 50% em 0.5 para cálculos
    porcentagem /= 100

    # Descobrindo o equivalente do aumento

    aumento = numero * porcentagem

    # ADD aumento no valor base do produto
    valor_final = numero + aumento

    return valor_final


def diminuir(numero, porcentagem):
    """
    :param numero: Número a sofrer desconto
    :param porcentagem: Valor em % do desconto
    :return: Valor final com a modificação
    """
    # Transformando, por exemplo, 50% em 0.5

    porcentagem /= 100

    # Descobrindo o equivalente do desconto

    desconto = numero * porcentagem

    # Subtraindo valor base com o desconto

    valor_final = numero - desconto

    return valor_final


def metade(numero):
    """
    :param numero: Valor a ser dividido
    :return: Metade do valor fornecido
    """
    return numero / 2


def moeda(valor):
    formatado = f'R$ {valor:.2f}'
    return formatado
