
dict_romano={"M":1000,"D":500, "C":100, "L":50, "X":10, "V":5, "I":1, 0:0}

dict_resta={"X":"I", "V":"I", "C":"X", "L":"X", "M":"C", "D": "C", "I":0}
def convertirRomano(numero):
    residuo=numero
    romano=""
    
    
    for letra, valor in dict_romano.items():
        if residuo==0:
            break
    
        


        if residuo//valor <=3:
            eval=residuo//valor
        else:
            eval=3
            

        for i in range(eval):
            romano = romano + letra
        

        residuo-=valor*eval

        if  residuo>=int( dict_romano[letra] - dict_romano[dict_resta[str(letra)]]   ):

            romano=romano + dict_resta[letra] + letra
            residuo-= int( dict_romano[letra] - dict_romano[dict_resta[str(letra)]]   )

            continue


    return romano

def main():
    numeros=[]
    numerosromanos=[]
    numero=-1
    while numero != 0:
        numero=int(input())
        if numero<0 or numero>3500:
            continue
        numeros.append(int(numero))
    print("\n")
    for numero in  numeros:

        numerosromanos.append(convertirRomano(numero))

    for numero, numeroromano in zip(numeros,numerosromanos):

        print(numero, "   ", numeroromano)

main()