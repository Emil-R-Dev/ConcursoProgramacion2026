teclado={


    "1": "@", "11": ".", "111":"?", "1111": "1",
    "2": "A", "22":"B", "222":"C", "22222":"2",
    "3": "D", "33":"E", "333": "F", "3333": "3",
    "4":"G", "44":"H", "444": "I", "4444":"4",
    "5":"J", "55":"K", "555": "L", "5555": "5",
    "6": "M", "66":"N", "666":"O", "6666":"6",
    "7": "P", "77": "Q", "777": "R", "7777": "S", "77777": "7",
    "8":"T", "88":"U", "888": "V", "8888": "8",
    "9": "W", "99":"X", "999":"Y", "9999": "Z", "99999": "9",
    "*":"\n",
    "0":"0",
    "#":" "
    }
inicios=[]
fines=[]


def escaneo(cadena):

    c_anterior=cadena[:1]

    inicio=0
    
    indice=0
    for i, c in enumerate(cadena):
        

        if(c_anterior == c):
            
            continue
        else:
            inicios.append(inicio)
            fines.append(i)
            inicio=i
            ultimo_fin=i
            

        c_anterior=c
        indice+=1

    inicios.append(ultimo_fin)
    fines.append(indice)





def traducir(cadena):
    traduccion=""
    for a, b in zip(inicios,fines):
        try:

            traduccion= traduccion + teclado[str(cadena[a:b])]
        except:
            continue
    return traduccion


def main():
    with open("Dia 1/segunda etapa/decode.txt","r") as archivo:
    #cadena = open("segunda etapa/decode.txt","r")
    #cadena=open("segunda etapa/decode.txt","w")
        for cadena in archivo:
            escaneo(cadena)
            traduccion= traducir(cadena)
            print(traduccion)



        
main()