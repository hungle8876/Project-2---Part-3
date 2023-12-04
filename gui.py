# Khanh Nguyen
# Van Hung Le
# Phu Truong
# CSE-3330 Project 2
# December 5th, 2023


from tkinter import *
import sqlite3
from PIL import ImageTk

root = Tk()
root.title('Library Management System')
root.geometry("500x600")
root.configure(bg="#a8ceff")
root.pack_propagate(False)


library_system_connect = sqlite3.connect('lms.db')
library_system_cyr = library_system_connect.cursor()

system_logo = ImageTk.PhotoImage(file="lms_logo.png")
logo_widget = Label(root, image=system_logo, font=20, bg="#a8ceff")
logo_widget.image = system_logo
logo_widget.pack()
logo_widget.grid(row=0, column=0, columnspan=2)


#1  Check out new book loan
check_out_btn = Button(root, text='Check Out', width=20)
check_out_btn.grid(row=1, column=0, columnspan=2,pady=10, padx=100)

#2  Add new member into Borrower
borrower_btn = Button(root, text='New Member', width=20)
borrower_btn.grid(row=2, column=0, columnspan=2,pady=10, padx=100)

#3  Add new book into all 5 branches, 5 copies each branch
new_book_btn = Button(root, text='New Book', width=20)
new_book_btn.grid(row=3, column=0, columnspan=2,pady=10, padx=100)

#4  List the copies that are being loaned by the book title
book_search_btn = Button(root, text='Search Book', width=20)
book_search_btn.grid(row=4, column=0, columnspan=2,pady=10, padx=100)

#5  List late returned from book_loans by a given date
late_list_btn = Button(root, text='Late List', width=20)
late_list_btn.grid(row=5, column=0, columnspan=2,pady=10, padx=100)



root.mainloop()