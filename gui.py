# Khanh Nguyen
# Van Hung Le
# Phu Truong


from tkinter import *
import sqlite3

root = Tk()
root.title('Library Management System')
root.geometry("400x400")

library_system_connect = sqlite3.connect('lms.db')
library_system_cyr = library_system_connect.cursor()

title = Label(root, text='Library Management System', font=20)
title.grid(row=0, column=0, columnspan=2, pady=10, padx=100)

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