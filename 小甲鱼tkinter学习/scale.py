from tkinter import *

root = Tk()

s1 = Scale(root,from_=0,to=42,tickinterval=5,resolution=5,length=200)
s1.pack()
s2 = Scale(root,from_=0,to=200,tickinterval=10,length=500,orient=HORIZONTAL)
s2.pack()


def show():
	print(s1.get(),s2.get())

Button(root,text='获取位置',command=show).pack()





mainloop()