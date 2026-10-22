

def crearCuadro(n):
    matriz=[]
    for i in range (n):
        fila=[]
        for _ in range(n):
            fila.append(None)
        matriz.append(fila)

    i=0
    j=int((n-1)/2)

    matriz[i][j]="01"

    for k in range(2,(n*n)+1):
        i_ant=i
        j_ant=j

        if (i-1) < 0:
            i=n-1
        else:
            i-=1
        
        if (j+1)==n:
            j=0
        else:
            j+=1
        
        if matriz[i][j]!= None:
            i= i_ant+1
            j=j_ant
        if k <10:
            asignacion="0"+str(k)
        else:
            asignacion=str(k)
        matriz[i][j]=asignacion
    return matriz





def main():
    while True:
        n=int(input("Ingrese tamaño matriz: "))
        if(n%2==0):
            print("Ingreso un numero par")
            continue
        cuadroMagico=crearCuadro(n)

        for fila in cuadroMagico:
            print(fila)
        break
    with open("Dia 2/magico.txt", "w") as c:

        for fila in cuadroMagico:
            for numero in fila:
                c.write(f"{numero} ")
            c.write("\n")

main()

