import os
import tkinter as tk
from tkinter import *  # To Create An Actual Windows Application
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
from datetime import datetime

competition = []
nominees = []

main = Tk()  # Initializing the GUI (Graphical User Interface)
main.geometry("1366x768")  # Size of the App
main.title("Voting System")
# main.resizable(0, 0)

# add menu bar
menubar = Menu(main)
main.config(menu=menubar)

# create a menu
file_menu = Menu(menubar, tearoff=False)
exit_menu = Menu(menubar, tearoff=False)

conn = sqlite3.connect(
                r"C:\Users\user\Desktop\tic atelier\Voting System\public\db\voting.db")
cur = conn.cursor()
records = cur.execute('''SELECT * from competition''')
comp = cur.execute('''SELECT DISTINCT competition from competition''')

def list(a):
    w = []
    for i in a:
        w.append(i[0])
    return w

def add_to_database(comp, cat, e2, d2, top):
    sure = messagebox.askyesno(
        "Add to database", "Are you sure you want to add the records?", parent=top)
    if sure == True:
        for item in nominees:
            connect = sqlite3.connect(
                r"C:\Users\user\Desktop\tic atelier\Voting System\public\db\voting.db")
            cur = connect.cursor()
            cur.execute("INSERT INTO nominees(name, category, competition, begin_date) values(?,?,?,?)",
                        (item, cat, comp, datetime.now()))
            connect.commit()
            connect.close()
        nominees.clear()
        d2.delete("1.0", "end")
        e2.delete(0, END)
        messagebox.showinfo(
            "Success", "Competition Records Added Successfully")
        main.withdraw()
        os.system("python public/overviewSystem/viewRecords.py")
        main.destroy()


def add_nominees(e2, d2):
    entry = e2.get()
    nominees.append(entry)
    print(nominees)
    d2.delete("1.0", "end")
    for item in nominees:
        d2.insert(END, item + "\n")
        e2.delete(0, END)

def open_nom(comp, cat):
    top= Toplevel(main)
    top.geometry("800x400")
    top.title(comp + " ["+cat+"]")
    
    h3 = Label(top, text="Add Nominees")
    l2 = Label(top, text="Nominees Name: ")
    e2 = Entry(top, width=20)
    h4 = Label(top, text="View Added Nominees")
    d2 = Text(top, height=8, width=20)
    b4 = Button(top, text="Add to Database", command=lambda: add_to_database(comp, cat, e2, d2, top))
    b3 = Button(top, text="Add", command=lambda: add_nominees(e2, d2))

    # grid method to arrange labels in respective
    # rows and columns as specified
    h3.grid(row=0, column=0, sticky=W, pady=10)
    l2.grid(row=2, column=0, sticky=W, pady=0)
    e2.grid(row=2, column=1, pady=0, sticky=W)
    b3.grid(row=2, column=2, sticky=E, padx=5)

    # grid method to arrange labels in respective
    # rows and columns as specified
    h4.grid(row=4, column=0, sticky=W, pady=10)
    d2.grid(row=4, column=1, sticky=W, pady=10)
    b4.grid(row=7, column=2, sticky=E, pady=5)
    

def open_cat(comp):
    top= Toplevel(main)
    top.geometry("400x250")
    top.title(comp)
    conn2 = sqlite3.connect(
                r"C:\Users\user\Desktop\tic atelier\Voting System\public\db\voting.db")
    cur = conn2.cursor()
    cat = cur.execute('''SELECT DISTINCT category from competition WHERE competition=?''',(comp,))
    cat_val = list(cat)
    print(cat_val)
    
    h3 = Label(top, text="Select Category")
    h3.grid(row=0, column=0, sticky=W, pady=5)
    Lb1 = Listbox(top, height=4)
    j = 1
    for i in cat_val:
        Lb1.insert(j, i)
        j=j+1
    Lb1.grid(row=0, column=2, sticky=W, pady=5)
    b2 = ttk.Button(top, text="Next", command=lambda: open_nom(comp, Lb1.get(ANCHOR)))
    b2.grid(row=3, column=1, sticky=W, pady=5)

def open_popup(competition, categories):
   top= Toplevel(main)
   top.geometry("400x400")
   top.title("Add Nominees")
   Label(top, text= competition + categories, font=('Mistral 18 bold')).place(x=150,y=80)

def open_form():
    top= Toplevel(main)
    top.geometry("400x250")
    top.title("Add Nominees")
    conn2 = sqlite3.connect(
                r"C:\Users\user\Desktop\tic atelier\Voting System\public\db\voting.db")
    cur = conn2.cursor()
    comp = cur.execute('''SELECT DISTINCT competition from competition''')
    val = list(comp)
    
    h3 = Label(top, text="Select Competition")
    h3.grid(row=0, column=0, sticky=W, pady=5)
    Lb1 = Listbox(top, height=4)
    j = 1
    for i in val:
        Lb1.insert(j, i)
        j=j+1
    Lb1.grid(row=0, column=2, sticky=W, pady=5)
    b2 = ttk.Button(top, text="Next", command=lambda: open_cat(Lb1.get(ANCHOR)))
    b2.grid(row=3, column=1, sticky=W, pady=5)
    conn2.close()
# Exit The Application Function


def Exit():
    sure = messagebox.askyesno(
        "Exit", "Are you sure you want to leave?", parent=main)
    if sure == True:
        main.withdraw()
        # os.system("python public/overviewSystem/addCompetition.py")
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

conn = sqlite3.connect(
                r"C:\Users\user\Desktop\tic atelier\Voting System\public\db\voting.db")
cur = conn.cursor()
records = cur.execute('''SELECT * from competition''')

# Create View Competition Grid
h1 = Label(main, text="Competition")

# grid method to arrange labels in respective
# rows and columns as specified
h1.grid(row=0, column=0, sticky=W, pady=5)

# Create View Category Grid
h1 = Label(main, text="Category")

# grid method to arrange labels in respective
# rows and columns as specified
h1.grid(row=0, column=1, sticky=W, pady=5)

# Create View Nominees Grid
h1 = Label(main, text="Nominees")

# grid method to arrange labels in respective
# rows and columns as specified
h1.grid(row=0, column=2, sticky=W, pady=5)

b = ttk.Button(main, text="Add Nominee", command= open_form)
b.grid(row=0, column=3, sticky=W, pady=5)

i = 0 #initialize the rows

def nom_list(nom):
    nom_list = []
    st = ""
    if(nom != None):
        for item in nom:
            nom_list.append(item[1])
        st = ', '.join(nom_list)
    return st

for record in records:
    i = i + 1
    r = Label(main, text=record[2])
    r.grid(row=i, column=0, sticky=W, pady=5)
    r = Label(main, text=record[1])
    r.grid(row=i, column=1, sticky=W, pady=5)
    
    con = sqlite3.connect(
                r"C:\Users\user\Desktop\tic atelier\Voting System\public\db\voting.db")
    cur = con.cursor()
    nom = cur.execute('''SELECT * from nominees WHERE competition=? AND category=?''',(record[2], record[1],))
    st = nom_list(nom)
    r1 = Label(main, text=st)
    r1.grid(row=i, column=2, sticky=W, pady=5)
    con.close()
    
    
        



main.mainloop()
