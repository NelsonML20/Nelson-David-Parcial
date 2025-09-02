# archivo: main.py

from aparatos import Aparato

# Crear instancias de aparatos
a1 = Aparato("Refrigerador", 150, 300)
a2 = Aparato("Televisor", 100, 120)
a3 = Aparato("Aire Acondicionado", 2000, 150)
a4 = Aparato("Iluminación", 60, 200)

# Mostrar datos de cada aparato
print(" Registro de Consumo Eléctrico Mensual\n")
for aparato in Aparato.lista_aparatos:
    print(aparato.info())

# Calcular totales
total_consumo = sum(a.calcular_consumo() for a in Aparato.lista_aparatos)
total_costo = sum(a.calcular_costo() for a in Aparato.lista_aparatos)

print("\n Resumen General:")
print(f"Total de Consumo: {total_consumo:.2f} kWh")
print(f"Total a pagar: ${total_costo:.2f}")
