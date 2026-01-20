import unittest
from src.logica.DesviacionEstandar import DesviacionEstandar


class TestDesviacionEstandar(unittest.TestCase):

    def test_lista_vacia_retorna_none(self):
        datos = []
        desviacion = DesviacionEstandar(datos)
        self.assertIsNone(desviacion.calcular())

    def test_lista_un_elemento_retorna_cero(self):
        datos = [5]
        desviacion = DesviacionEstandar(datos)
        self.assertEqual(0, desviacion.calcular())

    def test_lista_varios_elementos_retorna_desviacion(self):
        datos = [2, 4, 4, 4, 5, 5, 7, 9]
        desviacion = DesviacionEstandar(datos)
        self.assertEqual(2, desviacion.calcular())
