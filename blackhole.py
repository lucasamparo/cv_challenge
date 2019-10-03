
class Astro:
    def __init__(self, xf1, yf1, xf2, yf2, xe1, ye1, xe2, ye2):
        self.xf1 = xf1
        self.yf1 = yf1
        self.xf2 = xf2
        self.yf2 = yf2
        self.xe1 = xe1
        self.ye1 = ye1
        self.xe2 = xe2
        self.ye2 = ye2
    
    def BlackHolePosition(self):
        try:
            equacaoCircunferenciaL = (xe2**2 - xe1**2 + ye2**2 - ye1**2)/2(xe2 - xe1)
            equacaoCircunferenciaP =  (xf1**2 - xf2**2 + yf1**2 - yf2**2)
            Xn = ((equacaoCircunferenciaL*(xf1 - xf2) - equacaoCircunferenciaP / 2) / (yf2 -yf1) + ((ye1-ye2)*(xf2-xf1)/(xe2 - xe1))	* ((ye1-ye2)/(xe2-xe1))) + equacaoCircunferenciaL
            Yn = (equacaoCircunferenciaL * (xf1 - xf2) - equacaoCircunferenciaP /2)/(yf2-yf1 + ((ye1-ye2)*(xf2-xf1)/(xe2-xe1)))

            result = [Xn, Yn]
            return result
        except:
            return []


a = True

while(a):
    try:
        numberTests = int(input("Informe o número válido: "))
    except:
        print("input invalid")
        continue
    if numberTests < 1 or numberTests > 10000:
        print("input invalid")
        continue
    
    for i in range(numberTests):
        try:
            xf1 = float(input("Estrela F1 valor de x: "))
        except:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        if xf1 < -1000.0:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        
        try:
            yf1 = float(input("Estrela F1 valor de y: "))
        except:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        if yf1 > 1000.0:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        
        try:
            xf2 = float(input("Estrela F2 valor de x: "))
        except:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        if xf2 < -1000.0:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        
        try:
            yf2 = float(input("Estrela F2 valor de y: "))
        except:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        if yf2 > 1000.0:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        
        try:
            xe1 = float(input("Estrela E1 valor de x: "))
        except:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        if xe1 < -1000.0:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        
        try:
            ye1 = float(input("Estrela E1 valor de y: "))
        except:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        if ye1 > 1000.0:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        
        try:
            xe2 = float(input("Estrela E2 valor de x: "))
        except:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        if xe2 < -1000.0:
            print("Entrada inválida (O valor de x deve ser maior ou igual a -1000.0)")
            continue
        
        try:
            ye2 = float(input("Estrela E2 valor de y: "))
        except:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        if ye2 > 1000.0:
            print("Entrada inválida (O valor de y deve ser menor ou igual a 1000.0)")
            continue
        
        astro = Astro(xf1, yf1, xf2, yf2, xe1, ye1, xe2, ye2)

        result = astro.BlackHolePosition()

         print("Caso#" + str(i+1) + ": " +  format(result[0], '.2f') + " " + format(result[1], '.2f'))

    a = False
    close = input("press any key to finish")