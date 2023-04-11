import unittest
from cambiosdenumeracion import binario2decimal
from cambiosdenumeracion import decimal2binario



class Testnumeracion(unittest.TestCase):
#Test binario a decimal
    def testbinario2decimal(self):
        self.assertEqual(binario2decimal('01011100'), 92)
    def testbinario2decimal1(self):
        self.assertEqual(binario2decimal('011011011100'), 1756)
    def testbinario2decimal2(self):
        self.assertEqual(binario2decimal('111101011010'), 3930)
#Test decimal a binario
    def testdecimal2binario(self):
        self.assertEqual(decimal2binario(97), '01100001')
    def testdecimal2binario1(self):
        self.assertEqual(decimal2binario(166), '10100110')
    def testdecimal2binario2(self):
        self.assertEqual(decimal2binario(1097), '010001001001')
    def testdecimal2binario3(self):
        self.assertEqual(decimal2binario(10097), '0010011101110001')

if __name__ == '__main__':
    unittest.main()

