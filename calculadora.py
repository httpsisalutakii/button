from tkinter import *

def entrada(valor):
    lb1['text'] += valor

def saida():
    resultado = eval(lb1['text'])

    lb1['text'] = str(resultado)

root = Tk()

lb1 = Label(root, font='Arial 28')

# widgets

bt1 = Button(root, text='7', font='Arial 28', command=lambda: entrada('7'))
bt2 = Button(root, text='8', font='Arial 28', command=lambda: entrada('8'))
bt3 = Button(root, text='9', font='Arial 28', command=lambda: entrada('9'))
bt4 = Button(root, text='+', font='Arial 28', command=lambda: entrada('+'))
bt5 = Button(root, text='4', font='Arial 28', command=lambda: entrada('4'))
bt6 = Button(root, text='5', font='Arial 28', command=lambda: entrada('5'))
bt7 = Button(root, text='6', font='Arial 28', command=lambda: entrada('6'))
bt8 = Button(root, text='-', font='Arial 28', command=lambda: entrada('-'))
bt9 = Button(root, text='1', font='Arial 28', command=lambda: entrada('1'))
bt10 = Button(root, text='2', font='Arial 28', command=lambda: entrada('2'))
bt11 = Button(root, text='3', font='Arial 28', command=lambda: entrada('3'))
bt12 = Button(root, text='x', font='Arial 28', command=lambda: entrada('x'))
bt13 = Button(root, text='0', font='Arial 28', command=lambda: entrada('0'))
bt14 = Button(root, text=',', font='Arial 28', command=lambda: entrada(','))
bt15 = Button(root, text='/', font='Arial 28', command=lambda: entrada('/'))
bt16 = Button(root, text='=', font='Arial 28', command=lambda: saida())
bt17 = Button(root, text='Del', font='Arial 28', command=lambda: entrada('Del'))
bt18 = Button(root, text='C', font='Arial 28', command=lambda: entrada('C'))
bt19 = Button(root, text='(', font='Arial 28', command=lambda: entrada('('))
bt20 = Button(root, text=')', font='Arial 28', command=lambda: entrada(')'))

# layout
lb1.grid(row=0,column=0, columnspan=4, sticky=NSEW)
bt1.grid(row=1, column=0, sticky=NSEW)
bt2.grid(row=1, column=1, sticky=NSEW)
bt3.grid(row=1, column=2, sticky=NSEW)
bt4.grid(row=1, column=3, sticky=NSEW)
bt5.grid(row=2, column=0, sticky=NSEW)
bt6.grid(row=2, column=1, sticky=NSEW)
bt7.grid(row=2, column=2, sticky=NSEW)
bt8.grid(row=2, column=3, sticky=NSEW)
bt9.grid(row=3, column=0, sticky=NSEW)
bt10.grid(row=3, column=1, sticky=NSEW)
bt11.grid(row=3, column=2, sticky=NSEW)
bt12.grid(row=3, column=3, sticky=NSEW)
bt13.grid(row=4, column=0, sticky=NSEW)
bt14.grid(row=4, column=1, sticky=NSEW)
bt15.grid(row=4, column=2, sticky=NSEW)
bt16.grid(row=4, column=3, sticky=NSEW)
bt17.grid(row=5, column=0, sticky=NSEW)
bt18.grid(row=5, column=1, sticky=NSEW)
bt19.grid(row=5, column=2, sticky=NSEW)
bt20.grid(row=5, column=3, sticky=NSEW)

# run

root.mainloop()