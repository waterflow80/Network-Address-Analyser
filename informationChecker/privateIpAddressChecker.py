import re

"""Check if the ip address given is a valid private ip address"""
def checkPrivateIpAddress(ipAddress):
    ipAddress = str(ipAddress)
    if ipAddress.count('.') != 3:
        return False
    if not re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', ipAddress):
        return False
    ipAddressBlocks = ipAddress.split('.')  # ['xxx','xxx','xxx','xxx']
    if not isAPrivateAddress(ipAddressBlocks):
        return False
    return True


"""Check if the ip address is in the range of private ip address by 
checking the range of each block"""
def isAPrivateAddress(ipAddress):
    if is_A_Private_Class_A_Address(ipAddress) or is_A_Private_Class_B_Address(ipAddress)\
        or is_A_Private_Class_C_Address(ipAddress):
        return True
    else:
        # neither classes
        return False

"""Check if the address is within the range of private class A addresses"""
def is_A_Private_Class_A_Address(ipAddress):
    firstBlock = ipAddress[0]
    if firstBlock == '10':
        for i in range(1, 4):
            if int(ipAddress[i]) not in range(0, 256):
                return False
        return True

def is_A_Private_Class_B_Address(ipAddress):
    firstBlock = ipAddress[0]
    if firstBlock == '172':
        secondBlock = ipAddress[1]
        if int(secondBlock) not in range(16, 32):
            return False
        else:
            for i in range(2, 4):
                if int(ipAddress[i]) not in range(0, 256):
                    return False
        return True

def is_A_Private_Class_C_Address(ipAddress):
    firstBlock = ipAddress[0]
    secondBlock = ipAddress[1]
    if firstBlock == '192' and secondBlock == '168':
        for i in range(2, 4):
            if int(ipAddress[i]) not in range(0, 256):
                return False
        return True