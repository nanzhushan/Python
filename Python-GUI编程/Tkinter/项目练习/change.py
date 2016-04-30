#coding:utf8
from Tkinter import *
def on_click():
    label['text'] = text.get()

root = Tk(className='bitunion')
label = Label(root)
label['text'] = '原文件内容'
label.pack()
text = StringVar()
text.set('你想要改变成什么样子?')
entry = Entry(root)
entry['textvariable'] = text
entry.pack()
button = Button(root)
button['text'] = 'change it'
button['command'] = on_click
button.pack()
root.mainloop()
