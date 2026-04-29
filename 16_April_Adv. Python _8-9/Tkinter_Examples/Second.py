def clickme():
    print("Clicked ")
import tkinter as tk

root=tk.Tk()
btn=tk.Button(root,text="click me",command=clickme)
btn.pack()
root.geometry("300x300")
root.mainloop()