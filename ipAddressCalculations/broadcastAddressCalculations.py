from digitalElectronics.tools import *

"""Calculate the broadcast address for the given network adddress"""
def calculateBroadcasAddress(networkAddress: str, subnetMask: str)->str:
    subnetMaskBinary = convertlistDecimalsToBinary(subnetMask.split('.'))  # the binary sequence of the subnet mask
    networkAddressBinary = convertlistDecimalsToBinary(networkAddress.split('.'))  # the binary sequence of the ip address
    networkAddressLength = subnetMaskBinary.count('1')  # the number of '1' in the mask
    machineAddressLength = 32 - networkAddressLength  # the length of the machine address part in terms of number of bits
    biggestBinaryNumber = getBiggestNumberBinary(machineAddressLength)  # get the biggest number that can be formed with the number of digits of the machine part
    networkAddressPartOnly = networkAddressBinary[:networkAddressLength]
    broadcastAddressBinary = networkAddressPartOnly + biggestBinaryNumber  # making the address in its biggest binary sequence number
    broadcastAddressDecimalBlocks = binary32ToDecimal(broadcastAddressBinary)
    broadcastAddressFinalFormat = '.'.join(broadcastAddressDecimalBlocks)  # getting the final format of the address
    return broadcastAddressFinalFormat
