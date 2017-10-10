# import all the py algorithms #

from Backpack_Problem import *
from Coin_Change import *
from Dijkstra import *
from Floyd import *
from HanoiTowers import *
from HeapSort import *
from MatrixProduct import *
from Quicksort import *


# import the interface library #

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
    fromFrame.place(relx=-0.4, rely=-0.4)
    if toFrame == algorithmFrame or toFrame == shortestpathFrame or toFrame == sortFrame:
        toFrame.place(relx = 0.4, rely = 0.3)
    else:
        toFrame.place(relx=0.4, rely=0.4)


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
Button(mainFrame, text='Exit', command=lambda:control.quit()).pack(side=TOP, fill=X)
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


# coinFrame # CON ERRORES
Label(coinFrame, text='Insert the coin quantity:\n').pack()
coinQuantity = Entry(coinFrame).pack()
Label(coinFrame, text='Insert the coins values:\n').pack()
coinWeights = Entry(coinFrame).pack()
Label(coinFrame, text='Insert the total value you want to achieve:\n').pack()
totalInput = Entry(coinFrame).pack()
Button(coinFrame, text='Execute', command=lambda:print(change(getint(coinQuantity),getint(totalInput)))).pack(side=TOP, fill=X)
Button(coinFrame, text='Back', command=lambda:raise_frame(coinFrame, algorithmFrame)).pack(side=TOP, fill=X)


# knapsackFrame #
Label(knapsackFrame, text='This is a test.\n').pack()
Button(knapsackFrame, text='Back', command=lambda:raise_frame(knapsackFrame, algorithmFrame)).pack(side=TOP, fill=X)


# shortestpathFrame #
Label(shortestpathFrame, text='Choose between Floyd & Dijkstra.\n').pack()
Button(shortestpathFrame, text='Floyd', command=lambda:raise_frame(shortestpathFrame, floydFrame)).pack(side=TOP, fill=X)
Button(shortestpathFrame, text='Dijkstra', command=lambda:raise_frame(shortestpathFrame, dijkstraFrame)).pack(side=TOP, fill=X)
Button(shortestpathFrame, text='Back', command=lambda:raise_frame(shortestpathFrame, algorithmFrame)).pack(side=TOP, fill=X)

# floydFrame #
Label(floydFrame, text='Floyd.\n').pack()
Button(floydFrame, text='Back', command=lambda:raise_frame(floydFrame, shortestpathFrame)).pack(side=TOP, fill=X)

# dijkstraFrame #
Label(dijkstraFrame, text='Dijkstra.\n').pack()
Button(dijkstraFrame, text='Back', command=lambda:raise_frame(dijkstraFrame, shortestpathFrame)).pack(side=TOP, fill=X)


# hanoiFrame #
Label(hanoiFrame, text='This is a test.\n').pack()
Button(hanoiFrame, text='Back', command=lambda:raise_frame(hanoiFrame, algorithmFrame)).pack(side=TOP, fill=X)


# sortFrame #
Label(sortFrame, text='Choose between QuickSort & HeapSort.\n').pack()
Button(sortFrame, text='QuickSort', command=lambda:raise_frame(sortFrame, quickFrame)).pack(side=TOP, fill=X)
Button(sortFrame, text='HeapSort', command=lambda:raise_frame(sortFrame, heapFrame)).pack(side=TOP, fill=X)
Button(sortFrame, text='Back', command=lambda:raise_frame(sortFrame, algorithmFrame)).pack(side=TOP, fill=X)

# quickSortFrame #
Label(quickFrame, text='This is quicksort.\n').pack()
Button(quickFrame, text='Back', command=lambda:raise_frame(quickFrame, sortFrame)).pack(side=TOP, fill=X)

# heapSortFrame #
Label(heapFrame, text='Choose max or min.\n').pack()
Button(heapFrame, text='Max Heap', command=lambda:raise_frame(heapFrame, heapMaxFrame)).pack(side=TOP, fill=X)
Button(heapFrame, text='Min Heap', command=lambda:raise_frame(heapFrame, heapMinFrame)).pack(side=TOP, fill=X)
Button(heapFrame, text='Back', command=lambda:raise_frame(heapFrame, sortFrame)).pack(side=TOP, fill=X)

# heapMaxFrame #
Label(heapMaxFrame, text='HeapMax.\n').pack()
Button(heapMaxFrame, text='Back', command=lambda:raise_frame(heapMaxFrame, heapFrame)).pack(side=TOP, fill=X)

# heapMinFrame #
Label(heapMinFrame, text='HeapMin.\n').pack()
Button(heapMinFrame, text='Back', command=lambda:raise_frame(heapMinFrame, heapFrame)).pack(side=TOP, fill=X)


# matrixFrame #
Label(matrixFrame, text='This is a test.\n').pack()
Button(matrixFrame, text='Back', command=lambda:raise_frame(matrixFrame, algorithmFrame)).pack(side=TOP, fill=X)


raise_frame(mainFrame,mainFrame)
control.mainloop()