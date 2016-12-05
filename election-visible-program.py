# -*- coding: utf-8 -*-
from Tkinter import *
class Election():
    def __init__(self):
        self.rt = Tk()
        self.rt.title("竞选投票可视化程序")                                 #设置窗口名称
        self.minus1 = Button(self.rt,text="-",padx=7,command=self.vote1m)
        self.minus1.grid(row=0,column=0)                                 #设置第一个减号按钮
        self.plus1 = Button(self.rt,text="+",padx=7,command=self.vote1p)
        self.plus1.grid(row=0,column=1)                                  #设置第一个加号按钮
        self.v1 = StringVar()
        self.e1 = Entry(self.rt,textvariable=self.v1)
        self.e1.grid(row=0,column=2,columnspan=2)                        #设置第一个输入框
        self.vt1 = StringVar()
        self.voteShow1 = Label(self.rt,textvariable=self.vt1,relief=RAISED)
        self.voteShow1.grid(row=0,column=4)                              #设置第一个票数显示标签
        self.x1 = 0
        self.vt1.set(self.x1)
        self.piao1 = Label(self.rt,text="票")
        self.piao1.grid(row=0,column=5,sticky=W)
        self.minus2 = Button(self.rt,text="-",padx=7,command=self.vote2m)
        self.minus2.grid(row=1,column=0)                                 #设置第二个减号按钮
        self.plus2 = Button(self.rt,text="+",padx=7,command=self.vote2p)
        self.plus2.grid(row=1,column=1)                                  #设置第二个加号按钮
        self.v2 = StringVar()
        self.e2 = Entry(self.rt,textvariable=self.v2)
        self.e2.grid(row=1,column=2,columnspan=2)                        #设置第二个输入框
        self.vt2 = StringVar()
        self.voteShow2 = Label(self.rt,textvariable=self.vt2,relief=RAISED)
        self.voteShow2.grid(row=1,column=4)                              #设置第二个票数显示标签
        self.x2 = 0
        self.vt2.set(self.x2)
        self.piao2 = Label(self.rt,text="票")
        self.piao2.grid(row=1,column=5,sticky=W)
        self.minus3 = Button(self.rt,text="-",padx=7,command=self.vote3m)
        self.minus3.grid(row=2,column=0)                                 #设置第三个减号按钮
        self.plus3 = Button(self.rt,text="+",padx=7,command=self.vote3p)
        self.plus3.grid(row=2,column=1)                                  #设置第三个加号按钮
        self.v3 = StringVar()
        self.e3 = Entry(self.rt,textvariable=self.v3)
        self.e3.grid(row=2,column=2,columnspan=2)                        #设置第三个输入框
        self.vt3 = StringVar()
        self.voteShow3 = Label(self.rt,textvariable=self.vt3,relief=RAISED)
        self.voteShow3.grid(row=2,column=4)                              #设置第三个票数显示标签
        self.x3 = 0
        self.vt3.set(self.x3)
        self.piao3 = Label(self.rt,text="票")
        self.piao3.grid(row=2,column=5,sticky=W)
        self.minus4 = Button(self.rt,text="-",padx=7,command=self.vote4m)
        self.minus4.grid(row=3,column=0)                                 #设置第四个减号按钮
        self.plus4 = Button(self.rt,text="+",padx=7,command=self.vote4p)
        self.plus4.grid(row=3,column=1)                                  #设置第四个加号按钮
        self.v4 = StringVar()
        self.e4 = Entry(self.rt,textvariable=self.v4)
        self.e4.grid(row=3,column=2,columnspan=2)                        #设置第四个输入框
        self.vt4 = StringVar()
        self.voteShow4 = Label(self.rt,textvariable=self.vt4,relief=RAISED)
        self.voteShow4.grid(row=3,column=4)                              #设置第四个票数显示标签
        self.x4 = 0
        self.vt4.set(self.x4)
        self.piao4 = Label(self.rt,text="票")
        self.piao4.grid(row=3,column=5,sticky=W)
        self.minus5 = Button(self.rt,text="-",padx=7,command=self.vote5m)
        self.minus5.grid(row=4,column=0)                                 #设置第五个减号按钮
        self.plus5 = Button(self.rt,text="+",padx=7,command=self.vote5p)
        self.plus5.grid(row=4,column=1)                                  #设置第五个加号按钮
        self.v5 = StringVar()
        self.e5 = Entry(self.rt,textvariable=self.v5)
        self.e5.grid(row=4,column=2,columnspan=2)                        #设置第五个输入框
        self.vt5 = StringVar()
        self.voteShow5 = Label(self.rt,textvariable=self.vt5,relief=RAISED)
        self.voteShow5.grid(row=4,column=4)                              #设置第五个票数显示标签
        self.x5 = 0
        self.vt5.set(self.x5)
        self.piao5 = Label(self.rt,text="票")
        self.piao5.grid(row=4,column=5,sticky=W)
        self.cv = Canvas(self.rt,width=850,height=600,bg='white')
        self.cv.grid(row=0,rowspan=6,column=6,columnspan=6)              #设置画布
        self.cv.create_line(101,25,101,549,800,549,arrow=BOTH)           #设置坐标轴
        self.cor = range(0,71,10)
        for n in range(0,7+1):
            self.cv.create_line(101+90*n,549,101+90*n,539)               #设置横坐标标示竖线
            self.cv.create_text(101+90*n,550,text=self.cor[n],anchor=N)  #设置横坐标的坐标及间隔
        self.confirmButton = Button(self.rt,text="输入完成",command=self.draw)
        self.confirmButton.grid(row=5,column=1,columnspan=2)             #设置输入完成按钮
        self.clearButton = Button(self.rt,text="清除",command=self.clear)
        self.clearButton.grid(row=5,column=3,columnspan=1)               #设置清除按钮
        self.quitButton = Button(self.rt,text="结束",command=self.rt.quit)
        self.quitButton.grid(row=5,column=4,columnspan=1)                #设置结束按钮
        self.word = []
        self.num = []
        self.rt.mainloop()

    def vote1m(self):                                                    #第一个减号按钮的投票函数
        self.x1 = self.x1-1
        self.vt1.set(self.x1)

    def vote1p(self):                                                    #第一个加号按钮的投票函数
        self.x1 = self.x1+1
        self.vt1.set(self.x1)

    def vote2m(self):                                                    #第二个减号按钮的投票函数
        self.x2 = self.x2-1
        self.vt2.set(self.x2)

    def vote2p(self):                                                    #第二个加号按钮的投票函数
        self.x2 = self.x2+1
        self.vt2.set(self.x2)

    def vote3m(self):                                                    #第三个减号按钮的投票函数
        self.x3 = self.x3-1
        self.vt3.set(self.x3)

    def vote3p(self):                                                    #第三个加号按钮的投票函数
        self.x3 = self.x3+1
        self.vt3.set(self.x3)

    def vote4m(self):                                                    #第四个减号按钮的投票函数
        self.x4 = self.x4-1
        self.vt4.set(self.x4)

    def vote4p(self):                                                    #第四个加号按钮的投票函数
        self.x4 = self.x4+1
        self.vt4.set(self.x4)

    def vote5m(self):                                                    #第五个减号按钮的投票函数
        self.x5 = self.x5-1
        self.vt5.set(self.x5)

    def vote5p(self):                                                    #第五个加号按钮的投票函数
        self.x5 = self.x5+1
        self.vt5.set(self.x5)

    def draw(self):                                                      #可视化函数
        self.word.append(self.v1.get())
        self.word.append(self.v2.get())
        self.word.append(self.v3.get())
        self.word.append(self.v4.get())
        self.word.append(self.v5.get())                                  #建立候选人名单列表
        self.num.append(self.x1)
        self.num.append(self.x2)
        self.num.append(self.x3)
        self.num.append(self.x4)
        self.num.append(self.x5)                                         #建立各候选人票数列表
        a = max(self.num)
        b = self.num.index(a)                                            #找出票数最高的候选人在列表中的位置
        gap = 525/(2*5+1)                                                #计算候选人在纵轴上显示的间距
        for i in range(1,5+1):
            y = 1+(2*i-1)*gap+gap
            if i == b+1:                                                 #画出票数最高的候选人的柱状图并以红色显示
                self.cv.create_text(101,25+(2*i-1)*gap,text=self.word[i-1],anchor=NE)
                self.cv.create_rectangle(101,25+(2*i-1)*gap,102+9.45*self.num[i-1],y,fill="red")
            else:                                                        #画出其他候选人的柱状图并以绿色显示
                self.cv.create_text(101,25+(2*i-1)*gap,text=self.word[i-1],anchor=NE)
                self.cv.create_rectangle(101,25+(2*i-1)*gap,102+9.45*self.num[i-1],y,fill="green")
        self.conclusion1 = Label(self.rt,text="获胜者是")
        self.conclusion1.grid(row=6,column=2,sticky=W)
        self.conclusion2 = Label(self.rt,text=self.word[b])
        self.conclusion2.grid(row=6,column=3,sticky=W)
        self.conclusion3 = Label(self.rt,text="，票数为")
        self.conclusion3.grid(row=6,column=4,sticky=W)
        self.conclusion4 = Label(self.rt,text=a)
        self.conclusion4.grid(row=6,column=5,sticky=W)
        self.conclusion5 = Label(self.rt,text="票！")
        self.conclusion5.grid(row=6,column=6,sticky=W)                   #写出结论，包括获胜者姓名以及最终票数

    def clear(self):                                                     #清除函数
        self.word = []
        self.num = []                                                    #清空候选人名单以及票数列表
        self.v1.set("")
        self.v2.set("")
        self.v3.set("")
        self.v4.set("")
        self.v5.set("")                                                  #清空文本框文字
        self.x1 = 0
        self.vt1.set(self.x1)
        self.x2 = 0
        self.vt2.set(self.x2)
        self.x3 = 0
        self.vt3.set(self.x3)
        self.x4 = 0
        self.vt4.set(self.x4)
        self.x5 = 0
        self.vt5.set(self.x5)                                            #票数清零
        self.cv = Canvas(self.rt,width=850,height=600,bg='white')
        self.cv.grid(row=0,rowspan=6,column=6,columnspan=6)
        for z in range(0,7+1):
            self.cv.create_line(101+90*z,549,101+90*z,539)
            self.cv.create_text(101+90*z,550,text=self.cor[z],anchor=N)  #重新设置横坐标标示竖线及横坐标的坐标与间隔
        self.cv.create_line(101,25,101,549,800,549,arrow=BOTH)           #清空画布上的候选人姓名以及柱状图并重新设置坐标轴
        self.conclusion1.grid_forget()
        self.conclusion2.grid_forget()
        self.conclusion3.grid_forget()
        self.conclusion4.grid_forget()
        self.conclusion5.grid_forget()                                   #清除结论

el = Election()