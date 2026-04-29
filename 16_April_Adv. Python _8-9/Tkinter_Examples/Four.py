
import tkinter as tk

def show():
    add=int(txt.get())+int(txt2.get())
    print(f"Addition is {add}")
    #result_text.set("Addition is ")
    ans="Result is "+str(add)
    result_text.set(ans)

root=tk.Tk()
result_text=tk.StringVar()
# palcing text box on window
lbl1=tk.Label(root,text="Enter number 1 ")
#lbl1.pack()
lbl1.grid(row=0,column=0)
txt=tk.Entry(root)
#txt.pack()
txt.grid(row=0,column=1)

lbl2=tk.Label(root,text="Enter number 2 ")
#lbl2.pack()
lbl2.grid(row=1,column=0)
txt2=tk.Entry(root)
#txt2.pack()
txt2.grid(row=1,column=1)


btn=tk.Button(root,text='+',command=show)
btn.grid(row=2,column=0)

result=tk.Label(root,text="Answer is ",textvariable=result_text)
result.grid(row=2,column=1)



root.mainloop()
