import unittest
from src.logica.DesviacionEstandar import DesviacionEstandar


class TestDesviacionEstandar(unittest.TestCase):

    def test_lista_vacia_retorna_none(self):
        datos = []
        desviacion = DesviacionEstandar(datos)
        self.assertIsNone(desviacion.calcular())
