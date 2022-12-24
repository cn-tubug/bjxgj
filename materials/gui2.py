#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('班级小管家学霸版v1.0.0')
        self.master.geometry('759x484')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Check2Var = StringVar(value='0')
        self.style.configure('Check2.TCheckbutton',font=('黑体',14))
        self.Check2 = Checkbutton(self.top, text='多选合并', variable=self.Check2Var, style='Check2.TCheckbutton')
        self.Check2.place(relx=0.59, rely=0.116, relwidth=0.159, relheight=0.076)

        self.Check1Var = StringVar(value='0')
        self.style.configure('Check1.TCheckbutton',font=('黑体',14))
        self.Check1 = Checkbutton(self.top, text='获取大题图片链接', variable=self.Check1Var, style='Check1.TCheckbutton')
        self.Check1.place(relx=0.295, rely=0.116, relwidth=0.275, relheight=0.076)

        self.Text2Var = StringVar(value='输出')
        self.Text2 = Entry(self.top, text='输出', textvariable=self.Text2Var, font=('黑体',14))
        self.Text2.place(relx=0.021, rely=0.198, relwidth=0.739, relheight=0.762)

        self.style.configure('Command4.TButton',font=('黑体',14))
        self.Command4 = Button(self.top, text='确认', command=self.Command4_Cmd, style='Command4.TButton')
        self.Command4.place(relx=0.632, rely=0.033, relwidth=0.128, relheight=0.068)

        self.Text1Var = StringVar(value='你的微信OpenID Your OpenID')
        self.Text1 = Entry(self.top, text='你的微信OpenID Your OpenID', textvariable=self.Text1Var, font=('黑体',16))
        self.Text1.place(relx=0.021, rely=0.033, relwidth=0.592, relheight=0.068)

        self.Combo1List = ['Add items in design or code!',]
        self.Combo1 = Combobox(self.top, values=self.Combo1List, font=('黑体',15))
        self.Combo1.place(relx=0.021, rely=0.116, relwidth=0.233, relheight=0.058)
        self.Combo1.set(self.Combo1List[0])

        self.style.configure('Command3.TButton',font=('黑体',15))
        self.Command3 = Button(self.top, text='退出 Exit', command=self.Command3_Cmd, style='Command3.TButton')
        self.Command3.place(relx=0.78, rely=0.876, relwidth=0.202, relheight=0.085)

        self.style.configure('Command2.TButton',font=('黑体',14))
        self.Command2 = Button(self.top, text='网站 Github', command=self.Command2_Cmd, style='Command2.TButton')
        self.Command2.place(relx=0.78, rely=0.76, relwidth=0.202, relheight=0.085)

        self.style.configure('Command1.TButton',font=('黑体',14))
        self.Command1 = Button(self.top, text='帮助 Help', command=self.Command1_Cmd, style='Command1.TButton')
        self.Command1.place(relx=0.78, rely=0.645, relwidth=0.202, relheight=0.085)

        self.style.configure('Line1.TSeparator',background='#000000')
        self.Line1 = Separator(self.top, orient='vertical', style='Line1.TSeparator')
        self.Line1.place(relx=0.769, rely=0.017, relwidth=0.0013, relheight=0.959)

        self.style.configure('Label2.TLabel',anchor='w', font=('黑体',14))
        self.Label2 = Label(self.top, text='左侧为操作台与程序输出      请点帮助获取抓包OpenID        喜欢的话请在GitHub给个Star', style='Label2.TLabel')
        self.Label2.place(relx=0.78, rely=0.132, relwidth=0.202, relheight=0.481)

        self.style.configure('Label1.TLabel',anchor='w', font=('黑体',22))
        self.Label1 = Label(self.top, text='班级小管家', style='Label1.TLabel')
        self.Label1.place(relx=0.78, rely=0.033, relwidth=0.202, relheight=0.068)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command4_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command3_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
