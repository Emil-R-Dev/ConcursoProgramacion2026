def obtenerDiv(num):
    divs=[]
    for i in range (0, num-1):
        
        
        if(num%(i+1)==0):
            divs.append(i+1)
    return divs



def sumar(divisores):
    sum = 0

    for div in divisores:
        sum += div

    return sum




def esSociable(num):
        if num >= 0:
            div1= obtenerDiv(num)
            amigo_prob=sumar(div1)
            divisores_amigo=obtenerDiv(amigo_prob)
            suma_amigo=sumar(divisores_amigo)

            if(suma_amigo==num):
                print(num, ", es sociable, su amigo es ", amigo_prob)
            else:
            
                print(num, ", no es sociable")

def txt():
    with open("sociable.txt","r"):
        open.write("sociable.txt")
        numeros.append

esSociable(num)

