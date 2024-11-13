from calculadoraIMC import CalculadoraIMC

import unittest

class TestCalculadoraIMC(unittest.TestCase):
    def setUp(self):
        self.calcIMC = CalculadoraIMC()

        def test_resultado(self):
            # Testando o resultado para magreza
            self.assertEqual(self.calcIMC.resultado(60, 1.90), 'magreza')

if __name__ == '__main__':
    unittest.main()