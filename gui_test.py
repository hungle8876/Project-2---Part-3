import sqlite3
from tkinter import *
from tkinter import messagebox

# Create the root window
root = Tk()
root.title('LMS GUI Application')
root.geometry("600x800")

# address_book_connect = sqlite3.connect('lms.db')

# address_book_cur = address_book_connect.cursor()

# Define function for all button

def show_updated_copies():
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM Book_Copies")
    records = cur.fetchall()

    display_area.delete('1.0', END)  # Clear existing text
    for record in records:
        display_area.insert(END, f"Book ID: {record[0]}, Branch ID: {record[1]}, Number of Copies: {record[2]}\n")

    conn.close()

def checkout_book():
    # Connect to the database
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    # Insert into Book_Loans and rely on a trigger to update Book_Copies
    cur.execute('''INSERT INTO Book_Loans (Book_id, Branch_id, Card_no, Date_out, Due_date) 
                   VALUES (?, ?, ?, ?, ?)''', 
                (book_id_entry.get(), branch_id_entry.get(), card_no_entry.get(), date_out_entry.get(), due_date_entry.get()))

    # Commit and close
    conn.commit()
    conn.close()

    # Show updated Book_Copies (additional query needed)
    show_updated_copies()


def add_borrower():
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    cur.execute('''INSERT INTO Borrower (Name, Address, Phone) VALUES (?, ?, ?)''', 
                (name_entry.get(), address_entry.get(), phone_entry.get()))

    # Retrieve the last inserted card number
    card_no = cur.lastrowid

    conn.commit()
    conn.close()

    # Display the card number
    messagebox.showinfo("Card Number", f"New Card Number: {card_no}")

def add_book():
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    # Insert into Book
    cur.execute('''INSERT INTO Book (Title, Publisher_name) VALUES (?, ?)''', 
                (title_entry.get(), publisher_name_entry.get()))
    book_id = cur.lastrowid

    # Insert into Book_Authors
    cur.execute('''INSERT INTO Book_Authors (Book_id, Author_name) VALUES (?, ?)''', 
                (book_id, author_name_entry.get()))

    # Insert into Book_Copies for all 5 branches
    for branch_id in range(1, 6):
        cur.execute('''INSERT INTO Book_Copies (Book_id, Branch_id, No_of_copies) VALUES (?, ?, ?)''', 
                    (book_id, branch_id, 5))

    conn.commit()
    conn.close()

def list_copies_loaned():
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    cur.execute('''SELECT Branch_id, COUNT(*) FROM Book_Loans JOIN Book ON Book_Loans.Book_id = Book.Book_id 
                   WHERE Title = ? GROUP BY Branch_id''', (title_entry.get(),))

    records = cur.fetchall()

    # Display the records
    display_area.delete('1.0', END)  # Clear existing text
    for record in records:
        display_area.insert(END, f"Branch ID: {record[0]}, Copies Loaned: {record[1]}\n")

    conn.close()

def list_late_returns():
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    cur.execute('''SELECT Book_id, Branch_id, Card_no, Due_date, Returned_date, 
                   JULIANDAY(Returned_date) - JULIANDAY(Due_date) AS Late_Days
                   FROM Book_Loans
                   WHERE Returned_date > Due_date AND Due_date BETWEEN ? AND ?''', 
                (start_date_entry.get(), end_date_entry.get()))

    records = cur.fetchall()

    # Display the records
    display_area.delete('1.0', END)  # Clear existing text
    for record in records:
        display_area.insert(END, f"Book ID: {record[0]}, Branch ID: {record[1]}, Card No: {record[2]}, Late by {record[5]} days\n")

    conn.close()


def search_borrowers():
    conn = sqlite3.connect('lms.db')
    cur = conn.cursor()

    query = '''SELECT Card_no, Name, IFNULL(LateFee_Balance, 0.00) as Balance
               FROM Borrower
               LEFT JOIN LateFees ON Borrower.Card_no = LateFees.Card_no
            '''

    criteria = []
    if borrower_id_entry.get():
        query += ' WHERE Borrower.Card_no = ?'
        criteria.append(borrower_id_entry.get())
    elif borrower_name_entry.get():
        query += ' WHERE Name LIKE ?'
        criteria.append('%' + borrower_name_entry.get() + '%')

    query += ' ORDER BY Balance DESC'

    cur.execute(query, criteria)
    records = cur.fetchall()

    # Display the records
    display_area.delete('1.0', END)  # Clear existing text
    for record in records:
        display_area.insert(END, f"Card No: {record[0]}, Name: {record[1]}, Balance: ${record[2]:.2f}\n")

    conn.close()


# Define entry fields, labels, and buttons for each task
# ... (similar to the previous snippets)

# Place the components on the grid
# ... (use grid() method as shown before)



# # ---------------- Task 1: Check out a book ----------------

# # Labels
# Label(root, text='Book ID:').grid(row=0, column=0)
# Label(root, text='Branch ID:').grid(row=1, column=0)
# Label(root, text='Card No:').grid(row=2, column=0)
# Label(root, text='Date Out:').grid(row=3, column=0)
# Label(root, text='Due Date:').grid(row=4, column=0)

# # Entry fields
# book_id_entry = Entry(root)
# branch_id_entry = Entry(root)
# card_no_entry = Entry(root)
# date_out_entry = Entry(root)
# due_date_entry = Entry(root)

# book_id_entry.grid(row=0, column=1)
# branch_id_entry.grid(row=1, column=1)
# card_no_entry.grid(row=2, column=1)
# date_out_entry.grid(row=3, column=1)
# due_date_entry.grid(row=4, column=1)

# # Button
# Button(root, text='Check out Book', command=checkout_book).grid(row=5, column=0, columnspan=2)

# # ---------------- Task 2: Add a new Borrower ----------------

# Label(root, text='Borrower Name:').grid(row=6, column=0)
# Label(root, text='Borrower Address:').grid(row=7, column=0)
# Label(root, text='Borrower Phone:').grid(row=8, column=0)

# name_entry = Entry(root)
# address_entry = Entry(root)
# phone_entry = Entry(root)

# name_entry.grid(row=6, column=1)
# address_entry.grid(row=7, column=1)
# phone_entry.grid(row=8, column=1)

# Button(root, text='Add Borrower', command=add_borrower).grid(row=9, column=0, columnspan=2)

# # ---------------- Task 5: List Late Returns ----------------

# Label(root, text='Start Date:').grid(row=10, column=0)
# Label(root, text='End Date:').grid(row=11, column=0)

# start_date_entry = Entry(root)
# end_date_entry = Entry(root)

# start_date_entry.grid(row=10, column=1)
# end_date_entry.grid(row=11, column=1)

# Button(root, text='List Late Returns', command=list_late_returns).grid(row=12, column=0, columnspan=2)


# # Entry fields for adding a new book
# Label(root, text='Book Title:').grid(row=14, column=0)
# Label(root, text='Publisher Name:').grid(row=15, column=0)
# Label(root, text='Author Name:').grid(row=16, column=0)

# title_entry = Entry(root)
# publisher_name_entry = Entry(root)
# author_name_entry = Entry(root)

# title_entry.grid(row=14, column=1)
# publisher_name_entry.grid(row=15, column=1)
# author_name_entry.grid(row=16, column=1)

# Button(root, text='Add Book', command=add_book).grid(row=17, column=0, columnspan=2)

# # Entry fields for searching borrowers
# Label(root, text='Borrower ID:').grid(row=18, column=0)
# Label(root, text='Borrower Name:').grid(row=19, column=0)

# borrower_id_entry = Entry(root)
# borrower_name_entry = Entry(root)

# borrower_id_entry.grid(row=18, column=1)
# borrower_name_entry.grid(row=19, column=1)

# Button(root, text='Search Borrowers', command=search_borrowers).grid(row=20, column=0, columnspan=2)


# # Display area for results
# display_area = Text(root, height=10, width=50)
# display_area.grid(row=13, column=0, columnspan=2)


# Common padding
padx = 10
pady = 5
button_width = 20  # Width for buttons

# ---------------- Task 1: Check out a book ----------------
# Labels and Entry fields for checking out a book
labels = ['Book ID:', 'Branch ID:', 'Card No:', 'Date Out:', 'Due Date:']
entries = []
for idx, label in enumerate(labels):
    Label(root, text=label).grid(row=idx, column=0, padx=padx, pady=pady, sticky=W)
    entry = Entry(root, width=30)
    entry.grid(row=idx, column=1, padx=padx, pady=pady, sticky=W)
    entries.append(entry)

# Destructure entries for individual use
book_id_entry, branch_id_entry, card_no_entry, date_out_entry, due_date_entry = entries

# Button for checking out a book
Button(root, text='Check out Book', width=button_width, command=checkout_book).grid(row=5, column=0, columnspan=2, padx=padx, pady=pady)

# ---------------- Task 2: Add a new Borrower ----------------
# Labels and Entry fields for adding a new borrower
borrower_labels = ['Borrower Name:', 'Borrower Address:', 'Borrower Phone:']
borrower_entries = []
for idx, label in enumerate(borrower_labels):
    Label(root, text=label).grid(row=6 + idx, column=0, padx=padx, pady=pady, sticky=W)
    entry = Entry(root, width=30)
    entry.grid(row=6 + idx, column=1, padx=padx, pady=pady, sticky=W)
    borrower_entries.append(entry)

# Destructure entries for individual use
name_entry, address_entry, phone_entry = borrower_entries

# Button for adding a borrower
Button(root, text='Add Borrower', width=button_width, command=add_borrower).grid(row=9, column=0, columnspan=2, padx=padx, pady=pady)

# ---------------- Task 5: List Late Returns ----------------
# Labels and Entry fields for listing late returns
late_return_labels = ['Start Date:', 'End Date:']
late_return_entries = []
for idx, label in enumerate(late_return_labels):
    Label(root, text=label).grid(row=10 + idx, column=0, padx=padx, pady=pady, sticky=W)
    entry = Entry(root, width=30)
    entry.grid(row=10 + idx, column=1, padx=padx, pady=pady, sticky=W)
    late_return_entries.append(entry)

# Destructure entries for individual use
start_date_entry, end_date_entry = late_return_entries

# Button for listing late returns
Button(root, text='List Late Returns', width=button_width, command=list_late_returns).grid(row=12, column=0, columnspan=2, padx=padx, pady=pady)

# ---------------- Additional Tasks ----------------
# Additional task entry fields and buttons ...

# Display area for results
display_area = Text(root, height=10, width=50)
display_area.grid(row=13, column=0, columnspan=2, padx=padx, pady=pady)


# Main loop
root.mainloop()
