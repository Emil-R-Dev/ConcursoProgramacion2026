

def genmatrizA():
    
    matrizA=[]
    with open ("matrizA.txt","r") as archivo:

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
    with open ("matrizB.txt","r") as archivo:

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

    
    with open("segunda etapa/matrizC.txt", "w") as c:
        matrizA=genmatrizA()
        matrizB=genmatrizB()
        final=(sumar(matrizA,matrizB))
        c.write(final)
        
        print(sumar(matrizA,matrizB))
        


main()