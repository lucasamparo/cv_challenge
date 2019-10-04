# Resposta do desafio do buraco negro 
# Autor: Ivalbert Pereira

import numpy as np


# retorna um vetor com um dado tamanho e valor
def inicia_vetor (tam, valor):
  vet = [valor for i in range(tam)]
  return(vet)

# monta a matriz, resolve o sistema linear e retorna as coordenadas do centro da circunferência
def resolve(x1,y1,x2,y2,x3,y3,x4,y4):
  c1 = [float(x2 - x1), float(x4 - x3)]
  c2 = [float(y2 - y1), float(y4 - y3)]
  c3 = [float((x2**2 - x1**2 + y2**2 - y1**2)/2.00), float((x4**2 - x3**2 + y4**2 - y3**2)/2.00)]
  A = np.array([c1,c2]).transpose()
  B = c3
  try:
    resposta = np.linalg.solve(A,B)
    resposta[0] = float(resposta[0])
    resposta[1] = float(resposta[1])
  except Exception as ex:
    print(ex)
  finally:
    return resposta

# retorna o valor informado da variável dados os limites
def input_variavel(mensagem, limites, abortar):
  variavel = limites[0] -1
  while variavel == limites[0] -1:
    tmp = input(mensagem + "[cancelar = " + abortar + "]")
    try:
      variavel = int(tmp)
      if variavel < limites[0] or variavel > limites[1]:
        variavel = limites[0] -1
        print("Valor fora dos limites!")
    except Exception as ex:
      if tmp == abortar:
        return(-2)
      else:
        print(ex)
  else:
    return(variavel)

# retorna o valor informado da variável dados os limites
def input_vetor(tamanho, mensagem, limites, abortar):
  variavel = inicia_vetor(tamanho,(limites[0] -1))
  while (limites[0] -1) in variavel:
    tmp = input(mensagem + "[cancelar = " + abortar + "]")
    tmp = tmp.replace("\t", ",")
    try:
      variavel = [float(i) for i in eval("[" + tmp + "]")]
      #print(tmp)
      #for i in range(tamanho):
      #  variavel[i] = float(tmp[i])
      if any(variavel) < limites[0] or any(variavel) > limites[1]:
        variavel = limites[0] -1
        print("Valor fora dos limites!")
    except Exception as ex:
      if tmp == abortar:
        return(-2)
      else:
        print(ex)
  else:
    return(variavel)

#definindo limites e valores inciais
lim_estrelas = [-1000.00, 1000.00]
lim_casos = [1,10000.00]
casos = -1

#loop principal
while casos == -1:
  casos = input_variavel("Informe quantidade de casos: ", lim_casos, "c")
  if casos == -2:
    break
  else:
    centros = list()
    for i in range(casos):
      estrela = inicia_vetor(4,(lim_estrelas[0] -1))
      print("\n Informe as coordenada separada por vírgula(CASO #"+str(i+1)+"): x,y \n")
      c_e1_ini = input_vetor(2,"INICIAL ESTRELA 1: ", lim_estrelas, "c")
      c_e2_ini = input_vetor(2,"INICIAL ESTRELA 2: ", lim_estrelas, "c")
      c_e1_fim = input_vetor(2,"FiNAL ESTRELA 1: ", lim_estrelas, "c")
      c_e2_fim = input_vetor(2,"FINAL ESTRELA 2: ", lim_estrelas, "c")
      if c_e1_ini == c_e1_fim or c_e2_ini == c_e2_fim:
        print("As coordenadas iniciais e finais de uma mesma estrela devem ser diferentes")
        print(c_e1_ini + c_e1_fim + c_e2_ini + c_e2_fim)
        next
      else:
        estrela = c_e1_ini + c_e1_fim + c_e2_ini + c_e2_fim
        try:
          centros.append(resolve(estrela[0],estrela[1],estrela[2],estrela[3],estrela[4],estrela[5],estrela[6],estrela[7]))
        except Exception as ex:
          print(ex)
#exibe resultado final
    for i in range(casos):
      print("Caso #" + str(i+1) + ": " + ' '.join(str('%.2f' % x) for x in centros[i]))
