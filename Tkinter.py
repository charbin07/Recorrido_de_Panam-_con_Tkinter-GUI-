from tkinter import *
from tkinter import PhotoImage
root = Tk()
img = PhotoImage(file="Mapa_de_Panama_1.png") # archivo fuente de la imagen del background
logo = PhotoImage(file='logo_FISC.png')


def background(img, logo):
    root.title("Prueba")
    root.resizable(True, True)
    root.tk.call('wm', 'iconphoto', root._w, logo)
    canv = Canvas(root, width=1200, height=587, bg='white')
    canv.grid(row=2, column=3)
    """canvas de la ventana, donde se setean las coordenadas de la imagen y alineación"""
    canv.create_image(600, 293.5, anchor=CENTER, image=img)


def buttons():
    boc = Button(root, text="Bocas del toro")
    boc.place(x=50, y=120)
    coc = Button(root, text="Coclé")
    coc.place(x=360, y=340)
    col = Button(root, text="Colón")
    col.place(x=500, y=170)
    chi = Button(root, text="Chiriquí")
    chi.place(x=90, y=250)
    dar = Button(root, text="Darién")
    dar.place(x=1000, y=310)
    her = Button(root, text="Herrera")
    her.place(x=100, y=100)
    ls = Button(root, text="Los Santos")
    ls.place(x=100, y=100)
    pnm = Button(root, text="Panamá")
    pnm.place(x=100, y=100)
    ver = Button(root, text="Veraguas")
    ver.place(x=100, y=100)
    gy = Button(root, text="Guna Yala")
    gy.place(x=100, y=100)
    ewn = Button(root, text="Emberá\n Wounaan")
    ewn.place(x=100, y=100)
    nb = Button(root, text="Ngobe Bugle")
    nb.place(x=100, y=100)
    pnmo = Button(root, text="Panamá Oeste")
    pnmo.place(x=100, y=100)


background(img, logo)
buttons()
mainloop()

