import os
os.chdir('C:/Users/Administrator/Desktop')

from tkinter import *
root = Tk()

photo = PhotoImage(file='123.gif')
theLabel = Label(root,
				text= '学python\n到fishc',
				justify = LEFT,
				image = photo,
				compound = CENTER,
				font=('楷书',20),
				fg='black')

theLabel.pack()

mainloop()