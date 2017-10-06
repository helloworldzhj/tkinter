from tkinter import *


root = Tk()

textLabel=Label(root,
				text='您所下载的影片有未成年内容，\n请下载后观看！',
				justify = LEFT,
				padx=10)
textLabel.pack(side = LEFT)

photo = PhotoImage(file='123.gif')
imgLabel = Label(root,image=photo)
imgLabel.pack(side = RIGHT)

mainloop()