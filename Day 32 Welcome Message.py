from tkinter import *
from datetime import date

window = Tk()

window.title("Application") #Used to give the title 
window.geometry("1000x1000") #size of window
window.configure(bg="Navy")


def display():
    username = nameentry.get() #to get what the user has entered in the entry box
    message = "Good Morning\nToday's Date is "
    greeting = "Hello, " + username + "\n"
    textbox.insert(END,greeting)
    textbox.insert(END,message)
    textbox.insert(END,date.today())

heading = Label(window, text= "Welcome Aboard",font=("EB Garmond",40),bg="Light Blue",fg="Black")
heading.place(x=100,y=50)

name = Label(window,text= "What do we call you?",font=("EB Garmond",20),bg='Light Blue',fg='Black')
name.place(x=100,y=200)

nameentry = Entry(window,width=35,font=("EB Garmond",20),bg="light blue",fg="Black")
nameentry.place(x=100,y=300)

button = Button(window,text= "Let's go",font=("EB Garmond",10), width=20,bg= "light blue", fg="Black",command=display)
button.place(x=100,y=400)

textbox = Text(window,height=7)
textbox.place(y=500,x=100)


window.mainloop()