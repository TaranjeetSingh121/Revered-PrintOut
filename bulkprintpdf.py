# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 00:16:14 2018

@author: Dhillonsher
"""

import os
import time
import glob
import psutil

try:
    #user input
    loc = str(input('enter folder location: '))
    #replace \ with / why???
    floc = loc.replace("'\'","'/'")
    #change directory to pdf folder
    os.chdir(floc)
    x = 0
    
    for file in glob.glob('*.pdf'):
      if(file != ''):
        os.startfile(file,"print")
        time.sleep(10)
        for p in psutil.process_iter(): #Close Acrobat after printing the PDF
            if 'AcroRd' in str(p):
               p.kill()
        print('printing file '+ str(file))
        x = x+1
        #2 sec wait for printing
        time.sleep(2)
    
    print('no. of files printed:' + str(x))

except Exception as a:
   print(a)     