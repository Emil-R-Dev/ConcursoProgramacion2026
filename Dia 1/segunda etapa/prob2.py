

def genmatrizA():
    
    matrizA=[]
    with open ("Dia 1/segunda etapa/matrizA.txt","r") as archivo:

        for line in archivo:
            fila=[]
        
            for c in line:
                try:
                    fila.append(int(c))
                    
                except:
                    continue
            matrizA.append(fila)


    return matrizA

def genmatrizB():
    
    matrizB=[]
    with open ("Dia 1/segunda etapa/matrizB.txt","r") as archivo:

        for line in archivo:
            fila=[]
        
            for c in line:
                try:
                    fila.append(int(c))
                    
                except:
                    continue
            matrizB.append(fila)


    return matrizB

def sumar(matrizA, matrizB):

    matrizC=[]
    for filaA, filaB in zip(matrizA,matrizB):
        fila=[]
        for a, b in zip(filaA,filaB):
            fila.append(a+b)
        matrizC.append(fila)
    return matrizC



def main():

    matrizA=genmatrizA()
    matrizB=genmatrizB()
    matrizC=(sumar(matrizA,matrizB))
    print(matrizC)  
    with open("Dia 1/segunda etapa/matrizC.txt", "w") as c:

        for fila in matrizC:
            for numero in fila:
                c.write(f"{numero} ")
            c.write("\n")
        
    
        


main()