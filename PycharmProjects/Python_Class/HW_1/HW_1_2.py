import random
from decimal import Decimal

def calcular_pago(peso, descuento):
    pago = peso * 28.50
    if descuento:
        return pago * 0.85
    else:
        return pago

def main():
    clientes = []

    random.seed()

    for _ in range(15):
        num_pes = random.randint(1, 25)
        desc = num_pes > 10
        clientes.append((num_pes, desc))

    total_count = 0

    for i, (peso, desc) in enumerate(clientes):
        print(f"Cliente {i + 1}: {cliente_str(peso, desc)}")
        total_count += calcular_pago(peso, desc)

    print("\n**********************************************\n")
    print(f"En total la tienda gano ${total_count:.3f} pesos")

def cliente_str(peso, desc):
    round_format = "{:.3f}".format
    if desc:
        return f"Agarró {peso}kg y hubiera pagado ${round_format(peso * 28.50)}, pero con 15% de descuento fue ${round_format(calcular_pago(peso, desc))} pesos"
    else:
        return f"Agarró {peso}kg y pagó ${round_format(peso * 28.50)} pesos"

if __name__ == "__main__":
    main()