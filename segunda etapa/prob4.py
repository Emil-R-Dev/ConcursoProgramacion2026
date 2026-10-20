paises={ "CHI":"China", "KOR": "Korea", "IND": "India"}
meses=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
"octubre", "noviembre", "diciembre"]

def obetenerDatos(codigo):

    try:

        if(codigo[3:4] != "-" or codigo[8:9] != "-"):
             raise()
   
        pais=paises[codigo[0:3]]
    

        mes=meses[int(codigo[4:6])-1]

        anio=int("20" + codigo[6:8])
        if(anio<2005):
            raise()

        numero=int(codigo[9:14])

        print("Codigo valido. La pieza ", numero, ", se compro en ", pais, " en ", mes," del ",anio)
    except:
        print("Codigo no valido.")

def main():

    codigo=str(input("Ingrese el codigo de la pieza: "))
    obetenerDatos(codigo)


main()

