# coding=utf-8
'''
  1、 import Tkinter GUI绘制类

  2、 绘制按钮，设置按钮的属性

  3、 向窗口中添加组件，把按钮添加到窗口中

  4、  给按钮绑定事件

'''

import  Tkinter
from tkMessageBox import *

def save_click():
    showinfo('温馨提示','您点击【保存】操作')
def edit_click():
    showinfo('温馨提示','您点击【修改】操作')
def delete_click():
    showinfo('温馨提示','您点击【删除】操作')
def login_click():
    showinfo('温馨提示','您点击【登录】操作')
def cancel_click():
    showinfo('温馨提示','您点击【取消】操作')


root=Tkinter.Tk()

lb_title=Tkinter.Label(root,text='用户名：')
lb_title.pack()

btn_Login=Tkinter.Button(root,text='登录',command=login_click)
btn_Login.pack(side=Tkinter.LEFT)

btn_Cancel=Tkinter.Button(root,text='取消',command=cancel_click)
btn_Cancel.pack(side=Tkinter.RIGHT)

btn_Save=Tkinter.Button(root,
            anchor=Tkinter.E,       #指定对齐方式
            text='保存',           #指定按钮上的文本
            width=40,               #指定按钮宽度，相当于40个字符
            height=5,                #指定按钮高度，相当于5个字符
            command=save_click       #绑定事件
            )
btn_Save.pack()

btn_Edit=Tkinter.Button(root,
            anchor=Tkinter.E,       #指定对齐方式
            text='修改',           #指定按钮上的文本
            width=40,               #指定按钮宽度，相当于40个字符
            height=5,               #指定按钮高度，相当于5个字符
            bg='blue',              #指定按钮背景色
            command=edit_click      #绑定事件
        )
btn_Edit.pack()

btn_Delete=Tkinter.Button(root,
            anchor=Tkinter.E,       #指定对齐方式
            text='删除',           #指定按钮上的文本
            width=40,               #指定按钮宽度，相当于40个字符
            height=5,               #指定按钮高度，相当于5个字符
            bg='blue',              #指定按钮背景色
            state=Tkinter.DISABLED,   #指定按钮为禁用状态
            command=delete_click      #删除事件，被禁用
            )


btn_Delete.pack()
root.mainloop()