from tkinter import *

window=Tk()

window.title("SmartPlex") #Used to give the title 
window.geometry("300x300") #size of window
window.configure(bg="Lightblue")

def handlekeypress(event):
    print (event.char)
window.bind("<Key>",handlekeypress)

def handleclick():
    print("The Button Was Clicked!")

button = Button(window,text= "Let's go",font=("EB Garmond",10), width=20,bg= "grey", fg="Black",command=handleclick)
button.place(x=70,y=100)
window.mainloop()
