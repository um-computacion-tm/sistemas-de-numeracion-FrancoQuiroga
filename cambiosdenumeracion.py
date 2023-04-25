def binario2decimal(binario):
    total = 0
    for i in range(0, len(binario)):
        total += int(binario[-i-1]) * 2 ** i

    return total
def binario2octal(binario):
    resultdecimal = binario2decimal(binario)
    resultoctal = decimal2octal(resultdecimal)
    return resultoctal
def binario2hex(binario):
    resultdecimal = binario2decimal(binario)
    resulthex = decimal2hex(resultdecimal)
    return resulthex
def decimal2octal(decimal):
    resultoctal = ''
    resultinvertido = ''
    while decimal >= 8:
        resultinvertido += str(decimal % 8)
        decimal = decimal // 8
    resultinvertido += str(decimal) 
    for i in range(0,len(resultinvertido)):
        resultoctal = resultoctal + resultinvertido[-i-1]
    return int(resultoctal)
def decimal2hex(decimal):
    diccionarioshex = {15: 'F', 14: 'E', 13: 'D', 12: 'C',11: 'B',10: 'A'}
    valoreshex = (15, 14, 13, 12, 11, 10)
    resulthex = ''
    resultinvertido = ''
    while decimal >= 16:
        if 16 > (decimal % 16) > 9:
            for i in valoreshex:
                if ((decimal % 16) % i) == 0:
                    resultinvertido += diccionarioshex[i]
        else:
            resultinvertido += str(decimal % 16)
        decimal = decimal // 16
    if decimal in diccionarioshex:
        resultinvertido += diccionarioshex[decimal]
    else:    
        resultinvertido += str(decimal) 
    for i in range(0,len(resultinvertido)):
        resulthex = resulthex + resultinvertido[-i-1]
    return resulthex
def decimal2binario(decimal):
    result = ''
    resultinvertido = ''
    while decimal >= 2:
        resultinvertido += str(decimal % 2)
        decimal = decimal // 2
    resultinvertido += str(decimal)
    for i in range(0,len(resultinvertido)):
        result = result + resultinvertido[-i-1]
    while len(result) % 4 != 0:
        result = '0' + result
    return result
def octal2decimal(octal):
    octalstring = str(octal)
    totaloctal = 0
    for i in range(0, len(octalstring)):
        totaloctal += int(octalstring[-i-1]) * 8 ** i
    return totaloctal
def octal2binario(octal):
    decimalresult = octal2decimal(octal)
    binarioresult = decimal2binario(decimalresult)
    return binarioresult
def octal2hex(octal1):
    decimalresult = octal2decimal(octal1)
    hexresult = str(decimal2hex(decimalresult))
    return hexresult
def hex2decimal(hex):
    diccionarioshex = {'F': 15,'E': 14, 'D': 13,'C': 12,'B': 11,'A': 10 }
    palabraanumero = 0
    resulthex = 0
    for i in range(0, len(hex)):
        if diccionarioshex[i].isnumeric():
                resulthex += int(hex[-i-1]) * 16 ** i
        else:
            palabraanumero = diccionarioshex[i]
            resulthex += palabraanumero * 16 ** i
    return resulthex
