from tkinter import*
from tkinter import ttk
import sys
import os


def click1():
	os.system('imageGUI.py')

def click2():
	os.system('pdfGUI.py')

def click3():
	os.system('aboutGUI.py')

def close_window():
	root.destroy()
	exit()



root=Tk()
root.title("OCR Scanner")
root.configure(background="white")

photo1=PhotoImage(file="title.gif")
headlabel=Label(root,image=photo1) .grid(row=0,column=0,sticky=S)

labelfont = ('calibri', 14,'bold')
buttonfont = ('calibri',12)

title1=Label(root,text="Image to Text:", bg="white", fg="black",font=labelfont) .grid(row=1,column=0,padx=5, pady=5,sticky=S)

button1=Button(root,text="Convert", width=10, command=click1,font=buttonfont)  .grid(row=2,column=0,padx=5, pady=5,sticky=S)

title2=Label(root,text="PDF to Text:", bg="white", fg="black",font=labelfont) .grid(row=3,column=0,padx=5, pady=5,sticky=S)

button2=Button(root,text="Convert", width=10, command=click2,font=buttonfont)  .grid(row=4,column=0,padx=5, pady=5,sticky=S)

button3=Button(root,text="Exit", width=10, command=close_window,font=buttonfont) .grid(row=5,column=0,padx=15, pady=15,sticky=E)

button4=Button(root,text="About", width=10, command=click3,font=buttonfont) .grid(row=5,column=0,padx=5, pady=5,sticky=W)

root.mainloop()
