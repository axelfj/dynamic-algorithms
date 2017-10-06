from tkinter import *
from tkinter import ttk

main = Tk()

# You set the window title #
main.title('Algorithm Analize Project #1')

# Set the min & max values the window could have. #
main.minsize(width=800, height=600)
main.maxsize(width=3840, height=2160)

# Set the background black #
#control.configure(background = '#40E0D0')
frame = Frame()
# All the control Buttons #
continueButton = Button(text = 'Continue')
continueButton.place(relx = 0.5, rely = 0.4, anchor = CENTER)
helpButton = Button(text = 'Information')
helpButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)
exitButton = Button(text = 'Exit')
exitButton.place(relx = 0.5, rely = 0.6, anchor = CENTER)

# This shows the mainWindow #
main.mainloop()
