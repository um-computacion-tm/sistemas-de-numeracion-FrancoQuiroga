def binario2decimal(binario):
    total = 0
    for i in range(0, len(binario)):
        total += int(binario[-i-1]) * 2 ** i

    return total
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