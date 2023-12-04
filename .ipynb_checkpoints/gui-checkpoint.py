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




root.mainloop()