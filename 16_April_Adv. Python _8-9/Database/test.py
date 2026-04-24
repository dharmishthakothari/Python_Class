import tkinter as tk

#Tk() → creates the main window
root = tk.Tk()

#title() → sets window title
root.title("My First App")

# geometry() → sets size
root.geometry("300x200")

# Widget = UI element (Label, Button, etc.)
label = tk.Label(root, text="Hello, Tkinter!")

#pack() = places the widget in the window
label.pack()
#mainloop() → keeps app running
root.mainloop()