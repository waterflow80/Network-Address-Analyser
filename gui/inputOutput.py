from gui.screenUtils import EmptyRow
from tkinter import *

# Input the IP Address from the user
def inputIpAddress(window,ipAddress):
    Entry(window, textvariable=ipAddress, bg="light gray", justify=CENTER).grid(row=4, column=2, padx=(0, 5))

# Input the Subnet Mask from the user
def inputSubnetMask(window, subnetMask):
    Entry(window, textvariable=subnetMask, bg="light gray", justify=CENTER).grid(row=7, column=2, padx=(0, 5))

# Display the network address (after calculating it)
def displayNetworkAddress(window, networkAddress):
    Label(window, textvariable=networkAddress, bg="light gray", bd=1,
          relief="sunken", font=("Helvetica", 22)).grid(row=10, column=2, sticky=N)

# Display the First Address (after calculating it)
def displayFirstAddress(window, firstAddress):
    Label(window, textvariable=firstAddress, bg="light gray", bd=1,
          relief="sunken", font=("Helvetica", 22)).grid(row=13, column=2, sticky=N)

# Display the Last Address (after calculating it)
def displayLastAddress(window, lastAddress):
    Label(window, textvariable=lastAddress, bg="light gray", bd=1,
          relief="sunken", font=("Helvetica", 22)).grid(row=16, column=2, sticky=N)

# Display the Broadcast Address (after calculating it)
def displayBroadcastAddress(window, broadcastAddress):
    Label(window, textvariable=broadcastAddress, bg="light gray", bd=1,
          relief="sunken", font=("Helvetica", 22)).grid(row=19, column=2, sticky=N)

# Display the report (in case of an error)
def displayReport(window, report):
    Label(window, textvariable=report, bg="light gray", bd=1,
          relief="sunken", font=("Helvetica", 22)).grid(row=22, column=2, sticky=N)