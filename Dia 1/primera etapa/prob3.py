numeros = []
def numero():
    ip = ""
    
    for i in range(4):
        n =int(input("N"":" ))
        numeros.append(convertirBinario(n))
        ip + str(n)
        print(ip)
        if n>=0 and n<=255:
            pass
        else:
            print("Rango no valido")


def convertirBinario(num):
    residuo=num
    bin=""    
    for i in range(8):

        bin = bin + str(residuo % 2)
        residuo = residuo // 2

    return str(invertirCadena(bin))

def invertirCadena(cadena):
    invertida=""
    indice=len(cadena)-1
    while indice>=0:

        invertida = invertida + cadena[indice]

        indice -=1

    return invertida

def imprimir(numeros):
    cadena=""
    for i in range(4):
        cadena=cadena + str(numeros[i])
        if (i != 3):
            cadena= cadena +"."
        
    print(cadena)
     


def main():

    numero()
    imprimir(numeros)

main()