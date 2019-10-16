from tkinter import *
from tkinter import PhotoImage
root = Tk()
img = PhotoImage(file="Comarca_Emberá.png") # archivo fuente de la imagen del background
logo = PhotoImage(file='logo_FISC.png')


def background(img, logo):
    root.title("Prueba")
    root.resizable(False, False)
    root.tk.call('wm', 'iconphoto', root._w, logo)
    canv = Canvas(root, width=1200, height=587, bg='white')
    canv.grid(row=2, column=3)
    """canvas de la ventana, donde se setean las coordenadas de la imagen y alineación"""
    canv.create_image(600, 293.5, anchor=CENTER, image=img)


background(img, logo)
mainloop()

