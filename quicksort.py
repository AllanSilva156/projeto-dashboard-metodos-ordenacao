import time
trocas = 0
comp = 0


def quicksort(dados, esq, dir, key=lambda x: x):
    global trocas, comp
    contesq, contdir, m = (esq, dir, (esq + dir)//2)
    pivo = dados[m]
    while contesq <= contdir:
        while key(dados[contesq]) < key(pivo) and contesq < dir:
            comp += 1
            contesq += 1
        while key(dados[contdir]) > key(pivo) and contdir > esq:
            comp += 1
            contdir -= 1
        if contesq <= contdir:
            dados[contdir], dados[contesq] = dados[contesq], dados[contdir]
            trocas += 1
            contdir -= 1
            contesq += 1

    if contesq < dir:
        quicksort(dados, contesq, dir)
    if contdir > esq:
        quicksort(dados, esq, contdir)


def metricas(dados, key=lambda x: x):
    global trocas, comp
    trocas = 0
    comp = 0

    inicio = time.time()
    quicksort(dados, 0, len(dados) - 1, key)
    fim = time.time()
    return trocas, comp, fim - inicio
