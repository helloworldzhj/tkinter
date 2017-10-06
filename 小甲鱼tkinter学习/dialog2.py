from tkinter import *
root = Tk()

def callback():
	fileName = filedialog.askopenfilename()
	print(fileName)
	
Button(root,text='open the file',command=callback).pack()

mainloop()











