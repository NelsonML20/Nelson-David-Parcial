class Aparato:

    lista_aparatos = []

    def _init_(self, nombre, potencia_watts, horas_mensuales):
        self.nombre = nombre
        self.potencia = potencia_watts
        self.horas = horas_mensuales
        Aparato.lista_aparatos.append(self)

    def calcular_consumo(self):
        # kWh = (Watts / 1000) * horas
        return (self.potencia / 1000) * self.horas

    def calcular_costo(self):
        # Costo = kWh * $0.20
        return self.calcular_consumo() * 0.20

    def info(self):
        return (f"Aparato: {self.nombre} | Potencia: {self.potencia}W | "
                f"Horas/mes: {self.horas} | Consumo: {self.calcular_consumo():.2f} kWh | "
                f"Costo: ${self.calcular_costo():.2f}")
    

