def show():
    #print(txt.get(),txt2.get())
    add=0
    add=int(txt.get())+int(txt2.get())
    print(f"Addition is {add}")

import tkinter as tk
root=tk.Tk()
# palcing text box on window
txt=tk.Entry(root)
txt.pack()

txt2=tk.Entry(root)
txt2.pack()

btn=tk.Button(root,text='Get text',command=show)
btn.pack()

root.mainloop()

