from numeros_aleatorios.numeros_randomicos import gerarRandomicoUniforme

def gerar_tempos_de_distribuicao(aleatorio=True, tempo_total_min=540, distribuicao=[]):
    tempo_acumulado = 0
    tempo_chegadas=[]
    while(tempo_acumulado <= tempo_total_min):
        aleatorio = gerarRandomicoUniforme(0,100)
        for k, v in distribuicao.items():
	        if (aleatorio < k):
                  tempo_acumulado += v
                  tempo_chegadas.append({'minuto_tempo': tempo_acumulado, 'intervalo': v})
                  break
    return tempo_chegadas


# distribuicao_chegadas = { 25: 12, 50: 13, 77: 14, 100: 15 }
# distribuicao_atendimentos = { 30: 11, 70: 14, 85: 15, 100: 16 }
# tempo_chegadas = gerar_tempos_de_distribuicao(True, 800, distribuicao_chegadas)
# tempo_atendimentos = gerar_tempos_de_distribuicao(True, 800, distribuicao_atendimentos)

# for i in range(min(len(tempo_chegadas), len(tempo_atendimentos))):
#     print('Chegada no min: ', tempo_chegadas[i]['minuto_tempo'])
#     print('atendimento no min: ', tempo_atendimentos[i]['minuto_tempo'])

