import tkinter as tk
def show_data():
    print("Python ",varPython.get())
    print("Java ",varJava.get())


root=tk.Tk()

varPython=tk.IntVar()
varJava=tk.IntVar()

chkPython=tk.Checkbutton(root,text="Python",variable=varPython)
chkPython.pack()

chkJava=tk.Checkbutton(root,text="Java",variable=varJava)
chkJava.pack()

btn=tk.Button(root,text="Show",command=show_data)
btn.pack()
root.mainloop()