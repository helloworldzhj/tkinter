from tkinter import *

root = Tk()

def create():
	top = Toplevel()
	top.attributes('-alpha',0.5)
	top.title('fishc demo')

	msg = Message(top,text='i love fishc.com')
	msg.pack()


Button(root,text = '创建顶级窗口',command=create).pack()

mainloop()