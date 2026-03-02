from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename 

window=Tk()

window.title("SmartPlex") #Used to give the title 
window.geometry("1000x1000") #size of window
window.configure(bg="grey")

def openfile():
    filepath=askopenfilename(filetypes=[("Text Files","*.txt")])
    TextBox.delete(1.0,END)
    with open(filepath,"r")as inputfile: #opens the file as readeable file
        text=inputfile.read()   #it will read the content of the file
        TextBox.insert(END,text) #will eneter the text into the text editor
        inputfile.close()

def SaveFile():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[("Text Files","*.txt")])
    with open(filepath,"w")as outputfile: #writes in the new file
        text=TextBox.get(1.0,END)
        outputfile.write(text)


TextBox=Text(window,bg="lightblue",fg="Black")
TextBox.grid(row=0,column=1)
TextBox.place(x=300,y=100)

button = Button(window,text= "Open",font=("EB Garmond",10), width=20,bg= "white", fg="Black",command=openfile)
button.place(x=70,y=100)

button1 = Button(window,text= "Save As...",font=("EB Garmond",10), width=20,bg= "white", fg="Black",command=SaveFile)
button1.place(x=70,y=200)


window.mainloop()

