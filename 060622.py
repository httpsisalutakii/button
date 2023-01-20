from tkinter import *

root = Tk()

fr1 = Frame(root, background='pink')
fr2 = Frame(root, background='black')

lb1 = Label(fr1, text='Label no Frame 1', font='Arial 26')
lb2 = Label(fr2, text='Label no Frame 2', font='Arial 26')
bt1 = Button(fr1, text='Bt no Frame 1', font='Arial 26')
bt2 = Button(fr2, text='Bt no Frame 2', font='Arial 26')

fr1.pack()
fr2.pack()

lb1.grid(row=0, column=0)
bt1.grid(row=1, column=1)
lb2.grid(row=0, column=0)
bt2.grid(row=1, column=1)

root.mainloop()