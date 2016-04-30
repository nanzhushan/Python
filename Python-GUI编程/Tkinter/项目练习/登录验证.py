#coding:utf8
__author__="knight"
from Tkinter import *

class Reg (Frame):
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.lab1 = Label(frame,text = "用户名:")
        self.lab1.grid(row = 0,column = 0,sticky = W)
        self.ent1 = Entry(frame)

        self.ent1.grid(row = 0,column = 1,sticky = W)
        self.lab2 = Label(frame,text = "密码:")
        self.lab2.grid(row = 1,column = 0)
        self.ent2 = Entry(frame,show = "*")
        self.ent2.grid(row = 1,column = 1,sticky = W)

        self.button = Button(frame,text = "登录",command = self.Submit)        ##绑定Submit事件
        self.button.grid(row = 2,column = 1,sticky = E)

        self.lab3 = Label(frame,text = "")
        self.lab3.grid(row = 3,column = 0,sticky = W)
        self.button2 = Button(frame,text = "取消",command = frame.quit)
        self.button2.grid(row = 3,column = 3,sticky = E)

    def Submit(self):
        s1 = self.ent1.get()         #获取表单提交的值
        s2 = self.ent2.get()
        if s1 == 'knight' and s2 == '123':
            self.lab3["text"] = "登录成功"
        else:
            self.lab3["text"] = "登录失败!"
        self.ent1.delete(0,len(s1))
        self.ent2.delete(0,len(s2))

root = Tk()
root.title("登录框")

app = Reg(root)
root.mainloop()
