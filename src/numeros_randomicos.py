import random
# Criar métodos de geração de números aleatórios como Uniforme, triangular, exponencial e natural.
import math

metodoJson = {
    1: "uniforme",
    2: "triangular",
    3: "exponencial",
    4: "natural"
}

# x = a + (b-a)*R   R = Random number - a={valor menor} b={valor maior}
def gerarRandomicoUniforme(valorMenor, valorMaior):
    return valorMenor + (valorMaior - valorMenor)*random.random()

# Slide professor.
def gerarRandomicoTriangular(valorMenor, valorMaior, moda):
    U = random.random()
    if (U < (moda-valorMenor)/(valorMaior-valorMenor)):
        return valorMenor + (U*(moda-valorMenor)*(valorMaior-valorMenor)) ** 0.5
    else:
        return valorMaior - ((1-U)*(valorMaior-moda)*(valorMaior-valorMenor)) ** 0.5


def gerarRandomicoExponencial(limiteInferior, media):
    # http://mpsantos.com.br/simul.pdf - Página 66 e 67
    U = random.random()
    alpha = 1 / (media - limiteInferior)
    x = limiteInferior - (1 / alpha) * math.log(U)
    return x


def gerarRandomicoNatural(media, variancia):
    U1 = random.random()
    U2 = random.random()
    Z = math.sqrt(-2 * math.log(U1)) * math.sin(2 * math.pi * U2)
    X = media + variancia * Z
    return X


def gerarNumerosRandomicos(metodo, qtde, valorMenor=None, valorMaior=None, moda=None, media=None, variancia=None):
    numerosAleatorios = []
    if metodoJson[metodo] == 'uniforme':
        for _ in range(qtde):
            numerosAleatorios.append(
                gerarRandomicoUniforme(valorMenor, valorMaior))
    if metodoJson[metodo] == 'triangular':
        for _ in range(qtde):
            numerosAleatorios.append(
                gerarRandomicoTriangular(valorMenor, valorMaior, moda))
    if metodoJson[metodo] == 'exponencial':
        for _ in range(qtde):
            numerosAleatorios.append(
                gerarRandomicoExponencial(valorMenor, media))
    if metodoJson[metodo] == 'natural':
        for _ in range(qtde):
            numerosAleatorios.append(
                gerarRandomicoNatural(media, variancia))
    return numerosAleatorios
