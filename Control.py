from tkinter import *
from tkinter import ttk

control = Tk()

# You set the window title #
control.title('Algorithm Analize Project #1')

# Set the min & max values the window could have. #
control.minsize(width=800,height=600)
control.maxsize(width=3840,height=2160)

# Set the background black #
#control.configure(background = '#40E0D0')

# Create the main Screen #

# All the control Buttons #
continueButton = Button(text = 'Continue')
continueButton.place(anchor = height/2)

helpButton = Button(text = 'Information')
helpButton.place(relx = 0, rely = 0, anchor = CENTER)

exitButton = Button(text = 'Exit')
exitButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

# This shows the window #
control.mainloop()