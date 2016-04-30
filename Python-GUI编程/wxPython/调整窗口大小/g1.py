# coding:utf8
# 这样不智能，改变窗口大小，位置不会变，所以不能用绝对位置用相对位置
import wx
app = wx.App()
win = wx.Frame(None, title="Knight Edit", size=(410, 335))
win.Show()
loadButton = wx.Button(win, label='Open',pos=(225, 5), size=(80, 25))
saveButton = wx.Button(win,label='Save', pos=(315, 5), size=(80, 25))
filename = wx.TextCtrl(win, pos=(5, 5), size=(210, 25))

contents = wx.TextCtrl(win, pos=(5, 5), size=(390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)


app.MainLoop()