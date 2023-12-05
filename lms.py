# -- PyQt5 pip install PyQt5

# -- Tkinter pip install tkinter

# -- Kivy pip install kivy

from tkinter import *
import sqlite3

#connect to DB

conn = sqlite3.connect('lms.db')

# create tkinter window
root = Tk()
root.title('Library Manage System')
root.geometry("400x600")

# task 1

def task_1():
    submit_conn = sqlite3.connect('lms.db')

    submit_cur = submit_conn.cursor()

    submit_cur.execute("INSERT INTO Book_Loans VALUES (:book_id, :branch_id, :card_no, :date_out, :due_date, :returned_date)",
                       {
                           'book_id': book_id.get(),
                           'branch_id': branch_id.get(),
                           'card_no': card_no.get(),
                           'date_out': date_out.get(),
                           'due_date': due_date.get(),
                           'returned_date': returned_date.get() 
                       })
    
    submit_conn.commit()
    submit_conn.close()

# task 2

def task_2():
    submit_conn = sqlite3.connect('lms.db')

    submit_cur = submit_conn.cursor()

    submit_cur.execute("INSERT INTO Borrower VALUES (:name, :address, :phone)",
                       {
                           'name': book_id.get(),
                           'address': branch_id.get(),
                           'phone': card_no.get(),
                       })
    
    submit_conn.commit()
    submit_conn.close()

# task 3

def task_3():

    submit_conn = sqlite3.connect('lms.db')

    submit_cur = submit_conn.cursor()

    submit_cur.execute("INSERT INTO Book VALUES (:book_id, :title, :book_publisher)",
                       {
                           'book_id': book_id_1.get(),
                           'title': title.get(),
                           'book_publisher': book_publisher.get()
                       })
    
    submit_conn.commit()
    submit_conn.close()

# task 4

def task_4():

    submit_conn = sqlite3.connect('lms.db')

    submit_cur = submit_conn.cursor()

    submit_cur.execute("SELECT no_of_copies FROM Book_Copies JOIN Book ON Book_Copies.book_id=Book.book_id WHERE title = ?",
                       (book_title.get(),))
    
    records = submit_cur.fetchall()

    print_record = ''

    for output_record in records:
        print_record += str(output_record[0]) + "\n"

    task_4_label = Label(root, text = print_record)

    task_4_label.grid(row = 24, column = 0, columnspan = 2)

    submit_conn.commit()
    submit_conn.close()

# task 5

def task_5():

    submit_conn = sqlite3.connect('lms.db')

    submit_cur = submit_conn.cursor()

    submit_cur.execute("SELECT Title, julianday(Returned_date) - julianday(due_date) AS days_late FROM Book_Loans JOIN Book ON Book_Loans.book_id = Book.Book_id WHERE (Returned_date IS NOT NULL AND Returned_date > due_date)")
                       
    records = submit_cur.fetchall()

    print_record = ''

    for output_record in records:
        print_record += str(output_record[0]) + ": " + str(output_record[1]) + " Days late\n"

    task_5_label = Label(root, text = print_record)

    task_5_label.grid(row = 28, column = 0, columnspan = 2)

    submit_conn.commit()
    submit_conn.close()

# task 6



# gui -----------

# task 1 gui
book_id = Entry(root, width = 30)
book_id.grid(row = 0, column = 1, padx = 20)
branch_id= Entry(root, width = 30)
branch_id.grid(row = 1, column = 1)
card_no = Entry(root, width = 30)
card_no.grid(row = 2, column = 1)
date_out = Entry(root, width = 30)
date_out.grid(row = 3, column = 1)
due_date = Entry(root, width = 30)
due_date.grid(row = 4, column = 1)
returned_date = Entry(root, width = 30)
returned_date.grid(row = 5, column = 1)

book_id_label = Label(root, text = 'Book ID: ')
book_id_label.grid(row =0, column = 0)
branch_id_label = Label(root, text = 'Branch ID: ')
branch_id_label.grid(row =1, column = 0)
card_no_label = Label(root, text = 'Card No: ')
card_no_label.grid(row =2, column = 0)
date_out_label = Label(root, text = 'Date Out: ')
date_out_label.grid(row =3, column = 0)
due_date_label = Label(root, text = 'Due Date: ')
due_date_label.grid(row =4, column = 0)
returned_date_label = Label(root, text = 'Returned Date: ')
returned_date_label.grid(row =5, column = 0)

submit_book_loan_btn = Button(root, text ='Add Book Loan ', command = task_1)
submit_book_loan_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx =
140)

# task 2 gui

name = Entry(root, width = 30)
name.grid(row = 9, column = 1, padx = 20)
address = Entry(root, width = 30)
address.grid(row = 10, column = 1, padx = 20)
phone = Entry(root, width = 30)
phone.grid(row = 11, column = 1, padx = 20)

name_label = Label(root, text = 'Name: ')
name_label.grid(row =9, column = 0)
address_label = Label(root, text = 'Address: ')
address_label.grid(row =10, column = 0)
phone_label = Label(root, text = 'Phone: ')
phone_label.grid(row =11, column = 0)

submit_borrower_btn = Button(root, text ='Add Book Loan ', command = task_2)
submit_borrower_btn.grid(row = 13, column =0, columnspan = 2, pady = 10, padx = 10, ipadx =
140)

# task 3 gui

book_id_1 = Entry(root, width = 30)
book_id_1.grid(row = 15, column = 1, padx = 20)
title = Entry(root, width = 30)
title.grid(row = 16, column = 1, padx = 20)
book_publisher = Entry(root, width = 30)
book_publisher.grid(row = 17, column = 1, padx = 20)

book_id_label = Label(root, text = 'Book ID: ')
book_id_label.grid(row =15, column = 0)
title_label = Label(root, text = 'Title: ')
title_label.grid(row =16, column = 0)
book_publisher_label = Label(root, text = 'Book Publisher: ')
book_publisher_label.grid(row =17, column = 0)

submit_book_btn = Button(root, text ='Add Book ', command = task_3)
submit_book_btn.grid(row = 19, column =0, columnspan = 2, pady = 10, padx = 10, ipadx =
140)

#task 4 gui
 
book_title= Entry(root, width = 30)
book_title.grid(row = 21, column = 1, padx = 20)

book_title_label = Label(root, text = 'Book Title: ')
book_title_label.grid(row =21, column = 0)

submit_book_title_btn = Button(root, text ='Lookup Copies ', command = task_4)
submit_book_title_btn.grid(row = 23, column =0, columnspan = 2, pady = 10, padx = 10, ipadx =
140)

#task 5 gui

due_date_1= Entry(root, width = 30)
due_date_1.grid(row = 25, column = 1, padx = 20)

due_date_1_label = Label(root, text = 'Due Date: ')
due_date_1_label.grid(row =25, column = 0)

submit_book_title_btn = Button(root, text ='Lookup Late Returns ', command = task_5)
submit_book_title_btn.grid(row = 27, column =0, columnspan = 2, pady = 10, padx = 10, ipadx =
140)

root.mainloop()