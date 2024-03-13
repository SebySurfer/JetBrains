import random

print("Cuantos empleados son ?: ")
num = int(input())
print(f"Tomamos en cuenta que el salario base es igual a $30000.00 pesos")
print("***************************************************************************************")

emp_list = []

for i in range(num):
    vent1 = random.uniform(50000, 150001)
    vent2 = random.uniform(50000, 150001)
    vent3 = random.uniform(50000, 150001)

    emp_list.append((i + 1, vent1, vent2, vent3))

for emp_data in emp_list:
    id, venta1, venta2, venta3 = emp_data
    comis_ven = (venta1 + venta2 + venta3) * 0.10
    com_base = 30000
    comis_tot = comis_ven + com_base

    print(f"Empleado ID: 000{id}. Ventas: (${venta1:.3f}, ${venta2:.3f}, ${venta3:.3f}). Comision de Ventas: ${comis_ven:.3f}. Comision TOTAL con base = ${comis_tot:.3f}")
    print("")




