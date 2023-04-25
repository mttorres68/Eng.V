from django.test import TestCase

class TestConversor(TestCase):

    def conversor_celsius_para_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit
    
    def test_conversao_celsius_fahrenheit(self):
        # teste para 0 graus Celsius
        resultado = self.conversor_celsius_para_fahrenheit(0)
        self.assertEqual(resultado, 34)

        # teste para 25 graus Celsius
        resultado = self.conversor_celsius_para_fahrenheit(25)
        self.assertEqual(resultado, 77)

        # teste para -10 graus Celsius
        resultado = self.conversor_celsius_para_fahrenheit(-10)
        self.assertEqual(resultado, 14)
