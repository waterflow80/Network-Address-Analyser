import re
from networking.utils import *
"""Check if the mask entered is a valid subnet mask"""
def checkSubnetMask(subnetMask, ipAddress):
    subnetMask = str(subnetMask)
    if subnetMask.count('.') != 3:
        return False
    if not re.match('[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}$', subnetMask):
        return False
    subnetMaskBlocks = subnetMask.split('.')  # ['xxx','xxx','xxx','xxx']
    if not isValidSubnetMask(subnetMaskBlocks):
        return False
    ipAddressClass = getPrivateIpAddressClass(ipAddress)
    print(ipAddressClass)
    maskIsSuitable = subnetMaskSuitableForIpAddress(subnetMask, ipAddressClass) # Checking if the mask is suitable for the private ipAddress entered
    if not maskIsSuitable:
        return False
    return True



