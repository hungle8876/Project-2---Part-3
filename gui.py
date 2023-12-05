# Khanh Nguyen
# Van Hung Le
# Phu Truong
# CSE-3330 Project 2
# December 5th, 2023


from tkinter import *
import sqlite3
from PIL import ImageTk

# Define function for all button
def check_out():
    db_conn = sqlite3.connect('main.db')
    return 0

def new_borrower():
    return 0

def new_book():
    return 0

def book_search():
    return 0

def late_list():
    return 0






# Create GUI
root = Tk()
root.title('Library Management System')
root.geometry("500x600")
root.configure(bg="#a8ceff")
root.pack_propagate(False)


library_system_connect = sqlite3.connect('main.db')
library_system_cyr = library_system_connect.cursor()

system_logo = ImageTk.PhotoImage(file="lms_logo.png")
logo_widget = Label(root, image=system_logo, font=20, bg="#a8ceff")
logo_widget.image = system_logo
logo_widget.pack()
logo_widget.grid(row=0, column=0, columnspan=2, pady=0)
title = Label(root, text="Library Management System", font=10, bg="#a8ceff", fg='black')
title.grid(row=1, column=0, columnspan=2, pady=10, padx=100)


#1  Check out new book loan
check_out_btn = Button(root, text='Check Out', command=check_out, width=20, fg='black')
check_out_btn.grid(row=2, column=0, columnspan=2,pady=10, padx=100)

#2  Add new member into Borrower
new_borrower_btn = Button(root, text='New Member', command=new_borrower, width=20, fg='black')
new_borrower_btn.grid(row=3, column=0, columnspan=2,pady=10, padx=100)

#3  Add new book into all 5 branches, 5 copies each branch
new_book_btn = Button(root, text='New Book', command=new_book, width=20, fg='black')
new_book_btn.grid(row=4, column=0, columnspan=2,pady=10, padx=100)

#4  List the copies that are being loaned by the book title
book_search_btn = Button(root, text='Search Book', command=book_search, width=20, fg='black')
book_search_btn.grid(row=5, column=0, columnspan=2,pady=10, padx=100)

#5  List late returned from book_loans by a given date
late_list_btn = Button(root, text='Late List', command=late_list, width=20, fg='black')
late_list_btn.grid(row=6, column=0, columnspan=2,pady=10, padx=100)



root.mainloop()