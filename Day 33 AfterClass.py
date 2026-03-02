from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Inches to Centimeters Converter")
window.geometry("1000x1000")
window.configure(bg="grey")

# Label
label1 = Label(window, text="Enter length in inches:", 
               font=("EB Garamond",20), bg="white", fg="black")
label1.place(x=100, y=200)

# Entry box
inchentry = Entry(window, width=35, font=("EB Garamond",20),
                  bg="white", fg="Darkblue")
inchentry.place(x=100, y=250)

# Function
def convert():
    try:
        inches = float(inchentry.get())
        cm = inches * 2.54
        messagebox.showinfo("Result", f"Length in centimeters: {cm}")
    except:
        messagebox.showerror("Error", "Please enter a valid number")

# Button
button = Button(window, text="Convert", font=("EB Garamond",10),
                width=20, bg="red", fg="Black", command=convert)
button.place(x=100, y=350)

window.mainloop()