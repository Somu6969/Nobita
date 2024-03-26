import time 
import tkinter as chodu
while True:
  #t=time.strftime("%H:%M:%S")
  #print(t,"\r",end="")
  #time.sleep(1)
  

  
  root=chodu.Tk()
  root.geometry("1000x1000")
  root.title("Clock")
  label=chodu.Label(root,text=t,font=("times",50),bg="blacK",fg="pink")
  label.pack(anchor=chodu.CENTER)
  root.mainloop()
  #tkinter means a graphical user interface
  #Tkinter is the standard Python interface to the Tk GUI toolkit shipped with Python. It is Python's de fact
  #root means the main window
  #geometry means the size of the window
  #label means the text in the window
  #font means the font of the text
  #titile means the title of the window
  #bg means the background color
  #fg means the foreground color
  #pack means the position of the text
  #times means the font  size of the text
  #anchor means the position of the text
  #mainloop means the loop of the window