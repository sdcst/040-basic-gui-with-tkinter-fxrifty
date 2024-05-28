#!python3
import tkinter as tk

Window=tk.Tk()
Window.title=("tkk")
Window.geometry=("600x1800")
buttin1=tk.Entry(Window,width=20)
buttin2=tk.Entry(Window,width=20)
buttin3=tk.Entry(Window,width=20)
label1=tk.Label(Window,text="x")
label2=tk.Label(Window,text="=")



buttin1.grid(row=1,column=1)
buttin2.grid(row=1,column=3)
buttin3.grid(row=1,column=5)
label2.grid(row=1,column=4)
label1.grid(row=1,column=2)

Window.mainloop()