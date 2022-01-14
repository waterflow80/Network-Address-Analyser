"""Convert a decimal number (string) into a binary number,
retruns '#' if the operation cannot be done"""
def toBinary8Bit(sourceNumber: int, resultNumber: str = '0')->str:
    if sourceNumber == 0:
        if len(resultNumber) == 1:  # Case we have a zero
            return '00000000'  # zero in eight bits
        else:
            resultNumber = resultNumber[1::]  # Removing the default '0' that has been declared in the funciton arguments
            if len(resultNumber) > 8:
                return '#'  # the number cannot be converted to 8 bit binary number
            while(len(resultNumber) < 8):
                resultNumber += '0'
            return resultNumber[::-1]  # The reverse because it was initially reversed
    else:
        return toBinary8Bit(sourceNumber // 2, resultNumber + str(sourceNumber % 2))

""" Convert any decimal number into a binary number (sequence)
"""
def toBinaryAny(sourceNumber: int, resultNumber: str = '0')->str:
    if sourceNumber == 0:
        if len(resultNumber) == 1:  # Case we have a zero
            return '0'
        else:
            resultNumber = resultNumber[1::]  # Removing the default '0' that has been declared in the funciton arguments
            if len(resultNumber) > 8:
                return '#'  # the number cannot be converted to 8 bit binary number
            while(len(resultNumber) < 8):
                resultNumber += '0'
            return resultNumber[::-1]  # The reverse because it was initially reversed
    else:
        return toBinary8Bit(sourceNumber // 2, resultNumber + str(sourceNumber % 2))

"""Convert a list of decimals into one binary sequence"""
def convertlistDecimalsToBinary(decimalsList: list)->str:
    binarySequence = ''
    for block in decimalsList:
        binarySequence += toBinary8Bit(int(block))
    return binarySequence

"""Make the binary sum of two binary numbers"""
def binarySum(number1: str, number2: str)->str:
    sum = ''
    if len(number1) != len(number2) or len(number1) == 0 or len(number2) == 0:
        return False  # cannot make the sum, some conditions are missed
    for i in range(len(number1)):
        if number1[i] == '1' and number2[i] == '1':
            sum += '1'
        else:
            sum += '0'
    return sum

"""Convert a 32 binary sequence into a list of four blocks of decimal numbers,
the input should be correct in order to have valid result, otherwise we will get False"""
def binary32ToDecimal(binarySequence: str)->list:
    if len(binarySequence) != 32:
        return False
    binarySequence = binarySequence[::-1]  # reversing the sequence to apply the power correctly
    decimalNumber = 0
    decimalNumberBlocks = []  # group the decimal equivalent of each 8 bit binary number in the list
    while binarySequence:
        for i in range(8):
            decimalNumber += int(binarySequence[i]) * 2 ** i
        decimalNumberBlocks.append(str(decimalNumber))
        decimalNumber = 0  # initialize the number to zero
        binarySequence = binarySequence[8::]  # eliminate the first 8 bit digits that has been converted from the sequence
    decimalNumberBlocks.reverse()  # get the initial order of the numbers
    return decimalNumberBlocks


"""Convert a binary sequence into a decimal number"""
def binaryToDecimal(binarySequence: str)->str:
    decimalNumber = 0
    binarySequence = binarySequence[::-1]
    for i in range(len(binarySequence)):
        decimalNumber += int(binarySequence[i]) * 2 ** i
    return decimalNumber

"""Return the biggest number that can be formed from the number of bits passed in the 
parameter, ex: 3 bits --> biggest number = 7"""
def getBiggestDecimalNumber(numberOfDigits: int)->int:
    binaryNumber = ''
    for i in range(numberOfDigits):
        binaryNumber += '1'  # gettig the biggest number in binary
    decimalNumber = binaryToDecimal(binaryNumber)  # converting the binary number into decimal number
    return decimalNumber

"""Return the biggest number that can be formed from the number of bits passed in the 
parameter, ex: 3 bits --> '111' """
def getBiggestNumberBinary(numberOfDigits: int)->int:
    binaryNumber = ''
    for i in range(numberOfDigits):
        binaryNumber += '1'  # gettig the biggest number in binary
    return binaryNumber