import tkinter as tk
import sqlite3

def insert_data():
    data=txt.get()
    print("You have entered ",data)
    conn=sqlite3.connect("db2.db")
    cur=conn.cursor()
    cur.execute("create table if not exists users(uname varchar(20))")

    cur.execute("insert into users values(?)",(data,))
    conn.commit()
    print("Data Inserted Successfully ")
def show_data():
    conn=sqlite3.connect("db2.db")
    cur=conn.cursor()
    cur.execute("select * from users")
    rows=cur.fetchall()
    #lst.delete(0,tk.END)
    for row in rows:
        lst.insert(0,row)
    conn.close()
    
root=tk.Tk()
lbl=tk.Label(root,text="Enter username ")
lbl.pack()

txt=tk.Entry(root)
txt.pack()

btn=tk.Button(root,text="Insert",command=insert_data)
btn.pack()

btn2=tk.Button(root,text="Show Data ",command=show_data)
btn2.pack()

lst=tk.Listbox(root)
lst.pack()
root.mainloop()
