#Creamos la clase Aparatos
class Aparato:
    
    #creamos una lista vacia
    lista_aparatos = []

   #Creamos el contructor con los parametros nombre, potencia, hora_mensuales
    def __init__(self, nombre, potencia_watts, horas_mensuales):
        self.nombre = nombre
        self.potencia = potencia_watts
        self.horas = horas_mensuales
        Aparato.lista_aparatos.append(self)

    #definimos la función para calcular el consumo
    def calcular_consumo(self):
       
        return (self.potencia / 1000) * self.horas    # kWh = (Watts / 1000) * horas
    
    #definimos la función para calcular el costo
    def calcular_costo(self):
       
        return self.calcular_consumo() * 0.20     # Costo = kWh * $0.20

    #bloque de codigo para devolver la cadena de texto con toda la información del aparato
    def info(self):
        return (f"Aparato: {self.nombre} | Potencia: {self.potencia}W | "
                f"Horas/mes: {self.horas} | Consumo: {self.calcular_consumo():.2f} kWh | "
                f"Costo: ${self.calcular_costo():.2f}")
    
    if __name__ == "__main__":
     pass

 

