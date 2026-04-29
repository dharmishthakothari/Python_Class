import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox
def show_msg():
    messagebox.showinfo("Information","This is for Leanring ")
def show_warn():
    messagebox.showwarning("warning","Are you sure you want to delete ?")
root=tk.Tk()
btn=tk.Button(root,text="Show msg",command=show_msg)
btn.pack()

btn2=tk.Button(root,text='Delete',command=show_warn)
btn2.pack()

root.mainloop()
