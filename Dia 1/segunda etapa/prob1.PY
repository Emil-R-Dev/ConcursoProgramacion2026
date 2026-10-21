caracteres_validos = {"A": "a", "B":"b", "C": "c", "D":"d", 
                    "E": "e", "F":"f", "G": "g", "H":"h",
                    "I": "i", "J":"j", "K": "k", "L":"l", 
                    "M": "m", "N":"n", "O": "o", "P":"p",
                    "Q": "q", "R":"r", "S": "s", "T":"t", 
                    "U": "u", "V":"v", "W": "w", "X":"x",
                    "Y": "y", "Z": "z",
                    "a": "a", "b":"b", "c": "c", "d":"d", 
                    "e": "e", "f":"f", "g": "g", "h":"h",
                    "i": "i", "j":"j", "k": "k", "l":"l", 
                    "m": "m", "n":"n", "o": "o", "p":"p",
                    "q": "q", "r":"r", "s": "s", "t":"t", 
                    "u": "u", "v":"v", "w": "w", "x":"x",
                    "y": "y", "z": "z"}

def normalizar(cadena):
    normalizada = ""
    for c in cadena:
    
        normalizada = normalizada + str(caracteres_validos[c])
 

    return normalizada


def traducir(normalizada):
    long = len(normalizada)
    traduccion = "yo" + normalizada[long-1:] + normalizada[:long-1] + "yo"
    return traduccion

def main():
    palabras = []
    while True:
        try:
            palabra = str(input())

            if(palabra=="FIN"):
                break
            if len(palabra) > 10 or len(palabra)<1:
                print("palabra no valida in tente nuevamente")
                continue
            palabra_normalizada =normalizar(palabra)
            palabras.append(palabra_normalizada)

            
        except:
            print("Palabra invalida. Intente nuevamente.")
    traducidas=[]
    for p in palabras:
        traducidas.append(traducir(p))

    for p in traducidas:
        print(p)


main()