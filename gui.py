# Khanh Nguyen
# Van Hung Le
# Phu Truong
# CSE-3330 Project 2
# December 5th, 2023


from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk


# Define function for all button
def check_out():
    window = Toplevel(root)
    window.title("Check out")

    query_frame = Frame(window)
    query_frame.grid(row=0, column=0)
    output_frame = Frame(window)
    output_frame.grid(row=1, column=0)

    book_id_label = Label(query_frame, text='Book_id')
    book_id_label.grid(row=0, column=0, pady=10, padx=5)
    book_id_input = Entry(query_frame, width=10)
    book_id_input.grid(row=0, column=1, pady=10, padx=5)


    vlist = ['1', '2', '3']
    branch_id_label = Label(query_frame, text='Branch_id')
    branch_id_label.grid(row=1, column=0, pady=10, padx=5)
    branch_id_input = ttk.Combobox(query_frame, values=vlist, width=10)
    branch_id_input.set('Pick a branch')
    branch_id_input.grid(row=1, column=1, pady=10, padx=5)

    card_no_label = Label(query_frame, text='Card_no')
    card_no_label.grid(row=2, column=0, pady=10, padx=5)
    card_no_input = Entry(query_frame, width=10)
    card_no_input.grid(row=2, column=1, pady=10, padx=5)

    date_out_label = Label(query_frame, text='Date out')
    date_out_label.grid(row=3, column=0, padx=1, pady=10)

    year_lbl = Label(query_frame, text='Year')
    year_lbl.grid(row=3, column=1, padx=1, pady=10)
    year = Entry(query_frame, width=4)
    year.grid(row=3, column=2, padx=1, pady=10)

    month_lbl = Label(query_frame, text='Month')
    month_lbl.grid(row=3, column=3, padx=1, pady=10)
    month = Entry(query_frame, width=2)
    month.grid(row=3, column=4, padx=1, pady=10)

    day_lbl = Label(query_frame, text='Day')
    day_lbl.grid(row=3, column=5, padx=1, pady=10)
    day = Entry(query_frame, width=2)
    day.grid(row=3, column=6, padx=1, pady=10)

    submit_btn = Button(query_frame, text='Submit', command=lambda: checkout_result(output_frame, book_id_input.get(),
                         branch_id_input.get(), card_no_input.get(), year.get(), month.get(), day.get()))
    submit_btn.grid(row=4, column=0, columnspan=2, padx=1, pady=10)
    
def checkout_result(frame, book, branch, card, year, month, day):
    db_conn = sqlite3.connect('lms.db')
    db_cur = db_conn.cursor()
    date_out = year + '-' + month + '-' + day
    monthdue= int(month) + 1
    yeardue = int(year)
    if (monthdue == 13):
        yeardue += 1
        monthdue = 1
    due_date = "{}-{}-{}".format(str(yeardue), str(monthdue), day)
    db_cur.execute("INSERT INTO BOOK_LOANS(Book_id, Branch_id, Card_no, Date_out, Due_date) VALUES(?,?,?,?,?)", (int(book), int(branch), int(card), date_out, due_date))
    db_conn.commit()
    db_conn.close()

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