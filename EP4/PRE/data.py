'''
Programa que implementa as funcoes necessarias para o pre-processmento dos
dados brutos, necessario para leva-los a um estado adequado para
o treinamento pelo modelo definido em model.py.
'''
     
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sortedcontainers import SortedSet

def rolling_hash(a):
    """Ordena datas transformando DD/MM/AAAA em números base 10 da direita para a esquerda"""
    p = 10
    cur = 1
    val = 0
    n = len(a)
    for i in range(0, n):
        char_val = ord(a[n - 1 - i]) - ord('0')
        if char_val < 0 or char_val > 10:
            continue
        val = val + cur*char_val 
        cur = cur*p
    return val

def load_data(data_path):
    """Funcao que importa dados de um arquivo csv, usando pandas"""
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, data_path)
    raw_data = pd.read_csv(filename)
    return raw_data

def filter_inputs(dataframes):
    """"Funcao que gera arquivos com as entradas das colunas 'de_exame' e
    'de_analito'"""

    # Filtra a coluna 'de_exame'
    exames_bruto = SortedSet()
    for arquivo in dataframes:
        for exame in arquivo['de_exame']:
            exames_bruto.add(exame)
    with open('exames.txt', 'w') as arquivo:
        for exame in exames_bruto:
            arquivo.write(exame + "\n")

    # Filtra a coluna 'de_analito'
    exames_selecionados = SortedSet()
    with open('exames_selecionados.txt', 'r') as arquivo:
        for linha in arquivo:
            ultimo_char = len(linha) - 1
            exames_selecionados.add(linha if linha[ultimo_char] != '\n' else linha[:ultimo_char])

    analitos_bruto = SortedSet()
    for dataframe in dataframes:
        for i in range(0, len(dataframe)):
            if dataframe['de_exame'][i] in exames_selecionados:
                analitos_bruto.add(dataframe['de_analito'][i])
    with open('analitos.txt', 'w') as arquivo:
        for analito in analitos_bruto:
            arquivo.write(analito + "\n")

    analitos_selecionados = SortedSet()
    with open('analitos_selecionados.txt', 'r') as arquivo:
        for linha in arquivo:
            ultimo_char = len(linha) - 1
            analitos_selecionados.add(linha if linha[ultimo_char] != '\n' else linha[:ultimo_char])

    return exames_selecionados, analitos_selecionados

def build_dataframe():
    
    dataframes = []
    for arquivo in ['einstein_e.csv', 'fleury_e.csv', 'hsl_e.csv']:
        dataframes.append(load_data('../dados/' + arquivo))
    raw_data = pd.concat(dataframes, ignore_index=True)
    exames, analito = filter_inputs(dataframes)
    
    to_keep = []
    for i in range(0, len(raw_data)):
        if raw_data['de_exame'][i] in exames and raw_data['de_analito'][i] in analito:
            to_keep.append(i)

    raw_data = raw_data.loc[to_keep]
    raw_data = raw_data.reset_index(drop=True)

    return raw_data

def pre_processing(raw_data):
    """Funcao que filtra e limpa os dados medicos para o treinamento"""

    # Seleciona as variaveis que serao usadas como features:
    raw_data['exame'] = raw_data[['de_exame', 'de_analito']].apply(lambda x: ' - '.join(x), axis=1)
    cols = ['id_paciente', 'dt_coleta', 'exame', 'de_resultado', 'de_valor_referencia']
    processed_data = raw_data[cols]

    exames = SortedSet()
    for exame in processed_data['exame']:
        exames.add(exame if exame[-1] != '\n' else exame[:-1])    
    with open('exames_geral.txt', 'w') as arquivo:
        for exame in exames:
            arquivo.write(exame + "\n")

    ids = [str(id) for id in processed_data['id_paciente']]
    pairs = list(zip(ids, list(processed_data['dt_coleta'])))
    pairs.sort(key=lambda x: x[0])
    pairs.sort(key=lambda x: rolling_hash(x[1]))

    cols = ['id_paciente', 'dt_coleta']
    cols.extend(exames)
    final_data = pd.DataFrame(columns=cols)

    final_data_list = []
    size = len(processed_data)
    for id, dt in pairs:
        row = {'id_paciente' : id, 'dt_coleta': dt}
        for i in range(0, size):
            if id.rstrip("\n") == str(processed_data['id_paciente'][i]).rstrip("\n") and dt == processed_data['dt_coleta'][i]:
                row[processed_data['exame'][i]] = processed_data['de_resultado'][i]
        final_data_list.append(row)

    final_data = pd.DataFrame(final_data_list)
    final_data.to_csv('final_data.csv')

    # Remove todas as entradas dos dados que nao possuem
    # todas as features  instanciadas:
    processed_data = processed_data.dropna(how='any')
    return processed_data

def main():
    raw_data = load_data()
    processed_data = pre_processing(raw_data)
    visualize_data(processed_data)

if __name__ == "__main__":
    pre_processing(build_dataframe())
