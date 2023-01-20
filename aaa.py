from tkinter import *

def aumentar():
    if bt3['text'] < 10:
        bt3['text'] += 1

def diminuir():
    if bt3['text'] > -10:
        bt3['text'] -=1

root = Tk()

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.bind('-', lambda event: diminuir())
root.bind('+', lambda event: aumentar())

bt1 = Button(root, text='+', command=aumentar)
bt2 = Button(root, text='-', command=diminuir)
bt3 = Label(root, text=0)

bt1.grid(row=0, column=2, sticky=NSEW)
bt2.grid(row=0, column=0, sticky=NSEW)
bt3.grid(row=0, column=1, sticky=NSEW)

root.mainloop()