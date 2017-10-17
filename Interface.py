# import all the py algorithms #

from tkinter import *
from CoinChange import *
from Knapsack import *
from Dijkstra import *
from Floyd import *
from HanoiTowers import *
from HeapSort import *
from MatrixProduct import *
from Quicksort import *
import CreateGraph as CG
from CreateGraph import*

control = Tk()

# You set the window title #
control.title('Algorithm Analize Project #1')

# Set the min & max values the window could have. #
control.minsize(width=800, height=600)
control.maxsize(width=3840, height=2160)

def raise_frame(fromFrame,toFrame):
    fromFrame.place(relx=-9, rely=-9, anchor = "center")
    toFrame.place(relx=0.5, rely=0.5, anchor = "center")

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
Label(informationFrame, text='Software created by\n'
                             'Brenes Maleaño Andrés Ottón.\n'
                             'Fernández Jiménez Axel Alejandro.\n'
                             'López Saborio Iván Móises.\n\n').pack(side = TOP, fill= X)
Label(informationFrame, text =
                             'Coin change: This algorithm consist in give you the minimum coins you need to give an exact ammount of money.\n\n'
                             'Knapsack: Given elements that have weight and a backpack to put them in. We give you\n'
                             'the most valuable backpack and the elements you have to put into.\n\n'
                             'Floyd: This algorithm finds the shortest path between one way to every other ways.\n\n'
                             'Dijkstra: Dijkstra gives you the shortest path between one way to another point.\n\n'
                             'Hanoi Towers: Given a N number of disks, move them from one tower to another one, by just moving\n'
                             'one disk at the time, consider that you can only put smaller disk on top.\n\n'
                             'Quicksort: Algorithm used to order an array of N number increasingly or decreasingly.\n\n'
                             'HeapSort: Algorithm used to order an array of N number increasingly or decreasingly.\n\n'
                             'Matrix Multiplication: Algorithm that given N matrices of mXn elements, it calculates the minimum\n'
                             'number of multiplications that have to be done using the best arrange of them associatively.\n\n').pack(side=TOP, fill= X)
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
Label(coinFrame, text='Coin Change Algorithm\n', font = 20).pack()
Label(coinFrame, text='Insert the coin quantity:\n').pack()
coinQuantity = Entry(coinFrame, text = "Insert how many coins do you have")
coinQuantity.pack(side = TOP, fill = X)
Label(coinFrame, text='Insert the total value you want to achieve:\n').pack()
changeInput = Entry(coinFrame)
changeInput.pack(side = TOP, fill = X)
Button(coinFrame, text='Execute', command=lambda:setCoinValues()).pack(side=TOP, fill=X)
def setCoinValues():
    def clearFrame():
        result.destroy()
        cButton.destroy()
    result = Label(coinFrame, text = coinChange(int(coinQuantity.get()),int(changeInput.get())))
    result.pack()
    cButton = Button(coinFrame, text='Clear', command=lambda:clearFrame())
    cButton.pack(side=BOTTOM, fill=X)
Button(coinFrame, text='Back', command=lambda:raise_frame(coinFrame, algorithmFrame)).pack(side=BOTTOM, fill=X)


# knapsackFrame #
Label(knapsackFrame, text='Knapsack Algorithm.\n', font = 20).pack()
Label(knapsackFrame, text='Insert how many products do you own:\n').pack()
cantKnapsack = Entry(knapsackFrame)
cantKnapsack.pack(side = TOP, fill = X)
Label(knapsackFrame, text='Insert the weight the backpack can hold:\n').pack()
weightKnapsack = Entry(knapsackFrame)
weightKnapsack.pack(side = TOP, fill = X)

Button(knapsackFrame, text='Execute', command=lambda:setKnapsackValues()).pack(side=TOP, fill=X)
def setKnapsackValues():
    def clearFrame():
        result.destroy()
        cButton.destroy()
    result = Label(knapsackFrame, text = knapsack(int(cantKnapsack.get()),int(weightKnapsack.get())))
    result.pack()
    cButton = Button(knapsackFrame, text='Clear', command=lambda:clearFrame())
    cButton.pack(side=BOTTOM, fill=X)

Button(knapsackFrame, text='Back', command=lambda:raise_frame(knapsackFrame, algorithmFrame)).pack(side=BOTTOM, fill=X)


# shortestpathFrame #
Label(shortestpathFrame, text='Choose between Floyd & Dijkstra.\n').pack()
Button(shortestpathFrame, text='Floyd', command=lambda:raise_frame(shortestpathFrame, floydFrame)).pack(side=TOP, fill=X)
Button(shortestpathFrame, text='Dijkstra', command=lambda:raise_frame(shortestpathFrame, dijkstraFrame)).pack(side=TOP, fill=X)
Button(shortestpathFrame, text='Back', command=lambda:raise_frame(shortestpathFrame, algorithmFrame)).pack(side=TOP, fill=X)

# floydFrame #
Label(floydFrame, text='Floyd.\n', font = 20).pack()
Label(floydFrame, text='Insert how many nodes do you want:\n').pack()
nodesFloyd = Entry(floydFrame)
nodesFloyd.pack(side = TOP, fill = X)
Button(floydFrame, text='Execute', command=lambda:setFloydValues()).pack(side=TOP, fill=X)
def setFloydValues():
    graph = int(nodesFloyd.get())
    graph = creategraph(graph)
    graph = graphtomatrix(graph)
    def clearFrame():
        result.destroy()
        cButton.destroy()
    result = Label(floydFrame, text = floyd(graph))
    result.pack()
    cButton = Button(floydFrame, text='Clear', command=lambda:clearFrame())
    cButton.pack(side=BOTTOM, fill=X)
Button(floydFrame, text='Back', command=lambda:raise_frame(floydFrame, shortestpathFrame)).pack(side=BOTTOM, fill=X)

# dijkstraFrame #
Label(dijkstraFrame, text='Dijkstra.\n', font = 20).pack()
Label(dijkstraFrame, text='Insert how many nodes do you want:\n').pack()
nodesDijkstra = Entry(dijkstraFrame)
nodesDijkstra.pack(side = TOP, fill = X)
Label(dijkstraFrame, text='Insert the node you want to start from:\n').pack()
initDijkstra = Entry(dijkstraFrame)
initDijkstra.pack(side = TOP, fill = X)
Button(dijkstraFrame, text='Execute', command=lambda:setDijkstraValues()).pack(side=TOP, fill=X)
def setDijkstraValues():
    node,distance = creategraph(int(nodesDijkstra.get()))
    def clearFrame():
        result.destroy()
        cButton.destroy()
    result = Label(dijkstraFrame, text = dijkstra(node, int(initDijkstra.get()), distance))
    result.pack()
    cButton = Button(dijkstraFrame, text='Clear', command=lambda:clearFrame())
    cButton.pack(side=BOTTOM, fill=X)
Button(dijkstraFrame, text='Back', command=lambda:raise_frame(dijkstraFrame, shortestpathFrame)).pack(side=BOTTOM, fill=X)


# hanoiFrame #
Label(hanoiFrame, text='Hanoi Towers.\n', font = 20).pack()
Label(hanoiFrame, text='Insert the towers height:\n').pack()
heightHanoi = Entry(hanoiFrame)
heightHanoi.pack(side = TOP, fill = X)
Button(hanoiFrame, text='Back', command=lambda:raise_frame(hanoiFrame, algorithmFrame)).pack(side=BOTTOM, fill=X)


# sortFrame #
Label(sortFrame, text='Choose between QuickSort & HeapSort.\n').pack()
Button(sortFrame, text='QuickSort', command=lambda:raise_frame(sortFrame, quickFrame)).pack(side=TOP, fill=X)
Button(sortFrame, text='HeapSort', command=lambda:raise_frame(sortFrame, heapFrame)).pack(side=TOP, fill=X)
Button(sortFrame, text='Back', command=lambda:raise_frame(sortFrame, algorithmFrame)).pack(side=BOTTOM, fill=X)

# quickSortFrame #
Label(quickFrame, text='QuickSort.\n', font = 20).pack()
Label(quickFrame, text='Insert how long the array should be:\n').pack()
lenQuicksort = Entry(quickFrame)
lenQuicksort.pack(side = TOP, fill = X)
Button(quickFrame, text='Back', command=lambda:raise_frame(quickFrame, sortFrame)).pack(side=BOTTOM, fill=X)

# heapSortFrame #
Label(heapFrame, text='Choose max or min.\n').pack()
Button(heapFrame, text='Maximum Heap', command=lambda:raise_frame(heapFrame, heapMaxFrame)).pack(side=TOP, fill=X)
Button(heapFrame, text='Minimum Heap', command=lambda:raise_frame(heapFrame, heapMinFrame)).pack(side=TOP, fill=X)
Button(heapFrame, text='Back', command=lambda:raise_frame(heapFrame, sortFrame)).pack(side=BOTTOM, fill=X)

# heapMaxFrame #
Label(heapMaxFrame, text='Maximum Heap.\n', font = 20).pack()
Label(heapMaxFrame, text='Insert how long the array should be:\n').pack()
lenHeapMax = Entry(heapMaxFrame)
lenHeapMax.pack(side = TOP, fill = X)
Button(heapMaxFrame, text='Back', command=lambda:raise_frame(heapMaxFrame, heapFrame)).pack(side=BOTTOM, fill=X)

# heapMinFrame #
Label(heapMinFrame, text='Minimum Heap.\n', font = 20).pack()
Label(heapMinFrame, text='Insert how long the array should be:\n').pack()
lenHeapMin = Entry(heapMinFrame)
lenHeapMin.pack(side = TOP, fill = X)
Button(heapMinFrame, text='Back', command=lambda:raise_frame(heapMinFrame, heapFra/me)).pack(side=BOTTOM, fill=X)


# matrixFrame #
Label(matrixFrame, text='N-Matrix Chain Product.\n', font = 20).pack()
Label(matrixFrame, text='Insert how many matrix do you want:\n').pack()
valueMatrix = Entry(matrixFrame)
valueMatrix.pack(side = TOP, fill = X)
Button(matrixFrame, text='Back', command=lambda:raise_frame(matrixFrame, algorithmFrame)).pack(side=BOTTOM, fill=X)


raise_frame(mainFrame,mainFrame)
control.mainloop()