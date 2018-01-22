# coding: utf-8
'''
É Quadrado Mágico?

Escreva uma função que receba uma matriz e verifica se ela representa um quadrado mágico retornando True ou False (booleano).
No quadrado mágico o resultado da soma dos elementos de suas linhas, suas colunas e diagonais tem o mesmo valor.
Além disso, não pode haver elementos repetidos no quadrado.
'''

def lista_de_elementos_iguais(lista):
	elemento = lista[0]
	for k in lista:
		if k != elemento:
			return False
	return True

def ha_repetidos(lista):
	l = []
	for i in lista:
		if i in l:
			return True
		else:
			l.append(i)
	return False

def eh_quadrado_magico(m):
	n_linhas = len(m)
	n_colunas = len(m[0])
	if n_linhas != n_colunas:
		return False
	else:
		somas_de_m = []                # Lista com a soma das linhas, das colunas e das diagonais
		elementos_de_m = []            # Lista com os elementos da matriz m

		''' 1° Condicao: Todos os números da matriz m distintos '''
		for j in range(n_colunas):
			for i in range(n_linhas):
				elementos_de_m.append(m[i][j])
		if ha_repetidos(elementos_de_m):
			return False

		''' 2° Condicao: Soma da diagonal secundaria constante'''
		aux = 0
		i = n_linhas - 1
		j = 0
		while True:
			aux += m[i][j]
			i -= 1
			j += 1
			if i < 0:
				break
		somas_de_m.append(aux)

		''' 3° Condicao: Soma da diagonal principal constante'''
		aux = 0
		i = 0
		j = 0
		while i < n_linhas:
			aux += m[i][j]
			i += 1
			j += 1
		somas_de_m.append(aux)

		''' 4° condicao: Soma dos elementos verticais constante '''
		for j in range(n_colunas):
			aux = 0
			for i in range(n_linhas):
				aux += m[i][j]
			somas_de_m.append(aux)

		''' 5° condicao: Soma dos elementos horizontais constante '''
		for i in range(n_linhas):
			aux = 0
			for j in range(n_colunas):
				aux += m[i][j]
			somas_de_m.append(aux)

		if lista_de_elementos_iguais(somas_de_m):
			return True
		return False


# ------------ TESTES -------------

quadrado1 = [[2,7,6],[9,5,1],[4,3,8]]
quadrado2 = [[1,2,3],[4,5,6]]
assert eh_quadrado_magico(quadrado1)
assert not eh_quadrado_magico(quadrado2)
