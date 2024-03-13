cap = int(input("Ahorita queremos encontrar tu importe de interes. Cuanto capital tienes?: "))
tasa = int(input("La tasa de interes: "))
per = int(input("Periodo: "))

imp = cap*per*(tasa/100)

print("Es tu tasa de interes: ", round(imp, 3))

cap1 = int(input("Ahorita queremos encontrar el numero de periodos para acumular tu importe deseado. Cuanto capital tienes?: "))
tasa1 = int(input("La tasa de interes: "))
imp1 = int(input("Importe de interes: "))

per1 = imp1/(tasa1*cap1)

print("Es tu periodo deseado: ", round(per1, 2))*100

cap2 = int(input("Ahorita queremos encontrar tu tasa de interes. Cuanto capital tienes?: "))
per2 = int(input("Periodo: "))
imp2 = int(input("Importe de interes: "))

tasa2 = (imp2/(per2*cap2))*100

print("Es tu tasa de interes : ", round(tasa2, 3))

#importe de interes = 600
#Capital = 10000
#Tasa de interes = 3
#Periodo = 2

