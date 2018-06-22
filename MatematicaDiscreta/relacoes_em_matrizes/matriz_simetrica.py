#-*-coding: utf-8-*-

def eh_simetrica(relacao):
    matriz = relacao.__matriz_relacao__().__get_array_matriz__()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True