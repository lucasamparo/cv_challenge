#Autor: Silas Dantas de Carvalho
#Descricao: solução para o problema de localizacao do Buraco Negro

import numpy as np
from numpy.linalg import solve


#Funcao que encontra as coordenadas do Buraco Negro mediante as coordenadas das estrelas
def findBlackHole(coord, case):
	#Define os elementos das matrizes de coeficientes
	x_1 = 2*coord[4] - 2*coord[0]
	y_1 = 2*coord[5] - 2*coord[1]
	b_1 = (-1)*(coord[0]**2-coord[4]**2+coord[1]**2-coord[5]**2)
	x_2 = 2*coord[6] - 2*coord[2]
	y_2 = 2*coord[7] - 2*coord[3]
	b_2 = (-1)*(coord[2]**2-coord[6]**2+coord[3]**2-coord[7]**2)

	#Define as matrizes de coeficientes
	mA = np.array([[x_1,y_1], [x_2,y_2]])
	mB = np.array([b_1,b_2])
	
	#Resolve o sistema linear de primeira ordem com numpy.linalg.solve
	result = solve(mA, mB)

	#imprime o resultado
	print("Caso #%s" % case," %.2f %.2f" % (result[0],result[1]))


#Abre arquivo com os casos de teste (inputs)
f = open('coordenadas.cor', 'r')

#Inicia variaveis auxiliares
currentLine=0 # linha atual do arquivo (par de coordenadas)
currentCase=1 # Caso de teste Atual
testCases=0 # Numero de casos de teste
index=0 # index de cada caso de teste no vetor de coordenadas
coord=np.zeros(8) # vetor de coordenadas ([x_11, y_11, x_21, y_21, x_12, y_12, x_22, y_22])

#Lê arquivo linha a linha e processa os casos de teste
for line in f:
	valores = line.split()
	if currentLine==0:
		testCases = int(valores[0]) * 4
		currentLine = currentLine + 1
	else:
		currentLine = currentLine + 1
		if currentLine <= testCases+1:
			coord[index] = valores[0]
			coord[index+1] = valores[1]
			if index <= 4:
				index = index + 2
			else:
				findBlackHole(coord, currentCase)
				currentCase = currentCase + 1
				index = 0
		else:
			break


#Fecha arquivo
f.close()