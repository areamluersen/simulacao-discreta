# 1- Criar array de chegadas (aleatório ou deterministico) com Tempo total definido pelo usuário em minutos.
# 2- Criar Array de tempos de atendimento (aleatório ou deterministico). 
# 3- Definir se tamanho das filas terão limites (excluir unidades que chagarem e estrapolarem tamanho da fila).
# 4- while tempo_minutos > i i++ - loop
# 5- Dentro do while i vale como minutos - 
# 6- Ir adicionando as chegadas e realizando os atendimentos, armazenando valores das variáveis de interesse.

# Variáveis : (status_servidor(liberado, em_uso)) fila. cliente
import gerador_aleatorios

#  cliente = [{'minutoChegada': 5, 'tempo_': 'não'}, {}]

def main():
    # Variáveis que devem ser lidas do usuário
    tempo_simulacao_min = 540 #Equivalente a 8 horas
    distribuicao_chegadas = { 25: 12, 50: 13, 77: 14, 100: 15 }
    distribuicao_atendimentos = { 30: 11, 70: 14, 85: 15, 100: 16 }
    tempo_chegadas = gerador_aleatorios.gerar_tempos_de_distribuicao(True, tempo_simulacao_min, distribuicao_chegadas)
    tempo_atendimentos = gerador_aleatorios.gerar_tempos_de_distribuicao(True, tempo_simulacao_min, distribuicao_atendimentos)
    # Variáveis que devem ser lidas do usuário

    #variáveis discretas
    servidor_ocupado = False
    atendimentos_realizados_cont = 0
    atendimentos_realizados_inf = []
    fila = []
    posicao_lista_chegada = 0
    servidor_ficara_livre_no_min=0
    #variáveis discretas

    for i in range(tempo_simulacao_min):
        if (servidor_ocupado and servidor_ficara_livre_no_min == i+1):
           servidor_ocupado = False
           atendimentos_realizados_cont += 1
           print('\n---------------------------------------------- ')
           print('Servidor Ficou Livre no Min: ',i+1)
        
        if (servidor_ocupado == False and len(fila) > 0):
          servidor_ocupado = True
          servidor_ficara_livre_no_min = tempo_atendimentos[fila[0]['posicao_fila_chegada']]['intervalo'] + i+1
          fila.pop(0)

        if (tempo_chegadas[posicao_lista_chegada]['minuto_tempo'] == i+1):
          if (servidor_ocupado == False):
            servidor_ocupado = True
            servidor_ficara_livre_no_min = tempo_atendimentos[posicao_lista_chegada]['intervalo'] + i+1
            print('\n---------------------------------------------- ')
            print('Servidor Comecou atendimento no min: ', i+1)
            print('Tempo previsto de atendimento: ', tempo_atendimentos[posicao_lista_chegada]['intervalo'])
            print('Minuto previsto em que ficará livre: ',servidor_ficara_livre_no_min)
            print('\n---------------------------------------------- ')
            posicao_lista_chegada += 1
          else:
            fila.append({'minuto_chegada': i, 'posicao_fila_chegada': posicao_lista_chegada })
            tempo_chegadas[posicao_lista_chegada]['pegou_fila'] = True
            posicao_lista_chegada += 1

          


if __name__ == '__main__':
    main()
