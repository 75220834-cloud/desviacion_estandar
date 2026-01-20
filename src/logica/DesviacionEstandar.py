class DesviacionEstandar:
    def __init__(self, datos):
        self.__datos = datos

    def calcular(self):
        n = len(self.__datos)

        if n == 0:
            return None

        if n == 1:
            return 0

        media = sum(self.__datos) / n
        suma = sum((x - media) ** 2 for x in self.__datos)

        return (suma / n) ** 0.5
