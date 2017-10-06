import os
os.chdir('C:/Users/Administrator/Desktop')

from tkinter import *
root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('您所下载的影片有未成年内容，\n请下载后观看！')

def callback():
	var.set('吹吧，我才不信呢！！！！！')




textLabel=Label(frame1,
				textvariable=var,
				justify = LEFT,)
textLabel.pack(side = LEFT)

photo = PhotoImage(file='123.gif')
imgLabel = Label(frame1,image=photo)
imgLabel.pack(side = RIGHT)

theButton = Button(frame2,text='我已满十八岁',command=callback)
theButton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)


mainloop()