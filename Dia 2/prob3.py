class estacionamiento():
    def __init__(self, lugares, movimientos):
        self.lugares = lugares
        self.movimientos = movimientos
        self.slots = []
        self.asignar()
        self.acciones()
    def asignar(self):
        for i in range(self.lugares):
            self.slots.append(None)
    def agregar(self, placa):
        
        for i in range(self.lugares):
            if self.slots[i] == None:
                self.slots[i]=placa
                return
        print(f"SIN ESPACIO {placa}")
        


    def sacar(self, placa):
        encontrado=False
        for i in range(self.lugares):
            if self.slots[i] == placa:
                self.slots[i] = None
                encontrado=True
        if not encontrado:
            print(f"NO ENCONCOTRADO {placa}")
        

    def acciones(self):
        for i in range(self.movimientos):
            accion = str(input("ingresa accion "))
            if accion[0:5] == "ENTRA":
                placa = accion[6:]
                self.agregar(placa)
            else:
                placa=accion[5:]
                self.sacar(placa)
      
    def imprimir(self):
        print("ESTADO FINAL")
        for i in  range(self.lugares):
            if self.slots[i]==None:
                continue
            print(f"{i+1} {self.slots[i]}")
    
n =int(input("ingresa los espacios de estacionamientro: "))
m = int(input("ingresa los movimientos a realizar: "))
est = estacionamiento(n,m)
est.imprimir()
