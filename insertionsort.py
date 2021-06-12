import time
trocas = 0
comp = 0


def insertionsort(dados, key=lambda x: x):
    global trocas, comp
    i = 0
    while i < len(dados) - 1:
        davez = dados[i + 1]
        j = i
        comp += 1
        while j >= 0 and key(dados[j]) > key(davez):
            comp += 1
            trocas += 1
            dados[j], dados[j + 1] = dados[j + 1], dados[j]
            j -= 1
        else:
            comp += 1
        i += 1


def metricas(dados, key=lambda x: x):
    global trocas, comp
    trocas = 0
    comp = 0
    inicio = time.time()
    insertionsort(dados, key)
    fim = time.time()
    return trocas, comp, fim - inicio
