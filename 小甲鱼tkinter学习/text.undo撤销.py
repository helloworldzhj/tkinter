from tkinter import *
import hashlib

root = Tk()

text = Text(root,width=30,height = 5,undo=True，autoseparators=False)
text.pack()

text.insert(INSERT,'i love fishc.com!')

def callback(event):
	text.edit_seperator()

text.bind('<key>',callback)

def show():
	text.edit_undo()

Button(root,text='撤销',command = show).pack()

mainloop()