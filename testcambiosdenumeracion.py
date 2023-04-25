import unittest
from cambiosdenumeracion import binario2decimal
from cambiosdenumeracion import decimal2binario
from cambiosdenumeracion import decimal2octal
from cambiosdenumeracion import decimal2hex
from cambiosdenumeracion import binario2hex
from cambiosdenumeracion import binario2octal
from cambiosdenumeracion import octal2decimal
from cambiosdenumeracion import octal2binario
from cambiosdenumeracion import octal2hex
from cambiosdenumeracion import hex2decimal
class Testnumeracion(unittest.TestCase):
#Test binario a decimal
    def testbinario2decimal(self):
        self.assertEqual(binario2decimal('01011100'), 92)
    def testbinario2decimal1(self):
        self.assertEqual(binario2decimal('011011011100'), 1756)
    def testbinario2decimal2(self):
        self.assertEqual(binario2decimal('111101011010'), 3930)
#Test binario a octal
    def testbinario2octal(self):
        self.assertEqual(binario2octal('01011100'), 134)
    def testbinario2octal1(self):
        self.assertEqual(binario2octal('011011011100'), 3334)
#Test binario a Hexadecimal
    def testbinario2hex(self):
        self.assertEqual(binario2hex('011011011100'), '6DC')
    def testbinario2hex1(self):
        self.assertEqual(binario2hex('111011011011100'), '76DC')
#Test decimal a binario
    def testdecimal2binario(self):
        self.assertEqual(decimal2binario(97), '01100001')
    def testdecimal2binario1(self):
        self.assertEqual(decimal2binario(166), '10100110')
    def testdecimal2binario2(self):
        self.assertEqual(decimal2binario(1097), '010001001001')
    def testdecimal2binario3(self):
        self.assertEqual(decimal2binario(10097), '0010011101110001')
#Test decimal a octal
    def testdecimal2octal(self):
        self.assertEqual(decimal2octal(125), 175)
    def testdecimal2octal2(self):
        self.assertEqual(decimal2octal(575), 1077)
    def testdecimal2octal3(self):
        self.assertEqual(decimal2octal(2789), 5345)
#Test decimal a Hexadecimal
    def testdecimal2hex(self):
        self.assertEqual(decimal2hex(125), '7D')
    def testdecimal2hex1(self):
        self.assertEqual(decimal2hex(775), '307')
    def testdecimal2hex2(self):
        self.assertEqual(decimal2hex(1903), '76F')
    def testdecimal2hex3(self):
        self.assertEqual(decimal2hex(1756), '6DC')
    def testdecimal2hex4(self):
        self.assertEqual(decimal2hex(5655), '1617')
    def testdecimal2hex5(self):
        self.assertEqual(decimal2hex(3510), 'DB6')

#Test octal a decimal
    def testoctal2decimal(self):
        self.assertEqual(octal2decimal(6666), 3510)
    def testoctal2decimal2(self):
        self.assertEqual(octal2decimal(4567), 2423)
    def testoctal2decimal1(self):
        self.assertEqual(octal2decimal(7654), 4012)
#Test octal a binario
    def testoctal2binario(self):
        self.assertEqual(octal2binario(6666),'110110110110')
    def testoctal2binario1(self):
        self.assertEqual(octal2binario(4567),'100101110111')
#Test octal a hexadecimal
    def testoctal2hex(self):
        self.assertEqual(octal2hex(6666), 'DB6')
#Test Hexadecimal a decimal
    def testhex2decimal(self):
        self.assertEqual(hex2decimal('DB6'), 3510)
if __name__ == '__main__':
    unittest.main()

