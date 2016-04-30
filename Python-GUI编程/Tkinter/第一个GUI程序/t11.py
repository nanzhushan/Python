# coding:utf8
from Tkinter import *
root = Tk()
root.title("hello world")
root.geometry('300x200')
l = Label(root, text="show", bg="green", font=("Arial", 12), width=5, height=2)
l.pack(side=LEFT)  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
root.mainloop()