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
    boc.place(x=40, y=120)
    coc = Button(root, text="Coclé")
    coc.place(x=510,y=260)
    col = Button(root, text="Colón")
    col.place(x=500, y=170)
    chi = Button(root, text="Chiriquí")
    chi.place(x=80, y=250)
    dar = Button(root, text="Darién")
    dar.place(x=1000, y=310)
    her = Button(root, text="Herrera")
    her.place(x=450, y=390)
    ls = Button(root, text="Los Santos")
    ls.place(x=490, y=470)
    pnm = Button(root, text="Panamá")
    pnm.place(x=730, y=130)
    ver = Button(root, text="Veraguas")
    ver.place(x=340, y=340)
    gy = Button(root, text="Guna Yala")
    gy.place(x=980, y=100)
    ewn = Button(root, text="Emberá\n Wounaan")
    ewn.place(x=1100, y=280)
    nb = Button(root, text="Ngobe Bugle")
    nb.place(x=220, y=230)
    pnmo = Button(root, text="Panamá\n Oeste")
    pnmo.place(x=620, y=190)


background(img, logo)
buttons()
mainloop()

