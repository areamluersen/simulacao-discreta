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

# Slide professor.
def gerarRandomicoTriangular(valorMenor=0, valorMaior=1, moda= 0.5):
    U = random.random()
    if (U < (moda-valorMenor)/(valorMaior-valorMenor)):
        return valorMenor + (U*(moda-valorMenor)*(valorMaior-valorMenor)) ** 0.5
    else: 
        return valorMaior - ((1-U)*(valorMaior-moda)*(valorMaior-valorMenor)) ** 0.5
        


def gerarRandomicoEsponencial(valorMenor=0, valorMaior=1):
    return 1


def gerarRandomicoNatural(valorMenor=0, valorMaior=1):
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
    if metodoJson[metodo] == 'esponencial':
        for _ in range(qtde):
            numerosAleatorios.append(
                gerarRandomicoEsponencial(valorMenor, valorMaior))
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
