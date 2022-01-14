from digitalElectronics.tools import *

"""Return the network address of the given ip address that match the subnet mask"""
def calculateNetworkAddress(ipAddress: str, subnetMask: str):
    ipAddressBlocks = ipAddress.split('.')  # get the four blocks of the ip address
    subnetMaskBlocks = subnetMask.split('.')  # get the four blocks of the subnet mask
    ipAddressBinary = convertlistDecimalsToBinary(ipAddressBlocks)  # the binary equivalent of the ip address
    subnetMaskBinary = convertlistDecimalsToBinary(subnetMaskBlocks)  # the binary equivalent of the subnet mask
    netwrokAddressBinary = binarySum(ipAddressBinary, subnetMaskBinary)  # make binary sum of the ip adddress and the subnet mask
    networkAddressBlocks = binary32ToDecimal(netwrokAddressBinary)  # the network address in the form of a list of blocks
    networkAddress = '.'.join(networkAddressBlocks)  # get the network address in the final format (xxx.xxx.xxx.xxx)
    return networkAddress