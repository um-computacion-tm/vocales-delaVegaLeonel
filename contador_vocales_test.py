import unittest
from contador_vocales import vocal_counter
from contador_vocales import vocal_counter_des

class TestVocales(unittest.TestCase):

    def test_caso_1(self):
        esperado = {
            'a': 5,
            'e': 1,
            'u': 1,
        }
        resultado = vocal_counter("aca hay una frase")
        self.assertDictEqual(resultado, esperado)

    def test_caso_2(self):
        ca, ce, ci, co, cu = vocal_counter_des("ursula")
        resultado = (ca, ce, ci, co, cu)
        self.assertEqual(resultado, (1, 0, 0, 0, 2))

if __name__ == '__main__':
    unittest.main()


