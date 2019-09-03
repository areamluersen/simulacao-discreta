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
def gerarRandomicoUniforme(valorMenor=0, valorMaior=1):
    return valorMenor + (valorMaior - valorMenor)*random.random()

# Slide professor.
def gerarRandomicoTriangular(valorMenor=0, valorMaior=1, moda= 0.5):
    U = random.random()
    if (U < (moda-valorMenor)/(valorMaior-valorMenor)):
        return valorMenor + (U*(moda-valorMenor)*(valorMaior-valorMenor)) ** 0.5
    else: 
        return valorMaior - ((1-U)*(valorMaior-moda)*(valorMaior-valorMenor)) ** 0.5
        

def gerarRandomicoExponencial(limiteInferior=0, media=5):
    # http://mpsantos.com.br/simul.pdf - Página 66 e 67
    U = random.random()
    alpha = 1 / (media - limiteInferior)  # todo decobrir valor verdadeiro
    x = limiteInferior - (1 / alpha) * math.log(U)
    return x


def gerarRandomicoNatural(valorMenor=0, valorMaior=1):
    # unica referencia nas primeiras pesquisas no google
    # https://math.stackexchange.com/questions/1079904/natural-number-generator
    return 2


def gerarNumerosRandomicos(qtde=10, metodo=1, valorMenor=0, valorMaior=1, moda=0.5):
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
                gerarRandomicoExponencial(valorMenor, valorMaior))
    if metodoJson[metodo] == 'natural':
        for _ in range(qtde):
            numerosAleatorios.append(
                gerarRandomicoNatural(valorMenor, valorMaior))
    return numerosAleatorios
    
numerosAleatorios = gerarNumerosRandomicos(50, 2, 1 , 100, 8)
acc = 0
for i in range(len(numerosAleatorios)):
    acc += numerosAleatorios[i]
    print('numero',i+1, ':', numerosAleatorios[i])
print ('Valor medio : ', acc/len(numerosAleatorios))
