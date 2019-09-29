import sys

from numeros_randomicos import metodoJson

TEXTO_DE_ERRO_NA_ENTRADA = 'Erro na entrada.'


def selecaoMetodoDoUsuario():
    entradaUsuario = fazEntradaSelecaoMetodoDoUsuario()
    validaSelecaoMetodoDoUsuario(entradaUsuario)

    return entradaUsuario


def fazEntradaSelecaoMetodoDoUsuario():
    print('Digite o metodo a ser executado:')
    print('1)', metodoJson[1])
    print('2)', metodoJson[2])
    print('3)', metodoJson[3])
    print('4)', metodoJson[4])
    entradaUsuario = input('entrada: ')

    return entradaUsuario


def validaSelecaoMetodoDoUsuario(entradaUsuario):
    verificaTipoSelecaoMetodoDoUsuario(entradaUsuario)
    verificaValorSelecaoMetodoDoUsuario(entradaUsuario)


def verificaTipoSelecaoMetodoDoUsuario(entradaUsuario):
    try:
        int(entradaUsuario)
    except ValueError:
        tratarErroDeEntrada()


def tratarErroDeEntrada():
    print(TEXTO_DE_ERRO_NA_ENTRADA)
    sys.exit()


def verificaValorSelecaoMetodoDoUsuario(entradaUsuario):
    numeroDeMetodos = len(metodoJson)
    entradaUsuario = int(entradaUsuario)

    if entradaUsuario < 1 or entradaUsuario > numeroDeMetodos:
        tratarErroDeEntrada()


def selecaoDeValoresDoUsuario():
    entradasUsuario = fazEntradaSelecaoDeValoresDoUsuarioComValidacao()

    return entradasUsuario


def selecaoDeQuantidade():
    entradaUsuario = fazEntradaDeQuantidade()
    validaSelecaoDeQuantidade(entradaUsuario)

    return entradaUsuario


def validaSelecaoDeQuantidade(entradaUsuario):
    try:
        int(entradaUsuario)
    except ValueError:
        tratarErroDeEntrada()


def fazEntradaDeQuantidade():
    return input('Digite a quantidade: ')


def fazEntradaSelecaoDeValoresDoUsuarioComValidacao():
    entradasUsuario = {}

    print('Digite apenas os valores necessarios:')

    entrada = input('Limite inferior: ')
    validaSelecaoDeValorDoUsuario(entrada)
    entradasUsuario['valorMenor'] = entrada

    entrada = input('Limite superior: ')
    validaSelecaoDeValorDoUsuario(entrada)
    entradasUsuario['valorMaior'] = entrada

    entrada = input('Moda: ')
    validaSelecaoDeValorDoUsuario(entrada)
    entradasUsuario['moda'] = entrada

    entrada = input('Media: ')
    validaSelecaoDeValorDoUsuario(entrada)
    entradasUsuario['media'] = entrada

    entrada = input('Variancia: ')
    validaSelecaoDeValorDoUsuario(entrada)
    entradasUsuario['variancia'] = entrada

    return entradasUsuario


def validaSelecaoDeValorDoUsuario(entradaUsuario):
    verificaTipoSelecaoDeValorDoUsuario(entradaUsuario)


def verificaTipoSelecaoDeValorDoUsuario(entradaUsuario):
    if entradaUsuario == '':
        return

    try:
        float(entradaUsuario)
    except ValueError:
        tratarErroDeEntrada()


def converteValoresDeEntrada(entradasUsuario):
    return dict([k, float(v)] for k, v in entradasUsuario.items() if v != '')


def converteSelecaoMetodoDoUsuario(entradaUsuario):
    return int(entradaUsuario)


def converteSelecaoDeQuantidade(entradaUsuario):
    return int(entradaUsuario)
