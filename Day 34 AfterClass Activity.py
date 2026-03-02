from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Interest Calculator")
window.geometry("1000x1000")
window.configure(bg="grey")

# Labels
Label(window, text="Enter Principal:", font=("EB Garamond",20), bg="white").place(x=100,y=100)
Label(window, text="Enter Rate (%):", font=("EB Garamond",20), bg="white").place(x=100,y=200)
Label(window, text="Enter Time (years):", font=("EB Garamond",20), bg="white").place(x=100,y=300)

# Entry boxes
principalEntry = Entry(window, width=25, font=("EB Garamond",20))
principalEntry.place(x=400,y=100)

rateEntry = Entry(window, width=25, font=("EB Garamond",20))
rateEntry.place(x=400,y=200)

timeEntry = Entry(window, width=25, font=("EB Garamond",20))
timeEntry.place(x=400,y=300)

# Function
def calculate():
    try:
        P = float(principalEntry.get())
        R = float(rateEntry.get())
        T = float(timeEntry.get())

        SI = (P * R * T) / 100
        CI = P * ((1 + R/100) ** T) - P

        messagebox.showinfo("Result", f"Simple Interest: ₹{SI}\nCompound Interest: ₹{CI}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")

# Button
Button(window, text="Calculate", font=("EB Garamond",15),
       width=20, bg="white", command=calculate).place(x=250,y=450)

window.mainloop()