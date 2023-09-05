import os
from tkinter import *  # To Create An Actual Windows Application
from tkinter import messagebox

main = Tk()  # Initializing the GUI (Graphical User Interface)
main.geometry("1366x768")  # Size of the App
main.title("Voting System")
# main.resizable(0, 0)

# add menu bar
menubar = Menu(main)
main.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
exit_menu = Menu(menubar)


# Exit The Application Function


def Exit():
    sure = messagebox.askyesno(
        "Exit", "Are you sure you want to leave?", parent=main)
    if sure == True:
        main.destroy()


main.protocol("WM_DELETE_WINDOW", Exit)

# add a menu item to the menu
exit_menu.add_command(
    label='Exit',
    command=Exit
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)

menubar.add_cascade(
    label="Exit",
    menu=exit_menu
)



main.mainloop()
