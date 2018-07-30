from tkinter import*

def close_window():
	root.destroy()
	exit()


root=Tk()
root.title("OCR Scanner : About")
root.configure(background="white")

photo1=PhotoImage(file="title.gif")
headlabel=Label(root,image=photo1) .grid(row=0,column=0,sticky=S)

labelfont = ('calibri', 12,'bold')
labelfont2 = ('calibri', 12)
buttonfont = ('calibri',12)


title1=Label(root,text="Optical Character Recognition(OCR) Scanner Created By:", bg="white", fg="black",font=labelfont) .grid(row=1,column=0,padx=5, pady=5,sticky=S)
title2=Label(root,text="Deepesh Subedi", bg="white", fg="black",font=labelfont2) .grid(row=2,column=0,padx=5, pady=5,sticky=S)
title3=Label(root,text="Kushal Bhatta", bg="white", fg="black",font=labelfont2) .grid(row=3,column=0,padx=5, pady=5,sticky=S)
title4=Label(root,text="Yugesh Rai", bg="white", fg="black",font=labelfont2) .grid(row=4,column=0,padx=5, pady=5,sticky=S)
button1=Button(root,text="Exit", width=10, command=close_window,font=buttonfont) .grid(row=5,column=0,padx=15, pady=15,sticky=S)


root.mainloop()
