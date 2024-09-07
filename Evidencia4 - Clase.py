class Scooter:
    def __init__(self, color, marca, modelo, velocidad_maxima):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.__bateria = 100
        self.__velocidad_actual = 0
        self.__encendida = False

    @property
    def bateria(self):
        return self.__bateria

    @bateria.setter
    def bateria(self, value):
        if value < 0:
            raise ValueError("La batería no puede ser negativa.")
        self.__bateria = value

    @property
    def velocidad_actual(self):
        return self.__velocidad_actual

    @velocidad_actual.setter
    def velocidad_actual(self, value):
        if value < 0:
            raise ValueError("La velocidad no puede ser negativa.")
        if value > self.velocidad_maxima:
            raise ValueError("La velocidad no puede superar la velocidad máxima.")
        self.__velocidad_actual = value

    def encender(self):
        if self.__bateria > 0:
            self.__encendida = True
            self.__bateria -= 1  # Asumiendo que encender la scooter consume 1 unidad de batería
            return "Scooter encendida."
        else:
            raise ValueError("No se puede encender. La batería está vacía.")

    def apagar(self):
        if self.__encendida:
            self.__encendida = False
            return "Scooter apagada."
        else:
            raise ValueError("La scooter ya está apagada.")

    def acelerar(self, incremento):
        if self.__encendida:
            if self.__bateria > 0:
                nueva_velocidad = self.__velocidad_actual + incremento
                if nueva_velocidad > self.velocidad_maxima:
                    self.__velocidad_actual = self.velocidad_maxima
                else:
                    self.__velocidad_actual = nueva_velocidad
                self.__bateria -= 1  # Asumiendo que acelerar consume 1 unidad de batería
                return (f"Aceleramos: {incremento} km/h --- Velocidad actual: {self.__velocidad_actual} km/h, "
                        f"Nivel de batería: {self.__bateria}")
            else:
                raise ValueError("No se puede acelerar. La batería está vacía.")
        else:
            raise ValueError("La scooter está apagada. Primero enciéndela.")

    def frenar(self, decremento):
        if self.__encendida:
            nueva_velocidad = self.__velocidad_actual - decremento
            if nueva_velocidad < 0:
                self.__velocidad_actual = 0
            else:
                self.__velocidad_actual = nueva_velocidad
            self.__bateria -= 1  # Asumiendo que frenar consume 1 unidad de batería
            return (f"Desaceleramos: {decremento} km/h --- Velocidad actual: {self.__velocidad_actual} km/h, "
                    f"Nivel de batería: {self.__bateria}")
        else:
            raise ValueError("La scooter está apagada. Primero enciéndela.")

    def __str__(self):
        estado = "Encendida" if self.__encendida else "Apagada"
        return (f"Scooter - Color: {self.color}, Marca: {self.marca}, Modelo: {self.modelo}, "
                f"Velocidad Máxima: {self.velocidad_maxima} km/h, Velocidad Actual: {self.__velocidad_actual} km/h, "
                f"Batería: {self.__bateria}, Estado: {estado}")


# Ejemplo de uso
scooter = Scooter("Rojo", "Honda", "Activa", 60)

try:
    print(scooter.encender())
    print(scooter.acelerar(20))
    print(scooter.frenar(10))
    print(scooter)  # Uso del método __str__
    print(scooter.apagar())
except ValueError as e:
    print(e)
