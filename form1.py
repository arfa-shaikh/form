import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['customerid'])
    e2.insert(0, select['customername'])
    e3.insert(0, select['email'])
    e4.insert(0, select['contact'])


def Add():
    customerid = e1.get()
    customername = e2.get()
    email = e3.get()
    contact = e4.get()

    mysqldb = mysql.connector.connect(
        host="127.0.0.1", user="root", password="12345", database="cms")
    mycursor = mysqldb.cursor()

    try:
        sql = "INSERT INTO  customer (customerid,customername,email,contact) VALUES (%s, %s, %s, %s)"
        val = (customerid, customername, email, contact)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Customer inserted successfully...")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    customerid = e1.get()
    customername = e2.get()
    email = e3.get()
    contact = e4.get()
    mysqldb = mysql.connector.connect(
        host="127.0.0.1", user="root", password="12345", database="cms")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  customer set customername= %s,email= %s,contact= %s where customerid= %s"
        val = (customername, email, contact, customerid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo(
            "information", "Record Updateddddd successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(
        host="127.0.0.1", user="root", password="12345", database="cms")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from customer where customerid = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Deleteeeee successfully...")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(
        host="127.0.0.1", user="root", password="12345", database="cms")
    mycursor = mysqldb.cursor()
    mycursor.execute(
        "SELECT customerid,customername,email,contact FROM customer")
    records = mycursor.fetchall()
    print(records)

    for i, (customerid, customername, email, contact) in enumerate(records, start=1):
        listBox.insert("", "end", values=(
            customerid, customername, email, contact))
        mysqldb.close()


root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4

tk.Label(root, bg="yellow", text="Customer Registration",
         fg="red", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Customer ID").place(x=10, y=10)
Label(root, text="Customer Name").place(x=10, y=40)
Label(root, text="Email").place(x=10, y=70)
Label(root, text="Contact").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Add", command=Add, height=3, width=13).place(x=30, y=130)
Button(root, text="update", command=update,
       height=3, width=13).place(x=140, y=130)
Button(root, text="Delete", command=delete,
       height=3, width=13).place(x=250, y=130)

cols = ('Customer id', 'Customer name', 'Email', 'Contact')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()
