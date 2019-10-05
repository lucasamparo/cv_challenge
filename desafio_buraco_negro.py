
def mediatriz(ponto1, ponto2):
	x = (ponto1[0]+ponto2[0])/2
	y = (ponto1[1]+ponto2[1])/2
	return x, y

def coeficienteRetaBase(ponto1, ponto2):
	return (ponto2[1]-ponto1[1])/(ponto2[0]-ponto1[0])

def inversoDoOposto(coeficiente):
	inversoOposto = 0
	if coeficiente != 0:
		inversoOposto = 1/((-1)*coeficiente)
	return inversoOposto

def geraEquacaoDaReta(ponto, m):
	termo1 = str(m)+"x"
	termo2 = str((-ponto[0]*m)+ponto[1])
	print("y = "+termo1+" + "+termo2)

def encontroDeRetas(ponto1, coeficiente1, ponto2, coeficiente2):
	x = y = 0
	if coeficiente1 != 0 and coeficiente2 != 0:
		x = ((coeficiente1*ponto1[0]) - (coeficiente2*ponto2[0]) + ponto2[1] - ponto1[1])/(coeficiente1-coeficiente2)
		y = (coeficiente1*x) - (coeficiente1*ponto1[0]) + ponto1[1]
	elif coeficiente1 == 0:
		x = ponto1[0]
		y = (coeficiente2*x) - (coeficiente2*ponto2[0]) + ponto2[1]
	else:
		x = ponto2[0]
		y = (coeficiente1*x) - (coeficiente1*ponto1[0]) + ponto1[1]
	return x, y

def rotina(ponto1, ponto2, ponto3, ponto4):
	#-----------Primeiro Ponto-----------#
	m = coeficienteRetaBase(ponto1, ponto2)
	inversoOposto1 = inversoDoOposto(m)
	xm1, ym1 = mediatriz(ponto1, ponto2)
	#-----------Segundo Ponto------------#
	m = coeficienteRetaBase(ponto3, ponto4)
	inversoOposto2 = inversoDoOposto(m)
	xm2, ym2 = mediatriz(ponto3, ponto4)
	#----------Ponto do Encontro----------#
	xen, yen = encontroDeRetas([xm1, ym1], inversoOposto1, [xm2, ym2], inversoOposto2)

	return round(xen, 2), round(yen, 2) 

def verificacao(quantidade, tipo, escopo):
	if quantidade.isdigit():
		quantidade = int(quantidade)
		if type(quantidade) == tipo:
			if quantidade>=escopo[0] and quantidade<=escopo[1]:
				return True, 'Correto'
			else: 
				return False, 'Valor fora do Range de '+str(escopo[0])+' a '+str(escopo[1])
		else:
			return False, 'Valor não é do tipo '+str(tipo).replace("<class '","").replace("'>", "")
	else:
		return False, 'Valor não é do tipo '+str(tipo).replace("<class '","").replace("'>", "")

repeticoes = input('Informe a quantidade de casos de teste: ')
status, msg = verificacao(repeticoes, int, [1, 10000])
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = [] 
if status:
	repeticoes = int(repeticoes)
	for x in range(repeticoes):
		print("Dados do Caso "+str(x+1))
		coordenandas1 = input('Informe as coordenandas X e Y da primeira posicao da primeira estrela: ').split(" ")
		vetor1.append([float(coordenandas1[0]), float(coordenandas1[1])])
		coordenandas3 = input('Informe as coordenandas X e Y da primeira posicao da segunda estrela: ').split(" ")
		vetor3.append([float(coordenandas3[0]), float(coordenandas3[1])])
		coordenandas2 = input('Informe as coordenandas X e Y da segunda posicao da primeira estrela: ').split(" ")
		vetor2.append([float(coordenandas2[0]), float(coordenandas2[1])])
		coordenandas4 = input('Informe as coordenandas X e Y da segunda posicao da segunda estrela: ').split(" ")
		vetor4.append([float(coordenandas4[0]), float(coordenandas4[1])])

	for x in range(repeticoes):
		xc, yc = rotina(vetor1[x], vetor2[x], vetor3[x], vetor4[x])
		print("Caso #"+str(x+1)+": "+str(xc)+" "+str(yc))
else:
	print(msg)
