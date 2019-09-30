from numeros_aleatorios.numeros_randomicos import gerarRandomicoUniforme

def gerar_tempos_de_distribuicao(aleatorio=True, tempo_total_min=540, distribuicao=[]):
    tempo_acumulado = 0
    tempo_chegadas=[]
    while(tempo_acumulado <= tempo_total_min):
        aleatorio = gerarRandomicoUniforme(0,100)
        for k, v in distribuicao.items():
	        if (aleatorio < k):
                  tempo_acumulado += v
                  tempo_chegadas.append(v)
                  break
    return tempo_chegadas


distribuicao_chegadas = { 25: 12, 50: 13, 77: 14, 100: 15 }
distribuicao_atendimentos = { 30: 11, 70: 14, 85: 15, 100: 16 }
tempo_chegadas = gerar_tempos_de_distribuicao(True, 800, distribuicao_chegadas)
tempo_atendimentos = gerar_tempos_de_distribuicao(True, 800, distribuicao_atendimentos)

relogio_chegada = 0
relogio_atendimento = 0
for i in range(min(len(tempo_chegadas), len(tempo_atendimentos))):
    relogio_chegada += tempo_chegadas[i]
    relogio_atendimento += tempo_atendimentos[i]
    print('Chegada no min: ', relogio_chegada)
    print('atendimento no min: ', relogio_atendimento)

