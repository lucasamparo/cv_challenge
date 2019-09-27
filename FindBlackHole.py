import numpy as np

class Constelacao:
    def __init__(self, x_estrela1Inicial, y_estrela1Inicial, x_estrela1Final, y_estrela1Final, x_estrela2Inicial, y_estrela2Inicial, x_estrela2Final, y_estrela2Final):
        self.x_estrela1Inicial = x_estrela1Inicial
        self.y_estrela1Inicial = y_estrela1Inicial
        self.x_estrela1Final = x_estrela1Final
        self.y_estrela1Final = y_estrela1Final
        self.x_estrela2Inicial = x_estrela2Inicial
        self.y_estrela2Inicial = y_estrela2Inicial
        self.x_estrela2Final = x_estrela2Final
        self.y_estrela2Final = y_estrela2Final
    
    def ObterPosicaoBuracoNegro(self):
        try:
            equacao1FirstMember = [2 * (x_estrela1Final - x_estrela1Inicial), 2 * (y_estrela1Final - y_estrela1Inicial)]
            equacao1SecondMemberValue = -1 * (x_estrela1Inicial**2 - x_estrela1Final**2 + y_estrela1Inicial**2 - y_estrela1Final**2)
            equacao2FirstMember = [2 * (x_estrela2Final - x_estrela2Inicial), 2 * (y_estrela2Final - y_estrela2Inicial)]
            equacao2SecondMemberValue = -1 * (x_estrela2Inicial**2 - x_estrela2Final**2 + y_estrela2Inicial**2 - y_estrela2Final**2)
            a = np.array([equacao1FirstMember, equacao2FirstMember])
            b = np.array([equacao1SecondMemberValue, equacao2SecondMemberValue])
            result = np.linalg.solve(a,b)
            return result
        except:
            return [0,0]


run = True

while(run):
    try:
        numberTests = int(input("Informe o número de testes de caso: "))
    except:
        print("Entrada inválida (O número de testes tem que está entre 1 e 10000)")
        continue
    if numberTests < 1 or numberTests > 10000:
        print("Entrada inválida (O número de testes tem que está entre 1 e 10000)")
        continue
    
    for i in range(numberTests):
        try:
            x_estrela1Inicial = float(input("Estrela 1 inicial valor de x: "))
        except:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        if x_estrela1Inicial < -1000.0:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        
        try:
            y_estrela1Inicial = float(input("Estrela 1 inicial valor de y: "))
        except:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        if y_estrela1Inicial > 1000.0:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        
        try:
            x_estrela1Final = float(input("Estrela 1 final valor de x: "))
        except:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        if x_estrela1Final < -1000.0:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        
        try:
            y_estrela1Final = float(input("Estrela 1 final valor de y: "))
        except:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        if y_estrela1Final > 1000.0:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        
        try:
            x_estrela2Inicial = float(input("Estrela 2 inicial valor de x: "))
        except:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        if x_estrela2Inicial < -1000.0:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        
        try:
            y_estrela2Inicial = float(input("Estrela 2 inicial valor de y: "))
        except:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        if y_estrela2Inicial > 1000.0:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        
        try:
            x_estrela2Final = float(input("Estrela 2 final valor de x: "))
        except:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        if x_estrela2Final < -1000.0:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        
        try:
            y_estrela2Final = float(input("Estrela 2 final valor de y: "))
        except:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        if y_estrela2Final > 1000.0:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        
        constelacao = Constelacao(x_estrela1Inicial, y_estrela1Inicial, x_estrela1Final, y_estrela1Final, x_estrela2Inicial, y_estrela2Inicial, x_estrela2Final, y_estrela2Final)

        result = constelacao.ObterPosicaoBuracoNegro()

        print("Caso#" + str(i+1) + ": " +  format(result[0], '.2f') + " " + format(result[1], '.2f'))

    run = False
    close = input("aperte em qualquer tecla para encerrar.")