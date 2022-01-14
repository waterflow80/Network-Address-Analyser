"""Calculate the last address in the network, knowing the broadcast address"""
def calculateLastAddress(broadcastAddress:str):
    networkAddressBlocks = broadcastAddress.split('.')  # get each block aside
    networkAddressBlocks[3] = str(int(networkAddressBlocks[3]) - 1)  # decrementing one to the broadcast address
    if int(networkAddressBlocks[3]) > 255:
        return False
    firstAddress = '.'.join(networkAddressBlocks)  # getting the initial format of the ip address
    return firstAddress