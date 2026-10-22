

matriz=[
    [2,3],
    [4,5],
    [0,10]

]


def imprimirMatriz(matriz):

    for fila in matriz:
        
        print(fila)
    print("\n")






def traspuesta(matriz):

    matrizT=[]

    filas=len(matriz)
    columnas=len(matriz[0])

  #  print(f"La matriz tiene {filas} filas y {columnas}, columnas\nEs de {filas}*{columnas}")
    for i in range(columnas):
        nuevaFila=[]
        for fila in matriz:
            nuevaFila.append(fila[i])
        matrizT.append(nuevaFila)
    return matrizT




imprimirMatriz(matriz)

imprimirMatriz(traspuesta(matriz))