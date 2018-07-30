from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename 
from tkinter.filedialog import asksaveasfile
import PyPDF2
import time

root = Tk(  )
root.title("OCR Scanner : PDF to Text")
root.configure(background="white")

photo1=PhotoImage(file="title.gif")
Label(root,image=photo1) .grid(row=0,column=0,sticky=S)

labelfont = ('calibri', 12,'italic')
labelfont1 = ('calibri', 14,'bold')
buttonfont = ('calibri',12)


def readFpdf():
	path = PathTextBox.get('1.0','end-1c')
	
	if path:
		pdfFileObj = open(path,'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

		num_pages = pdfReader.numPages
		count = 0
		text = ""

		while count < num_pages:
			pageObj = pdfReader.getPage(count)
			count +=1
			text += pageObj.extractText()

			ResultTextBox.delete('1.0',END)
			ResultTextBox.insert(END,text)

			return text
	else:
			ResultTextBox.delete('1.0',END)
			ResultTextBox.insert(END,"File Cannot Be Read!")

	

			

def SaveFile():
	f = asksaveasfile(filetypes=[("Text File", "*.txt"),("Doc File", "*.doc")])
	if f is None: 
		return
	else: 
		text = readFpdf()
		f.write('-------------'+time.asctime()+'------------'+'\n\n'+text+'\n\n')
		f.close()
	
    

def OpenFile():
    name = askopenfilename(filetypes=[("PDF File", "*.pdf")])
    
    PathTextBox.delete("1.0",END)
    PathTextBox.insert(END,name)


def close_window():
    root.destroy()
    exit()

path = StringVar()

HeadLabel1 = Label(root,text="PDF Reader",bg="white", fg="black",font=labelfont1)
HeadLabel1.grid(row = 1,column = 0,sticky=(S))


BrowseButton = Button(root,text="Browse PDF",command = OpenFile,font=buttonfont)
BrowseButton.grid(row=3,column=0,padx=10, pady=10,sticky=(S))

PathLabel = Label(root,text = "Path:",bg="white", fg="black",font=labelfont)
PathLabel.grid(row = 4,column=0,padx=10, pady=10,sticky=(W))

PathTextBox = Text(root,height = 2,bg="light cyan", fg="black",font=buttonfont)
PathTextBox.grid(row = 5,column = 0,sticky=(S))

ReadButton = Button(root,text="Read From PDF",command = readFpdf,font=buttonfont)
ReadButton.grid(row = 6,column = 0,padx=10, pady=10,sticky=(S))

DataLabel = Label(root,text = "Data in PDF:",bg="white", fg="black",font=labelfont)
DataLabel.grid(row = 7,column=0,sticky=(W))

ResultTextBox = Text(root,height = 10,bg="light cyan", fg="black",font=buttonfont)
ResultTextBox.grid(row = 8,column = 0,padx=10, pady=10,sticky=(S))

exitbutton = Button(root,text="Exit", width=10, command=close_window,font=buttonfont) 
exitbutton.grid(row=10,column=0,padx=10, pady=10,sticky=S)

savebutton = Button(root,text="Save",width=10,command=SaveFile,font=buttonfont)
savebutton.grid(row=9,column=0,padx=10,pady=10,sticky=S)



root.mainloop()
