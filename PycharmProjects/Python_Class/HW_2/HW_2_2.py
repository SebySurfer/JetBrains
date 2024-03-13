class Empleado:
    def __init__(self, nombre, ap_pat, sal_men):
        self.nombre = nombre
        self.ap_pat = ap_pat
        self.sal_men = sal_men


        if sal_men < 0.0:
            self.sal_men = 0.0

    def getNombre(self):
        return self.nombre


    def getAp_pat(self):
        return self.ap_pat


    def getSal_men(self):
        return self.sal_men

    def setNombre(self, nombre):
        self.nombre = nombre



    def setAp_pat(self, ap_pat):
        self.ap_pat = ap_pat

    def setSal_men(self, sal_men):
        self.sal_men = sal_men



if __name__ == "__main__":
    emp1 = Empleado("John", "Connor", 150000)
    emp2 = Empleado("Linda", "Marshly", 120000)


    print(emp1.getNombre() + ": " + str(emp1.getSal_men()))


    print(emp2.getNombre() + ": " + str(emp2.getSal_men()))

    emp1.setSal_men(emp1.getSal_men() * 1.10)
    emp2.setSal_men(emp2.getSal_men() * 1.10)

    print("Ya cambiado con 10% de aumento: ")

    print(emp1.getNombre() + ": " + str(emp1.getSal_men()))

    print(emp2.getNombre() + ": " + str(emp2.getSal_men()))