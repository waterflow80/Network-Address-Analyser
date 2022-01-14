from tkinter import Button

"""The submit button to calculate the IP Adress information"""
def submitButton(window, textField, submitFunction):
    #Submit
    Button(window, text=textField,command=submitFunction,font="Helvetica 14")\
        .grid(row=25,column=3, padx= (100,5), pady=5)

"""Clearing all the fields (set them to empty strings"""
def clearFieldsButton(window, textField, clearFieldsFunction):
    Button(window, text=textField, command=clearFieldsFunction, font="Helvetica 14")\
        .grid(row=25, column=1,padx=(100, 5), pady=5)

