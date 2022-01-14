from tkinter import *
from gui.labels import labels
from gui.inputOutput import *
from gui.buttons import *
from informationChecker.privateIpAddressChecker import *
from informationChecker.subnetMaskChecker import *
from ipAddressCalculations.networkAddressCalculations import *
from ipAddressCalculations.fisrtAddressCalculations import *
from ipAddressCalculations.lastAddressCalculations import *
from ipAddressCalculations.broadcastAddressCalculations import *

class NetworkAddressAnalyser:
    def __init__(self):
        window = Tk()
        window.title("Network Address Analayser")  # title of the app

        # Input Variables
        self.ipAddress = StringVar(window, value="")
        self.subnetMask = StringVar(window, value="")

        # Output Variables (Network Address information && report)
        self.networkAddress = StringVar(window, value="")
        self.firstAddress = StringVar(window, value="")
        self.lastAddress = StringVar(window, value="")
        self.broadcastAddress = StringVar(window, value="")
        self.report = StringVar(window, value="")


        # Display labels (instructions)
        labels(window)

        # Inputs
        inputIpAddress(window,self.ipAddress)
        inputSubnetMask(window, self.subnetMask)

        # Network Address Information Output
        displayNetworkAddress(window, self.networkAddress)
        displayFirstAddress(window, self.firstAddress)
        displayLastAddress(window, self.lastAddress)
        displayBroadcastAddress(window, self.broadcastAddress)

        # Report Output
        displayReport(window, self.report)

        # Buttons
        submitButton(window, "Start",self.determineNetworkInfo)
        clearFieldsButton(window, "Clear", self.clearAllFields)


        # displaying the screen
        window.mainloop()

    def determineNetworkInfo(self):
        ipAddress = self.ipAddress.get()
        valid_ip_address = checkPrivateIpAddress(ipAddress)  # (true or false)
        if not valid_ip_address:
            self.report.set("Please enter a valid PRIVATE ip address")
        else:
            # self.report.set(" valid ip address")
            subnetMask = self.subnetMask.get()
            valid_subnet_mask = checkSubnetMask(subnetMask, ipAddress)
            if not valid_subnet_mask:
                self.report.set("Incorrect Subnet Mask")
            else:  # all inputs are now correct, lets start the calculations
                networkAddress = calculateNetworkAddress(ipAddress, subnetMask)
                firstAddress = caluclateFirstAddress(networkAddress)
                broadcastAddress = calculateBroadcasAddress(ipAddress, subnetMask)
                lastAddress = calculateLastAddress(broadcastAddress)
                self.lastAddress.set(lastAddress)
                self.broadcastAddress.set(broadcastAddress)
                self.networkAddress.set(networkAddress)
                self.firstAddress.set(firstAddress)
                self.report.set("FINISHED")

    """Set all fields to empty strings"""
    def clearAllFields(self):
        self.ipAddress.set("")
        self.subnetMask.set("")
        self.networkAddress.set("")
        self.firstAddress.set("")
        self.lastAddress.set("")
        self.broadcastAddress.set("")
        self.report.set("")

# Application Runner
NetworkAddressAnalyser()