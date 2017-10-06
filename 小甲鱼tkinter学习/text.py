import os
os.chdir('C:/Users/Administrator/Desktop')

from tkinter import *
root = Tk()

text = Text(root,width=300,height=300)
text.pack()

photo = PhotoImage(file='123.gif')



def show():
	text.image_create(END,image=photo)


b1=Button(text,text='点我点我',command=show)
text.window_create(INSERT,window=b1)



mainloop()