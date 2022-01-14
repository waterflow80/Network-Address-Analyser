from tkinter import Label

class EmptyRow:
    index1 = 2  # the index of the row to be left
    index2 = 3  # the index of the row to be left
    def __init__(self, window):
        Label(window, text=None).grid(row=EmptyRow.index1, column=1)
        Label(window, text=None).grid(row=EmptyRow.index2, column=1)
        EmptyRow.index1 += 3  # going to the next row to be left
        EmptyRow.index2 += 3

