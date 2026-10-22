

def calcularTiempo(N,M):
    ventanillaTiempo=[]
    ventanillaPersonas=[]
    for _ in range(N):
        ventanillaTiempo.append(0)
        ventanillaPersonas.append(0)

    for tiempo in M:
        menor=10000
        indice=0

        for i,espacio in enumerate(ventanillaPersonas):

            if espacio<menor:
                menor=espacio
                indice=i

            # if espacio==0:
            #     ventanillaPersonas[i]+=1
            #     ventanillaTiempo[i]+=tiempo
            #     break
        
        ventanillaPersonas[indice]+=1
        ventanillaTiempo[indice]+=tiempo

        continue
    


    ventanillaRapida=0
    tiempoMayor=0
    for i, tiempo in enumerate(ventanillaTiempo):
        if tiempo>tiempoMayor:
            tiempoMayor=tiempo
            ventanillaRapida=i+1


    for i, tiempo in enumerate(ventanillaTiempo):

        print(f"{i+1} {tiempo}")  
    
    print(f"ULTIMA {ventanillaRapida} {tiempoMayor}")
            

def main():

    n=int(input())
    m=int(input())
    M=[]
    for i in range(m):
        M.append(int(input()))


    calcularTiempo(n,M)
            
main()