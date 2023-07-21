#Import the required Libraries
from tkinter import *
from tkinter import ttk
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of Tkinter frame
win.geometry("300x300")

top = None

def open_popup():
   global top
   top = Toplevel(win)
   top.geometry("200x200")
   top.title("Child Window")

   # Label(top, text= "Hello World!", font=('Mistral 18 bold')).grid(row=0, column=0)
   # frame = Frame(top).grid(row=1, column=0)

   canvas = Canvas(top, bg="ivory",
                          width=100,
                          height=100,
                          scrollregion=(0, 0, 100, 100))
   canvas.pack()

   canvas.create_rectangle(0, 0, 20, 20, width=1, outline="red", fill="green")

Label(win, text=" Open the Popup Window", font=('Helvetica 14 bold')).pack(pady=20)
#Create a button in the main Window to open the popup
ttk.Button(win, text= "Open", command=open_popup).pack()

def close():
    top.destroy()
ttk.Button(win, text= "Close", command=close).pack()

frame = Frame(top).pack()
canvas = Canvas(frame, bg="ivory",
                width=100,
                height=100,
                scrollregion=(0, 0, 100, 100))

canvas.pack()

# canvas.config(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)


canvas.create_rectangle(0, 0, 20, 20, width=1, outline="red", fill="green")

canvas.config(scrollregion=canvas.bbox("all"))


win.mainloop()
