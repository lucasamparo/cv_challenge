########################################################################
# Projeto           : Desafio Senai: Estrelas orbitando um buraco negro
#
# Nome do programa  : desafio.py
#
# Autor             : Diogo Lima Marques
#
# Data de criacao   : 02-09-2019
#
# Funcionamento     : Le arquivos de texto contidos numa pasta 'Input', contendo dados de posicoes de pontos referentes a coordenadas
#                     de estrelas ao longo do tempo, e calcula o ponto central da orbita de ambas as estrelas, assumindo que ambas as
#                     orbitas sao circulos concentricos, devido a influencia do buraco negro.
#
# Hist. de Revisao  :
#
# Data        Author      Ref    Revisao
# 03-09-2019  diogo       1      Codigo finalizado e submetido para avaliacao.
#
########################################################################

import sys
import os
import numpy as np

########################################################################
# inicio(): Funcao basica que le os arquivos de entrada, prepara o 
#           diretorio de saida e chama as funcoes de processamento.
#
#           Retorno: Nenhum.
########################################################################
def inicio():

    diretorio = os.path.abspath('.')+"/input/" #Pega os valores de entrada
    diretorioSaida = os.path.abspath('.')+"/output/"
    nomes_arq = os.listdir(diretorio)
    if not (os.path.isdir(diretorioSaida)):
        os.mkdir(diretorioSaida) #cria diretorio de saida se ele nao existir

    for file in nomes_arq:
        output = open(diretorioSaida + file, 'w')

        with open(diretorio+file) as arq:
            linhas = arq.readlines()
            numLinha = 1
            entradasEsperadas = 0
            listaCoordenadas = []
            coordenadas = []

            for linha in linhas:
                linha = linha.replace("\n", "")
                if(numLinha == 1): #Numero de testes
                    entradasEsperadas = float(linha)
                    numLinha = numLinha + 1
                elif(numLinha == 2): #Coordenadas do ponto A no primeiro instante de tempo
                    valores = encontraValores(linha)
                    coordenadas = []
                    coordenadas.append(valores)
                    numLinha = numLinha + 1
                elif(numLinha == 3): #Coordenadas do ponto B no primeiro instante de tempo
                    valores = encontraValores(linha)
                    coordenadas.append(valores)
                    numLinha = numLinha + 1
                elif(numLinha == 4): #Coordenadas do ponto A no segundo instante de tempo
                    valores = encontraValores(linha)
                    coordenadas.append(valores)
                    numLinha = numLinha + 1
                elif(numLinha == 5): #Coordenadas do ponto B no segundo instante de tempo
                    valores = encontraValores(linha)
                    coordenadas.append(valores)
                    numLinha = 2
                    
                    listaCoordenadas.append(coordenadas)
                    entradasEsperadas = entradasEsperadas - 1

                if(entradasEsperadas < 0):
                    print("Numero de entradas informado incorretamente.")

        caso = 0
        for coordenada in listaCoordenadas: #Para cada conjunto de 4 pontos, executar a logica para encontrar a posicao do buraco negro!
            A1 = coordenada[0]
            B1 = coordenada[1]
            A2 = coordenada[2]
            B2 = coordenada[3]
            caso = caso + 1
            
            vetorDeslocamento = calculaVetor(A1, A2, B1, B2) #Achar o vetor que define o deslocamento entre os dois pontos de cada estrela no tempo
            pontoMedio = calculaPontoMedio(A1, A2, B1, B2) #Determina o ponto medio da corda que liga os dois pontos

            vetorPerpendicular = perpendicularizaVetor(vetorDeslocamento) #Encontra o vetor perpendicular ao vetor de deslocamento, que cruza o centro da circunferencia

            retas = calculaReta(pontoMedio[0], pontoMedio[1], vetorPerpendicular) #Encontra as equacoes das retas para ambas as estrelas
 
            intersecao = calculaIntersecao(retas) #Encontra a intersecao entre as duas retas, que demarca o centro das orbitas concentricas!

            X1 = "{0:.2f}".format(intersecao[0])
            Y1 = "{0:.2f}".format(intersecao[1])

            print("Caso #"+str(caso)+": "+str(X1)+" "+str(Y1))
            output.write("Caso #"+str(caso)+": "+str(X1)+" "+str(Y1)+"\n")
        output.close()

########################################################################
# encontraValores(): Obtem os valores do arquivo de texto, eliminando
#                    espacos desnecessarios.
#
#                    Retorno: Vetor de 2 posicoes com os valores
#                             encontrados (float).
########################################################################

def encontraValores(linha): #encontra os valores na linha
    linha = linha.replace(" ", "")
    linha = linha.replace(" ", "")
    retorno = []

    posicaoPonto1 = linha.find(".", 0, len(linha))
    posicaoPonto2 = linha.find(".", posicaoPonto1+1, len(linha))

    valor1 = linha[0:posicaoPonto1+3]
    valor2 = linha[posicaoPonto1+3:posicaoPonto2+3]

    retorno.append(float(valor1))
    retorno.append(float(valor2))

    return retorno

########################################################################
# calculaVetor(): Calcula o vetor que ilustra o deslocamento entre
#                 dois pontos no tempo.
#
#                 Retorno: Conjunto de dois vetores, um para cada estrela.
########################################################################

def calculaVetor(A1, A2, B1, B2): #recebe as coordenadas e retorna um vetor de duas posicoes, contendo dois vetores de deslocamento
    vetA = []
    vetB = []
    vetRet = []

    vetA.append(A2[0]-A1[0])
    vetA.append(A2[1]-A1[1])



    vetB.append(B2[0]-B1[0])
    vetB.append(B2[1]-B1[1])



    vetRet.append(vetA)
    vetRet.append(vetB)


    return vetRet

########################################################################
# calculaPontoMedio(): Calcula o ponto que se localiza no centro da
#                      corda criada entre os dois pontos.
#
#                      Retorno: Um vetor contendo 2 conjuntos de pontos
#                               (X, Y), um para cada estrela.
########################################################################

def calculaPontoMedio(A1, A2, B1, B2): #recebe as coordenadas e calcula o ponto medio da reta que as liga
    vetRet = []
    A3 = []
    B3 = []

    A3.append((float(A1[0])+float(A2[0]))/2)
    B3.append((B1[0]+B2[0])/2)
    A3.append((A1[1]+A2[1])/2)
    B3.append((B1[1]+B2[1])/2)

    vetRet.append(A3)
    vetRet.append(B3)

    return vetRet

########################################################################
# perpendicularizaVetor(): Recebe um vetor e devolve um vetor perpendicular
#                          ao mesmo.
#
#                          Retorno: Conjunto de dois vetores perpendiculares,
#                                   um para cada estrela.
########################################################################

def perpendicularizaVetor(vetDesl): #recebe um vetor de deslocamento e retorna o vetor de mesmos valores, porem perpendicular ao mesmo
    vetA = vetDesl[0]
    vetB = vetDesl[1]
    vetRet = []
    aux = 0

    aux = vetA[0]
    vetA[0] = vetA[1]*(-1)
    vetA[1] = aux

    aux = vetB[0]
    vetB[0] = vetB[1]*(-1)
    vetB[1] = aux

    vetRet.append(vetA)
    vetRet.append(vetB)

    return vetRet

########################################################################
# calculaReta(): Recebe um ponto de partida (meio da corda) e um vetor
#                que indica a taxa de crescimento da reta, e calcula a
#                equacao da reta no formato 'y=Ax+B'. Tal reta possui a
#                garantia que um de seus pontos se localiza no centro
#                da orbita, para ambas as estrelas.
#
#                Retorno: Conjunto de dois vetores contendo os indices A
#                         e B. Em caso da reta ser completamente vertical
#                         retorna apenas um indice.
########################################################################

def calculaReta(A3, B3, vetPerp): #calcula a equacao geral da reta para ambos os vetores
    vetA = vetPerp[0]
    vetB = vetPerp[1]
    vetRet = []
    x = []
    y = []

    x.append(A3[0])
    x.append(A3[0]+vetA[0])

    y.append(A3[1])
    y.append(A3[1]+vetA[1])

    if not(x[0] == x[1]):
        coeficientes = np.polyfit(x, y, 1)
    else:
        coeficientes = [x[0]]

    vetRet.append(coeficientes)
    x = []
    y = []

    x.append(B3[0])
    x.append(B3[0]+vetB[0])

    y.append(B3[1])
    y.append(B3[1]+vetB[1])

    coeficientes = np.polyfit(x, y, 1)

    vetRet.append(coeficientes)

    vetRet.append(vetA)
    vetRet.append(vetB)

    return vetRet

########################################################################
# calculaIntersecao(): Recebe as duas retas e assume a igualdade dos pontos
#                      para encontrar a intersecao entre as duas. A unica
#                      intersecao valida e o centro de ambas as orbitas, 
#                      isto e, a posicao do buraco negro!
#
#                      Retorno: Retorna os pontos de localizacao do buraco
#                               negro.
########################################################################

def calculaIntersecao(retas): #calcula a intersecao entre duas retas
    retaA = retas[0]
    retaB = retas[1]
    intersecao = []


    if(len(retaA) > 1 and len(retaB) > 1):


        intersecaoX = (retaB[1]-retaA[1])/(retaA[0]-retaB[0])
        intersecaoY = (intersecaoX*retaA[0])+retaA[1]

    
    elif(len(retaA) == 1):
        intersecaoX = retaA[0]
        intersecaoY = retaA[0]*retaB[0]+retaB[1]

    elif(len(retaB) == 1):
        intersecaoX = retaB[0]
        intersecaoY = retaB[0]*retaA[0]+retaA[1]

    intersecao.append(intersecaoX)
    intersecao.append(intersecaoY)

    return intersecao


############ Iniciar Programa! ############

inicio()
