# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 13:35:36 2018

@author: Dhillonsher
"""

from tkinter import *
import datetime
import os
import time
import glob
import psutil

window = Tk()
window.title("Printing Thing")
window.geometry("475x403")
window.configure(bg='snow')

def Clear():
  try:
      directory= e1_value.get()
      cdirectory= directory.replace("'\'","'/'")
      os.chdir(cdirectory)
      files=glob.glob('*.pdf')
      for filename in files:
         os.unlink(filename)
      t1.insert(END,"deleting the files at "+str(datetime.datetime.now().strftime("%H:%M:%S"))+"\n")
  except Exception as o:
    t1.insert(END,o)
def Print():
  
  try:
    #user input
    loc = e1_value.get()
    #replace \ with / why???
    floc = loc.replace("'\'","'/'")
    #change directory to pdf folder
    try:
        os.chdir(floc)
        x = 0
        t1.insert(END,"Printing the files at "+str(datetime.datetime.now().strftime("%H:%M:%S"))+"\n")
        for file in glob.glob('*.pdf'):
          if(file != ''):
            os.startfile(file,"print")
            time.sleep(10)
            for p in psutil.process_iter(): #Close Acrobat after printing the PDF
                if 'AcroRd' in str(p):
                   p.kill()
            t2.insert(END,"Printing "+ str(file)+" at "+str(datetime.datetime.now().strftime("%H:%M:%S"))+"\n")
            x = x+1
            #2 sec wait for printing
            time.sleep(2)
    
        t3.insert(END,"no. of files printed:" + str(x))
    except Exception as p:
          t1.insert(END,p)
  
  except Exception as a:
            t1.insert(END,a)  

b1=Button(window,text='Print',command=Print,fg='black',bg='lawn green',height=1,width=20)

b1.grid(row=0,column=0)

b6=Button(window,text='clear',command=Clear,fg='black',bg='lawn green',height=1,width=20)

b6.grid(row=0,column=1)

b2=Button(window,text='Enter Folder location',fg='black',bg='white',height=1,width=20)

b2.grid(row=1,column=0)


b3=Button(window,text='Print and Error Log',fg='black',bg='white',height=10,width=20)

b3.grid(row=5,column=0)


b4=Button(window,text='File Log',fg='black',bg='white',height=10,width=20)

b4.grid(row=9,column=0)


b5=Button(window,text='Final',fg='black',bg='white',height=1,width=20)

b5.grid(row=11,column=0)





e1_value=StringVar()

e1=Entry(window,width=53,textvariable=e1_value,bg='pale turquoise')

e1.grid(row=1,column=1)


t1=Text(window,height=10,width=40,bg='linen')

t1.grid(row=5,column=1)


t2=Text(window,height=10,width=40,bg='old lace')

t2.grid(row=9,column=1)


t3=Text(window,height=1,width=40,bg='floral white')

t3.grid(row=11,column=1)


window.mainloop()
