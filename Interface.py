from tkinter import *
from tkinter import ttk

control = Tk()

# You set the window title #
control.title('Algorithm Analize Project #1')

# Set the min & max values the window could have. #
control.minsize(width=800, height=600)
control.maxsize(width=800, height=600)

# Set the background black #
#control.configure(background = 'black')

def raise_frame(fromFrame,toFrame):
    fromFrame.place(relx = -0.4, rely = -0.4)
    toFrame.place(relx = 0.4, rely = 0.4)

def exit_frame():
    control.quit()

# First Frames #
mainFrame = Frame(control)
algorithmFrame = Frame(control)
informationFrame = Frame(control)

# Second Frames #
coinFrame = Frame(control)
knapsackFrame = Frame(control)
shortestpathFrame = Frame(control)
hanoiFrame = Frame(control)
sortFrame = Frame(control)
matrixFrame = Frame(control)

# Third Frames #
floydFrame = Frame(control)
dijkstraFrame = Frame(control)
heapFrame = Frame(control)
quickFrame = Frame(control)

# Fourth Frames #
heapMaxFrame = Frame(control)
heapMinFrame = Frame(control)

# MainFrame #
Label(mainFrame, text='Welcome to our program.').pack()
Button(mainFrame, text='Continue to the algorithms', command=lambda:raise_frame(mainFrame,algorithmFrame)).pack(side=TOP, fill=X)
Button(mainFrame, text='Information', command=lambda:raise_frame(mainFrame, informationFrame)).pack(side=TOP, fill=X)
Button(mainFrame, text='Exit', command=lambda:exit_frame()).pack(side=TOP, fill=X)
Label(mainFrame, text='Thank you for using our program.').pack()

# HelpFrame #
Label(informationFrame, text='Program created by\n'
                             'Brenes Maleaño Andrés Ottón.\n'
                             'Fernández Jiménez Axel Alejandro.\n'
                             'López Saborio Iván Móises.\n').pack(side = TOP, fill= X)
Button(informationFrame, text='Back', command=lambda:raise_frame(informationFrame, mainFrame)).pack(side=TOP, fill=X)

# AlgorithmFrame #
Label(algorithmFrame, text='Choose your favorite algorithm.').pack()
Button(algorithmFrame, text='Coin Change', command=lambda:raise_frame(algorithmFrame,coinFrame)).pack(side=TOP, fill=X)
Button(algorithmFrame, text='Knapsack', command=lambda:raise_frame(algorithmFrame, knapsackFrame)).pack(side=TOP, fill=X)
Button(algorithmFrame, text='Shortest Path', command=lambda:raise_frame(algorithmFrame,shortestpathFrame)).pack(side=TOP, fill=X)
Button(algorithmFrame, text='Hanoi Towers', command=lambda:raise_frame(algorithmFrame,hanoiFrame)).pack(side=TOP, fill=X)
Button(algorithmFrame, text='Sort Algorithms', command=lambda:raise_frame(algorithmFrame, sortFrame)).pack(side=TOP, fill=X)
Button(algorithmFrame, text='N-Matrix Product', command=lambda:raise_frame(algorithmFrame, matrixFrame)).pack(side=TOP, fill=X)
Button(algorithmFrame, text='Back', command=lambda:raise_frame(algorithmFrame, mainFrame)).pack(side=TOP, fill=X)

# coinFrame #
Label(coinFrame, text='This is the coin change algorithm.\n'
                      'You need to say how much coins you have & the value of each.\n'
                      '').pack()

# knapsackFrame #

# shortestpathFrame #

# hanoiFrame #

# sortFrame #

# matrixFrame #

raise_frame(mainFrame,mainFrame)
control.mainloop()