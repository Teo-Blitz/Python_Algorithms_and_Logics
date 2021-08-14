#coding:UTF-8
#Beginner Calculator with Tkinter - Mateus Páscoa

from tkinter import Tk, Button, Label, StringVar, Entry, Frame

#Functions
def returnSum():
    valueOne = int(valueOneUser.get())
    valueTwo = int(valueTwoUser.get())
    resultOperation.set(valueOne + valueTwo)

def returnDecrease():
    valueOne = int(valueOneUser.get())
    valueTwo = int(valueTwoUser.get())
    resultOperation.set(valueOne - valueTwo)

def returnMultiply():
    valueOne = int(valueOneUser.get())
    valueTwo = int(valueTwoUser.get())
    resultOperation.set(valueOne * valueTwo)

def returnDivide():
    valueOne = int(valueOneUser.get())
    valueTwo = int(valueTwoUser.get())
    resultOperation.set(round((valueOne / valueTwo), 4))

#GUI
appCalculator = Tk()
appCalculator.title('Calculator')
appCalculator.geometry('600x600')

#VariablesToComputation
resultOperation = StringVar()

#Widgets
frameCalculator = Frame(appCalculator)

labelTitleValueOneUser = Label(frameCalculator,
                               font = 'Arial 15',
                               text = 'Insert the first value:')

labelTitleValueTwoUser = Label(frameCalculator,
                               font = 'Arial 15',
                               text = 'Insert the second value:')

labelResultValue = Label(frameCalculator,
                         font = 'Arial 20',
                         bd = '5', relief = 'ridge', width = 10,
                         textvariable = resultOperation)

labelMessage = Label(frameCalculator,
                     font = 'Arial 15',
                     text = 'This is the result:')

buttonReturnSum = Button(frameCalculator,
                         text = 'Sum',
                         padx = 10, pady = 10, width = 20,
                         command = returnSum)

buttonReturnDecrease = Button(frameCalculator,
                              text = 'Decrease',
                              padx = 10, pady = 10, width = 20,
                              command = returnDecrease)

buttonReturnMultiply = Button(frameCalculator,
                              text = 'Multiply',
                              padx = 10, pady = 10, width = 20,
                              command = returnMultiply)

buttonReturnDivide = Button(frameCalculator,
                            text = 'Divide',
                            padx = 10, pady = 10, width = 20,
                            command = returnDivide)

valueOneUser = Entry(frameCalculator)
valueTwoUser = Entry(frameCalculator)

#Layouts
labelTitleValueOneUser.pack()
valueOneUser.pack()

labelTitleValueTwoUser.pack()
valueTwoUser.pack()

buttonReturnSum.pack()
buttonReturnDecrease.pack()
buttonReturnMultiply.pack()
buttonReturnDivide.pack()

labelMessage.pack()
labelResultValue.pack()

frameCalculator.pack()

valueOneUser.focus()

#FinalProgram
appCalculator.mainloop()
