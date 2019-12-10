from tkinter import *
window = Tk()
window.title("Printing Thing")
window.geometry("500x400")

def Print():
  
  t1.insert(END,"Printing the files")

b1=Button(window,text='Print',command=Print)
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)


window.mainloop()
