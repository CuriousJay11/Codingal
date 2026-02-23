from tkinter import *
# creates a tkinter window
window=Tk()

window.title("KeyPad") #Used to give the title 
window.geometry("350x400") #size of window
window.configure(bg="Dark Grey")

keys = [[1,2,3],
        [4,5,6],
        [7,8,9],
        ["#",0,"*"]]

y = 80

for row in keys:
    x = 80   # starting x position for each row
    for i in row:
        button = Button(window,
                        text=i,
                        font=("Arial",10),
                        width=5,
                        bg="light grey",
                        fg="black")
        button.place(x=x, y=y)
        x = x + 70   # move right
    y = y + 70       # move down






window.mainloop()