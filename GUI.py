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

mainFrame = Frame(control)
algorithmFrame = Frame(control)
informationFrame = Frame(control)

# MainFrame #
Label(mainFrame, text='Welcome to our program.').pack()
Button(mainFrame, text='Continue to the algorithms', command=lambda:raise_frame(mainFrame,algorithmFrame)).pack(side=TOP, fill=X)
Button(mainFrame, text='Information', command=lambda:raise_frame(mainFrame, informationFrame)).pack(side=TOP, fill=X)
Button(mainFrame, text='Exit', command=lambda:exit_frame()).pack(side=TOP, fill=X)
Label(mainFrame, text='Thank you for using our program.').pack()

# HelpFrame #
Label(informationFrame, text='Thanks for using our program.').pack()
Button(informationFrame, text='Back', command=lambda:raise_frame(informationFrame, mainFrame)).pack()


raise_frame(mainFrame,mainFrame)
control.mainloop()