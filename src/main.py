from src.entrada import selecaoMetodoDoUsuario, selecaoDeValoresDoUsuario, converteValoresDeEntrada, \
    converteSelecaoMetodoDoUsuario, selecaoDeQuantidade, converteSelecaoDeQuantidade
from src.numeros_randomicos import gerarNumerosRandomicos

if __name__ == '__main__':
    metodoDeEntrada = selecaoMetodoDoUsuario()
    metodoDeEntrada = converteSelecaoMetodoDoUsuario(metodoDeEntrada)

    selecaoDeQuantidade = selecaoDeQuantidade()
    selecaoDeQuantidade = converteSelecaoDeQuantidade(selecaoDeQuantidade)

    valoresDeEntrada = selecaoDeValoresDoUsuario()
    valoresDeEntrada = converteValoresDeEntrada(valoresDeEntrada)

    numerosAleatorios = gerarNumerosRandomicos(metodoDeEntrada, selecaoDeQuantidade, **valoresDeEntrada)

    print('\nResultado:')
    acc = 0
    for i in range(len(numerosAleatorios)):
        acc += numerosAleatorios[i]
        print('numero', i + 1, ':', numerosAleatorios[i])
    with open('output.dst', 'w') as file:
        for item in numerosAleatorios:
            file.write(str(item) + '\n')
    print('Valor medio : ', acc / len(numerosAleatorios))
