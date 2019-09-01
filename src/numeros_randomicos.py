import random
# Criar métodos de geração de números aleatórios como Uniforme, triangular, esponencial e natural.
metodoJson = {
    1: "uniforme",
    2: "triangular",
    3: "esponencial",
    4: "natural"
}

# x = a + (b-a)*R   R = Random number - a={valor menor} b={valor maior}
def gerarRandomicoUniforme(valorMenor=0, valorMaior=1):
    return valorMenor + (valorMaior - valorMenor)*random.random()


def gerarRandomicoTriangular(valorMenor=0, valorMaior=1):
    return 0


def gerarRandomicoEsponencial(valorMenor=0, valorMaior=1):
    return 1


def gerarRandomicoNatural(valorMenor=0, valorMaior=1):
    return 2


def gerarNumerosRandomicos(qtde=10, metodo=1, valorMenor=0, valorMaior=1):
    numerosAleatorios = []
    if metodoJson[metodo] == 'uniforme':
        for _ in range(qtde):
            numerosAleatorios.append(
                gerarRandomicoUniforme(valorMenor, valorMaior))
    if metodoJson[metodo] == 'triangular':
        for _ in range(qtde):
            numerosAleatorios.append(
                gerarRandomicoTriangular(valorMenor, valorMaior))
    if metodoJson[metodo] == 'esponencial':
        for _ in range(qtde):
            numerosAleatorios.append(
                gerarRandomicoEsponencial(valorMenor, valorMaior))
    if metodoJson[metodo] == 'natural':
        for _ in range(qtde):
            numerosAleatorios.append(
                gerarRandomicoNatural(valorMenor, valorMaior))
    return numerosAleatorios
    
numerosAleatorios = gerarNumerosRandomicos(15, 1, 2 , 5)
for i in range(len(numerosAleatorios)):
    print('numero',i+1, ':', numerosAleatorios[i])
