import tkinter as tk
Window=tk.Tk()
Window.title=("tkk")
Window.geometry=("1400x1400")
dogphotot= tk.PhotoImage(file="dog.png")
label0 = tk.Label(Window, image=dogphotot)
Label1 = tk.Label(text="A Cuddly Little Puppy! This Is From The Same ", background="#ffaaff")
Label2 = tk.Label(text="Creators Who Brought You Keropi And Kero Kero", background="#ffaaff")
Label3 = tk.Label(text="Pochacco!")

label0.place(x=30,y=40)
Label1.place(x=10,y=160)
Label2.place(x=0,y=180)
Label3.place(x=110,y=80)
Window.mainloop()