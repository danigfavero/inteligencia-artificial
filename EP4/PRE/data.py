'''
Programa que implementa as funcoes necessarias para o pre-processmento dos
dados brutos, necessario para leva-los a um estado adequado para
o treinamento pelo modelo definido em model.py.
'''

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(data_path):
    """Funcao que importa dados de um arquivo csv, usando pandas"""
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, data_path)
    raw_data = pd.read_csv(filename)
    return raw_data

def filter_inputs():
    """"Funcao que gera arquivos com as entradas das colunas 'de_exame' e
    'de_analito'"""

    # Filtra a coluna 'de_exame'
    dataframes = []
    for arquivo in ['einstein_e.csv', 'fleury_e.csv', 'hsl_e.csv']:
        dataframes.append(load_data('../dados/' + arquivo))
    exames_bruto = set()
    for arquivo in dataframes:
        for exame in arquivo['de_exame']:
            exames_bruto.add(exame)
    with open('exames.txt', 'w') as arquivo:
        for exame in exames_bruto:
            arquivo.write(exame + "\n")

    # Filtra a coluna 'de_analito'
    exames_selecionados = set()
    with open('exames_selecionados.txt', 'r') as arquivo:
        for linha in arquivo:
            ultimo_char = len(linha) - 1
            exames_selecionados.add(linha if linha[ultimo_char] != '\n' else linha[:ultimo_char])

    analitos_bruto = set()
    for dataframe in dataframes:
        for i in range(0, len(dataframe)):
            if dataframe['de_exame'][i] in exames_selecionados:
                analitos_bruto.add(dataframe['de_analito'][i])
    with open('analitos.txt', 'w') as arquivo:
        for analito in analitos_bruto:
            arquivo.write(analito + "\n")

def pre_processing(raw_data):
    """Funcao que filtra e limpa os dados meteorologicos para o treinamento"""

    # Seleciona as variaveis que serao usadas como features:
    cols = ['Rainfall', 'Humidity3pm', 'Pressure9am',
            'RainToday', 'RainTomorrow']
    processed_data = raw_data[cols]

    # Adequa o formato das variaveis RainToday e RainTomorrow:
    processed_data['RainToday'].replace({'No': 0, 'Yes': 1}, inplace=True)
    processed_data['RainTomorrow'].replace({'No': 0, 'Yes': 1}, inplace=True)

    # Remove todas as entradas dos dados que nao possuem
    # todas as features  instanciadas:
    processed_data = processed_data.dropna(how='any')
    return processed_data


def visualize_data(data):
    """Gera graficos das distribuicoes das features e salva em disco"""

    ibm_pltt = ['#648FFF', '#785EF0', '#DC267F',
                '#FE6100', '#FFB000']  # Paleta colorblind-friendly
    plt.figure(figsize=(8, 6))

    # RainToday:
    sns.set()
    sns.set_palette(sns.color_palette([ibm_pltt[2], ibm_pltt[0]]))
    sns.countplot(data.RainToday)
    plt.xlabel('Choveu Hoje?')
    plt.ylabel('Contagem')
    plt.title("Valores de 'RainToday' para os dados pré-processados")
    plt.savefig('data_RainToday.png')
    plt.clf()

    # RainTomorrow:
    sns.set()
    sns.set_palette(sns.color_palette([ibm_pltt[3], ibm_pltt[1]]))
    sns.countplot(data.RainTomorrow)
    plt.xlabel('Choverá Amanhã?')
    plt.ylabel('Contagem')
    plt.title("Valores de 'RainTomorrow' para os dados pré-processados")
    plt.savefig('data_Rainomorrow.png')
    plt.clf()

    # Humidity3pm:
    sns.set()
    sns.distplot(data.Humidity3pm, color=ibm_pltt[0])
    plt.xlabel('Umidade às 3PM')
    plt.ylabel('Densidade normalizada')
    plt.title("Distribuição da variável 'Humidity3pm' para os dados pré-processados")
    plt.savefig('data_Humidity3pm.png')
    plt.clf()

    # Pressure9am:
    sns.set()
    sns.distplot(data.Pressure9am, color=ibm_pltt[4])
    plt.xlabel('Pressão atmosférica às 9AM')
    plt.ylabel('Densidade normalizada')
    plt.title("Distribuição da variável 'Pressure9amm' para os dados pré-processados")
    plt.savefig('data_Pressure9am.png')
    plt.clf()

    # Rainfall:
    sns.set()
    sns.distplot(data.Rainfall, color=ibm_pltt[1], bins=500, kde=False)
    plt.xlim(0, 10)
    plt.xlabel('Pluviosidade')
    plt.ylabel('Densidade normalizada')
    plt.title("Distribuição da variável 'Rainfall' para os dados pré-processados")
    plt.savefig('data_Rainfall.png')
    plt.clf()

    return


def main():
    raw_data = load_data()
    processed_data = pre_processing(raw_data)
    visualize_data(processed_data)


if __name__ == "__main__":
    filter_inputs()
