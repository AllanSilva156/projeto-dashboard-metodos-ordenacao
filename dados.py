import os
import insertionsort
import mergesort
import quicksort
import pandas as pd

# ==================  Para obter/atualizar os dados de exemplo é necessário executar este programa  ==================

# Dicionário das características de desempenho
METRICAS = {
    'trocas': 0,
    'comp': 1,
    'tempo': 2}

# Tamanhos padronizados dos arquivos a serem gerados
tamanho_arquivos = [10, 50, 100, 250, 500, 750, 1000]


# Função responsável por aplicar os métodos de ordenação em cada arquivo
def ordenaDados(caractericas, arquivo):
    dados = {'Tamanho': tamanho_arquivos,
             'insert': [], 'merge': [], 'quick': []}

    for i, tam_arq in enumerate(tamanho_arquivos):
        with open('{}{}.dat'.format(arquivo, i + 1)) as file:
            registros = [registro.strip().split(' ')
                         for registro in file.readlines()[1:]]

            insert = insertionsort.metricas(
                registros[:], key=lambda registro: registro[2])
            merge = mergesort.metricas(
                registros[:], key=lambda registro: registro[2])
            quick = quicksort.metricas(
                registros[:], key=lambda registro: registro[2])

            index = METRICAS[caractericas]

            dados['insert'].append(insert[index])
            dados['merge'].append(merge[index])
            dados['quick'].append(quick[index])

    dataframe = pd.DataFrame(dados)

    return dataframe


# Função responsável por criar os arquivos
def criar_dat():
    for arquivo in ['desordenado', 'ordenado', 'semiordenado']:
        for tam_arq in tamanho_arquivos:
            cmd = 'py {}.py {}'.format(arquivo, tam_arq)
            os.system(cmd)


# Função responsável por deletar arquivos preexistentes
def excluir_dat(n=len(tamanho_arquivos)):
    for arquivo in ['desordenado', 'ordenado', 'semiordenado']:
        for i in range(n):
            cmd = 'del {}{}.dat'.format(arquivo, i + 1)
            os.system(cmd)


if __name__ == '__main__':
    excluir_dat()
    criar_dat()
