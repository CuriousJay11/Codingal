import tkinter as tk
from datetime import date

def age():
    y = int(year.get())
    m = int(month.get())
    d = int(day.get())

    today = date.today()
    a = today.year - y
    if (today.month, today.day) < (m, d):
        a -= 1

    result.config(text="Age: " + str(a))

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Day").pack()
day = tk.Entry(root)
day.pack()

tk.Label(root, text="Month").pack()
month = tk.Entry(root)
month.pack()

tk.Label(root, text="Year").pack()
year = tk.Entry(root)
year.pack()

tk.Button(root, text="Find Age", command=age).pack()

result = tk.Label(root, text="")
result.pack()

root.mainloop()