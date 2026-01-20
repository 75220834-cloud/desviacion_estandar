class DesviacionEstandar:
    def __init__(self, datos):
        self.__datos = datos

    def calcular(self):
        n = len(self.__datos)

        if n == 0:
            return None

        if n == 1:
            return 0

        # media
        media = sum(self.__datos) / n

        # suma de cuadrados
        suma = 0
        for x in self.__datos:
            suma += (x - media) ** 2

        # desviación estándar poblacional
        return (suma / n) ** 0.5
