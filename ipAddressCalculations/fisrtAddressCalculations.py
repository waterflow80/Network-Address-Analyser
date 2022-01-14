"""calculate the fisrt ip address that corresponds to the given network address"""
def caluclateFirstAddress(networkAddress: str)->str:
    networkAddressBlocks = networkAddress.split('.')  # get each block aside
    networkAddressBlocks[3] = str(int(networkAddressBlocks[3]) + 1)  # incrementing one after the network address
    if int(networkAddressBlocks[3]) > 255:
        return False
    firstAddress = '.'.join(networkAddressBlocks)  # getting the initial format of the ip address
    return firstAddress