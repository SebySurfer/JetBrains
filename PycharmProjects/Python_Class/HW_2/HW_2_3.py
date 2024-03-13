class Fecha:
    def __init__(self, mes, dia, año):
        self.mes = mes
        self.dia = dia
        self.año = año

    def mostrarFecha(self):
        return self.mes, " / ", self.dia, " / ", self.año

    def setMes(self, x):
        self.mes = x

    def setDia(self, x):
        self.dia = x

    def setAño(self, x):
        self.año = x

    def getMes(self):
        return self.mes

    def getDia(self):
        return self.dia

    def getAño(self):
        return self.año


FechaTest = Fecha(5, 22, 2003)

print(FechaTest.mostrarFecha())




