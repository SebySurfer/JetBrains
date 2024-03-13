

class Factura:
    def __init__(self, pieza, descr, num, precio):
        self.pieza = pieza
        self.descr = descr
        self.num = num
        self.precio = precio

    def getPieza(self):
        return self.pieza

    def getDescr(self):
        return self.descr

    def getNum(self):
        return self.num

    def getPrecio(self):
        return self.precio

    def setPieza(self, pieza):
        self.pieza = pieza

    def setDescr(self, descr):
        self.descr = descr

    def setNum(self, num):
        self.num = num

    def setPrecio(self, precio):
        self.precio = precio

    def obtenerMontoFactura(self):
        p = 0

        if self.num < 0:
            self.num = 0

        if self.precio < 0:
            self.precio = 0.0

        p = self.num * self.precio

        return p


if __name__ == "__main__":
    FacturaTest = Factura("0EV-303-23R", "Pieza chida", 6, 250.50)


    FacturaTest.setDescr("De hecho es mas chida que lo que pense")

    print(FacturaTest.getDescr())



    print(FacturaTest.obtenerMontoFactura())