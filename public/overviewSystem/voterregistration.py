import os
from tkinter import *  # To Create An Actual Windows Application
from tkinter import messagebox

main = Tk()  # Initializing the GUI (Graphical User Interface)
main.geometry("1366x768")  # Size of the App
main.title("Voting System")
# main.resizable(0, 0)

name = StringVar()
student_class = StringVar()
student_regno = StringVar()

# Exit The Application Function


def Exit():
    sure = messagebox.askyesno(
        "Exit", "Are you sure you want to leave?", parent=main)
    if sure == True:
        main.destroy()


main.protocol("WM_DELETE_WINDOW", Exit)


main.mainloop()
