import tkinter as tk
from tkinter.constants import E, N, W

Window=tk.Tk()
Window.title=("tkk")
Window.geometry=("900x900")
dogphotot= tk.PhotoImage(file="dog.png")
label0 = tk.Label(Window, image=dogphotot)
Label1 = tk.Label(text="A Cuddly Little Puppy! This Is From The Same ", background="#ffaaff")
Label2 = tk.Label(text="Creators Who Brought You Keropi And Kero Kero", background="#ffaaff")
Label3 = tk.Label(text="Pochacco!")


label0.grid(row=0,column=1)
Label1.grid(row=1,column=1)
Label2.grid(row=2,column=1)
Label3.grid(row=0,column=1,sticky=E)



Window.mainloop()