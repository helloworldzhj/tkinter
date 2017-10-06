from tkinter import *

master = Tk()

theLB = Listbox(master,selectmode=EXTENDED)
theLB.pack()

for item in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13',' ','  ','   ']:
	theLB.insert(END,item)

thebutton = Button(master,text='删除它',command=lambda x=theLB:x.delete(ACTIVE))

thebutton.pack()

mainloop()