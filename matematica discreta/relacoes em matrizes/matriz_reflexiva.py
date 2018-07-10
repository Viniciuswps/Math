#-*-coding: utf-8-*-

def eh_reflexiva(relacao):
    matriz = relacao.__matriz_relacao__().__get_array_matriz__()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j and matriz[i][j] != 1:
                return False
    return True