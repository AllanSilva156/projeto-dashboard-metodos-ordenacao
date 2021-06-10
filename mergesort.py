import time
trocas = 0
comp = 0

def mergesort(dados, esq, dir, key=lambda x: x):
    if esq >= dir:
        return
    m = (esq + dir)//2
    mergesort(dados, m+1,dir, key=lambda x: x)
    mergesort(dados, esq, m, key=lambda x: x)
    merge(dados, esq, m, dir, key=lambda x: x)

def merge(dados, esq, m, dir, key=lambda x: x):
    global trocas, comp
    copia = dados[:]
    contdir = m + 1
    contesq = esq

    cont = esq
    while contdir <= dir and contesq <= m:
        if key(copia[contdir]) <= key(copia[contesq]):
            comp += 1
            trocas += 1
            dados[cont] = copia[contdir]
            contdir += 1
        else:
            comp += 1
            trocas += 1
            dados[cont] = copia[contesq]
            contesq += 1

        cont += 1

    while contdir <= dir:
        trocas += 1
        dados[cont] = copia[contdir]
        contdir += 1
        cont += 1
    while contesq <= m:
        trocas += 1
        dados[cont] = copia[contesq]
        contesq += 1
        cont += 1
    
def metricas(dados, key=lambda x: x):
    global trocas, comp
    trocas = 0
    comp = 0
    inicio = time.time()
    mergesort(dados, 0, len(dados)-1, key)
    fim = time.time()
    return trocas, comp, fim - inicio
    
    
