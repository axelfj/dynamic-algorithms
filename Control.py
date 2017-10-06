from tkinter import *
from tkinter import ttk

control = Tk()

# You set the window title #
control.title('Algorithm Analize Project #1')

# Set the min & max values the window could have. #
control.minsize(width=800, height=600)
control.maxsize(width=800, height=600)

# Set the background black #
#control.configure(background = '#40E0D0')

def raise_frame(fromFrame,toFrame):
    fromFrame.place(relx = -0.5, rely = -0.5)
    toFrame.place(relx = 0.5, rely = 0.5)

def exit_frame():
    control.quit()

mainFrame = Frame(control)
algorithmFrame = Frame(control)
helpFrame = Frame(control)

Button(mainFrame, text='Continue to the algorithms', command=lambda:raise_frame(mainFrame,algorithmFrame)).pack()
Button(mainFrame, text='Information', command=lambda:raise_frame(mainFrame,helpFrame)).pack()
Button(mainFrame, text='Exit', command=lambda:exit_frame()).pack()
Label(mainFrame, text='Thanks for using our program.').pack()


raise_frame(mainFrame,mainFrame        )
