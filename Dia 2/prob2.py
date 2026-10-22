

class gestionHerramientas():
    def __init__(self):
        self.herramientas=["T01", "T02", "T03", "M10", "M20","A10", "A20","C10","C20","C30"]
        #herramientas -> persona
        self.prestamos={}
        self.numeroErrores=0
       
        

    def prestar(self,herramienta, persona):
        try:
            if self.prestamos[str(herramienta)] != None:
                pass

        except:
            self.prestamos[str(herramienta)]=str(persona)
         
           # print("ERRORPREST1")
            return

        try:
            if self.prestamos[str(herramienta)] != None:
                raise()
        except:
            self.numeroErrores+=1
          #  print("ERRORPREST2")
            return
        

    def devolver(self,herramienta,persona):
        try:
            if self.prestamos[str(herramienta)] == None:
                self.numeroErrores+=1
                return
            if self.prestamos[str(herramienta)] != str(persona):
                self.numeroErrores+=1
                return
            self.prestamos.pop(str(herramienta))
        except:
           # print("ERRORDEV")
            self.numeroErrores+=1
            return
    def geterrores(self):
        return self.numeroErrores
    def getprestamos(self):
        if self.prestamos=={}:
            print("NINGUNA")
        else:
            for clave, valor in self.prestamos.items():
                print(f"{clave} {valor}")


def main():
    gestor=gestionHerramientas()
    n=int(input())

    for i in range(n):

        instruccion=input()
        #print(instruccion[0:8])
        if instruccion[0:6]=="PRESTA":
            herramienta=""+ instruccion[7:10]
            persona=""+instruccion[11:]
            gestor.prestar(herramienta, persona)
        if instruccion[0:8]=="DEVUELVE":
            herramienta=""+ instruccion[9:12]
            persona=""+instruccion[13:]
            gestor.devolver(herramienta, persona)
        
    print(f"ERRORES {gestor.geterrores()}")
    gestor.getprestamos()


main()