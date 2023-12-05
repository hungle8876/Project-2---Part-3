# Khanh Nguyen
# Van Hung Le
# Phu Truong
# CSE-3330 Project 2
# December 5th, 2023


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
#from PIL import ImageTk


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
    year = Entry(query_frame, width=4)
    year.grid(row=3, column=2, padx=1, pady=10)
    year_lbl = Label(query_frame, text='Year')
    year_lbl.grid(row=3, column=1, padx=1, pady=10)
    

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

def new_borrower_gui():
    window = Toplevel(root)
    window.title("New Borrower")

    query_frame = Frame(window)
    query_frame.grid(row=0, column=0)

    borrower_labels = ['Borrower Name:', 'Borrower Address:', 'Borrower Phone:']
    borrower_entries = []
    for idx, label in enumerate(borrower_labels):
        Label(query_frame, text=label).grid(row=1 + idx, column=0, padx=5, pady=10, sticky=W)
        entry = Entry(query_frame, width=30)
        entry.grid(row=1 + idx, column=1, padx=5, pady=10, sticky=W)
        borrower_entries.append(entry)

    name_entry, address_entry, phone_entry = borrower_entries

    # Button for adding a borrower
    Button(query_frame, text='Add Borrower', width=20, command=lambda: new_borrower(name_entry.get(), address_entry.get(), phone_entry.get())).grid(row=5, column=0, columnspan=2, padx=5, pady=10)

   
def new_borrower(name, address, phone):
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    cur.execute('''INSERT INTO Borrower (Name, Address, Phone) VALUES (?, ?, ?)''', 
                (name, address, phone))

    # Retrieve the last inserted card number
    card_no = cur.lastrowid
    

    conn.commit()
    conn.close()

    # Display the card number
    messagebox.showinfo("Card Number", f"New Card Number: {card_no}")


def new_book_gui():
    window = Toplevel(root)
    window.title("New Borrower")

    query_frame = Frame(window)
    query_frame.grid(row=0, column=0)


    title = Entry(query_frame, width = 30)
    title.grid(row = 1, column = 1, padx = 20)
    book_publisher = Entry(query_frame, width = 30)
    book_publisher.grid(row = 2, column = 1, padx = 20)
    book_author = Entry(query_frame, width = 30)
    book_author.grid(row = 3, column = 1, padx = 20)

    
    title_label = Label(query_frame, text = 'Title: ')
    title_label.grid(row =1, column = 0)
    book_publisher_label = Label(query_frame, text = 'Book Publisher: ')
    book_publisher_label.grid(row =2, column = 0)
    book_author_label = Label(query_frame, text = 'Book Author: ')
    book_author_label.grid(row =3, column = 0)

    submit_book_btn = Button(query_frame, text ='Add Book ', command =lambda: new_book(title.get(), book_publisher.get(), book_author.get()))
    submit_book_btn.grid(row = 4, column =0, columnspan = 2, pady = 10, padx = 5, ipadx =100)

def new_book(title, publisher, author):
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    # Insert into Book
    cur.execute('''INSERT INTO Book (Title, Publisher_name) VALUES (?, ?)''', 
                (title, publisher))
    book_id = cur.lastrowid

    # Insert into Book_Authors
    cur.execute('''INSERT INTO Book_Authors (Book_id, Author_name) VALUES (?, ?)''', 
                (book_id, author))

    # Insert into Book_Copies for all 5 branches
    for branch_id in range(1, 6):
        cur.execute('''INSERT INTO Book_Copies (Book_id, Branch_id, No_of_copies) VALUES (?, ?, ?)''', 
                    (book_id, branch_id, 5))

    conn.commit()
    conn.close()


def book_search_gui():
    window = Toplevel(root)
    window.title("New Borrower")

    query_frame = Frame(window)
    query_frame.grid(row=0, column=0)

    book_title= Entry(query_frame, width = 30)
    book_title.grid(row = 1, column = 1, padx = 20)

    book_title_label = Label(query_frame, text = 'Book Title: ')
    book_title_label.grid(row =1, column = 0)

    display_area = Text(query_frame, height=10, width=50)
    display_area.grid(row=13, column=0, columnspan=2, padx=5, pady=10)

    submit_book_title_btn = Button(query_frame, text ='Lookup Copies ', command = lambda: book_search(book_title.get(),display_area))
    submit_book_title_btn.grid(row = 2, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 70)

    

def book_search(title, display_area):
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    cur.execute('''SELECT Branch_id, COUNT(*) FROM Book_Loans JOIN Book ON Book_Loans.Book_id = Book.Book_id 
                   WHERE Title = ? GROUP BY Branch_id''', (title,))

    records = cur.fetchall()

    # Display the records
    display_area.delete('1.0', END)  # Clear existing text
    for record in records:
        display_area.insert(END, f"Branch ID: {record[0]}, Copies Loaned: {record[1]}\n")

    conn.close()

def late_list_gui():
    window = Toplevel(root)
    window.title("New Borrower")

    query_frame = Frame(window)
    query_frame.grid(row=0, column=0)

    start_date_1= Entry(query_frame, width = 30)
    start_date_1.grid(row = 1, column = 1, padx = 5)
    start_date_1_label = Label(query_frame, text = 'Start Date: ')
    start_date_1_label.grid(row =1, column = 0)

    due_date_1= Entry(query_frame, width = 30)
    due_date_1.grid(row = 2, column = 1, padx = 5)
    due_date_1_label = Label(query_frame, text = 'Due Date: ')
    due_date_1_label.grid(row =2, column = 0)

    submit_book_title_btn = Button(query_frame, text ='Lookup Late Returns ', command = lambda: late_list(start_date_1.get(), due_date_1.get()))
    submit_book_title_btn.grid(row = 3, column =0, columnspan = 2, pady = 10, padx = 5, ipadx = 70)

def late_list(start, due):
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    cur.execute('''SELECT Book_id, Branch_id, Card_no, Due_date, Returned_date, 
                   JULIANDAY(Returned_date) - JULIANDAY(Due_date) AS Late_Days
                   FROM Book_Loans
                   WHERE Returned_date > Due_date AND Due_date BETWEEN ? AND ?''', 
                (start, due))

    records = cur.fetchall()

    # Display the records
    display_area.delete('1.0', END)  # Clear existing text
    for record in records:
        display_area.insert(END, f"Book ID: {record[0]}, Branch ID: {record[1]}, Card No: {record[2]}, Late by {record[5]} days\n")

    conn.close()





# Create GUI
root = Tk()
root.title('Library Management System')
root.geometry("500x600")
root.configure(bg="#a8ceff")
root.pack_propagate(False)


library_system_connect = sqlite3.connect('main.db')
library_system_cyr = library_system_connect.cursor()

"""library_system_connect = '''CREATE TRIGGER update_book_copies
                            AFTER UPDATE ON book_loans
                            FOR EACH ROW
                            WHEN NEW.Book_id IS NOT NULL AND NEW.Branch_id IS NOT NULL
                            BEGIN
                                UPDATE book_copies
                                SET No_of_copies = No_of_copies - 1
                                WHERE Book_copies.Book_id = NEW.Book_id AND Book_copies.Branch_id = NEW.Branch_id;
                            END;'''"""

#system_logo = ImageTk.PhotoImage(file="lms_logo.png")
#logo_widget = Label(root, image=system_logo, font=20, bg="#a8ceff")
#logo_widget.image = system_logo
#logo_widget.pack()
#logo_widget.grid(row=0, column=0, columnspan=2, pady=0)
title = Label(root, text="Library Management System", font=10, bg="#a8ceff", fg='black')
title.grid(row=1, column=0, columnspan=2, pady=10, padx=100)


#1  Check out new book loan
check_out_btn = Button(root, text='Check Out', command=check_out, width=20, fg='black')
check_out_btn.grid(row=2, column=0, columnspan=2,pady=10, padx=100)

#2  Add new member into Borrower
new_borrower_btn = Button(root, text='New Borrower', command=new_borrower_gui, width=20, fg='black')
new_borrower_btn.grid(row=3, column=0, columnspan=2,pady=10, padx=100)

#3  Add new book into all 5 branches, 5 copies each branch
new_book_btn = Button(root, text='New Book', command=new_book_gui, width=20, fg='black')
new_book_btn.grid(row=4, column=0, columnspan=2,pady=10, padx=100)

#4  List the copies that are being loaned by the book title
book_search_btn = Button(root, text='Search Book', command=book_search_gui, width=20, fg='black')
book_search_btn.grid(row=5, column=0, columnspan=2,pady=10, padx=100)

#5  List late returned from book_loans by a given date
late_list_btn = Button(root, text='Late List', command=late_list_gui, width=20, fg='black')
late_list_btn.grid(row=6, column=0, columnspan=2,pady=10, padx=100)



root.mainloop()