import unittest

class TestSistemaNotas(unittest.TestCase):
    def test_promedio(self):
        nota1 = 14
        nota2 = 16
        promedio = (nota1 + nota2) / 2
        self.assertEqual(promedio, 15)

if __name__ == '__main__':
    unittest.main()