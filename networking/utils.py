from digitalElectronics.tools import *
import re
CLASS_A_SUBNET_MASK = '11111111'  # the sequence of one('1') bits of the class A private address subnet mask (the minimum number)
CLASS_B_SUBNET_MASK = '111111111111'  # the sequence of one('1') bits of the class B private address subnet mask (the minimum number)
CLASS_C_SUBNET_MASK = '1111111111111111'  # the sequence of one('1') bits of the class B private address subnet mask (the minimum number)


"""Check if the Subnet Mask is valid or not ["xxx","xxx","xxx","xxx"]"""
def isValidSubnetMask(subnetMask):
    correctRange = list(map(lambda block: int(block) in range(0,256),subnetMask))  # [True, False, ...] check if the each block is in the range of 1-255
    print(correctRange)
    for block in correctRange:
        if block == False:
            return False
    binarySubnetMask = convertlistDecimalsToBinary(subnetMask)
    notCorrect = re.match('.*0+1.*',binarySubnetMask)  # Check if there is a '1' that comes after a '0', which is absurd
    if notCorrect:
        return False
    return True


"""Check if the subnet mask is suitable for the private ip address chosen"""
def subnetMaskSuitableForIpAddress(subnetMask: str, ipAddressClass: str)->bool:
    subnetMask = subnetMask.split('.')  # getting the list of blocks of the subnet mask ['xxx','xxx',...]
    subnetMaskBinary = convertlistDecimalsToBinary(subnetMask)  # get the binary sequence of the subnet mask
    subnetMaskLength = subnetMaskBinary.count('1')  # the number of the one '1' digits in the subnet mask
    print("binary subnet mask: ", subnetMaskBinary)
    if ipAddressClass == 'A':
        if subnetMaskLength < len(CLASS_A_SUBNET_MASK):
            return False
        return True
    if ipAddressClass == 'B':
        if subnetMaskLength < len(CLASS_B_SUBNET_MASK):
            return False
        return True
    if ipAddressClass == 'C':
        if subnetMaskLength < len(CLASS_C_SUBNET_MASK):
            return False
        return True
    return False  # The class is not a private class ('#')

"""Return the class of the corresponding private ip address,
returns 'A', 'B', 'C' or '#' for none
considering that the ip address passed is a valid private ip address"""
def getPrivateIpAddressClass(ipAddress: str)->str:
    ipAddress = ipAddress.split('.')
    print(ipAddress[0])
    print(ipAddress[1])
    if ipAddress[0] == '10':
        return 'A'
    elif ipAddress[0] == '172' and int(ipAddress[1]) in range(16,32):
        return 'B'
    elif ipAddress[0] == '192' and ipAddress[1] == '168':
        return 'C'
    else:
        return '#'  # does not match any private ip address

