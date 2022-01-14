from gui.screenUtils import EmptyRow
from tkinter import *


def labels(window):
    # Header
    Label(window, text="Welcome to Network Address Analyser", bg="light gray", bd=1,
          relief="sunken", font=("Helvetica", 22)).grid(row=1, column=1, sticky=N)

    EmptyRow(window)

    # Ip Address
    Label(window, text="IP Address :", bg="light gray", bd=1,
          font=("Helvetica", 22)).grid(row=4, column=1, sticky=W)

    EmptyRow(window)

    # Subnet Mask
    Label(window, text="Subnet Mask :", bg="light gray", bd=1,
          font=("Helvetica", 22)).grid(row=7, column=1, sticky=W)

    EmptyRow(window)

    # Network Address
    Label(window, text="Network Address :", bg="light gray", bd=1,
          font=("Helvetica", 22)).grid(row=10, column=1, sticky=W)

    EmptyRow(window)

    # First Address
    Label(window, text="First Address :", bg="light gray", bd=1,
          font=("Helvetica", 22)).grid(row=13, column=1, sticky=W)

    EmptyRow(window)

    # Last Address
    Label(window, text="Last Address :", bg="light gray", bd=1,
          font=("Helvetica", 22)).grid(row=16, column=1, sticky=W)

    EmptyRow(window)

    # Broadcast Address
    Label(window, text="Broadcast Address :", bg="light gray", bd=1,
          font=("Helvetica", 22)).grid(row=19, column=1, sticky=W)

    EmptyRow(window)

    # Report
    Label(window, text="Report :", bg="light gray", bd=1,
          font=("Helvetica", 22)).grid(row=22, column=1, sticky=W)
