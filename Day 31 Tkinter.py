from tkinter import *
# creates a tkinter window
window=Tk()

window.title("SmartPlex") #Used to give the title 
window.geometry("1000x1000") #size of window
window.configure(bg="Lightblue")

heading = Label(window, text= "Welcome Users to SmartPlex",font=("EB Garmond",40),bg="white",fg="black")
heading.place(x=100,y=50)
name = Label(window,text= "What are you looking for today?",font=("EB Garmond",20),bg='white',fg='black')
name.place(x=100,y=200)
nameentry = Entry(window,width=35,font=("EB Garmond",20),bg="darkblue",fg="White")
nameentry.place(x=100,y=300)
submitbutton=Button(window,text=("Click me to leave"),bg="red",fg="black",command=window.destroy)
submitbutton.place(x=100,y=600)
window.mainloop()
