from tkinter import *

# back-end
# função soma
def soma ():
    if en1.get().isnumeric()) and en2.get().isnumeric():
        lb1['text'] = float(en1.get()) = float(en2.get()))
    else:
        lb1['text'] = 'Valor Invalido'

# front-end
# window
janela = Tk()
#a
# valores constantes
fn = 'Arial 26'

# widgets
lb1 = Label(janela, text='Resultado', font=fn)
en1 = Entry(janela, font=fn)
en2 = Entry(janela, font=fn)
bt1 = Button(janela, text='Soma', font=fn, command=soma)

#layout
lb1.pack()
en1.pack()
en2.pack()
bt1.pack()

# run
janela.mainloop()
