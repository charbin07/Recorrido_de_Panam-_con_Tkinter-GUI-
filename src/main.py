import tkinter as tk
from src.Place import *

#Clase base que controla los frames, recursos y switches del programa
class SampleApp(tk.Tk):
    def __init__(self):
        #setea tkinter
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(MainMenu) #frame por defecto

    def switch_frame(self, frame_class):
        #Destruye el frame actual y lo reemplaza con uno nuevo
        new_frame = frame_class(self)#setea el nuevo frame
        if self._frame is not None:
            self._frame.destroy()#destruye el actual
        #invoca el frame en pantalla
        self._frame = new_frame
        self._frame.pack()

#Cada subclase representa un subframde del programa
class MainMenu(tk.Frame):
    def __init__(self, master):
        #setup del frame y recursos
        self.master = master
        self.master.title("Aerolinea Arthur Ryan -MenuPrincipal")
        logo = tk.PhotoImage(file='../logo_FISC.png')
        self.master.tk.call('wm','iconphoto', self.master._w, logo)
        bgMap = tk.PhotoImage(file="../Mapa_de_Panama_1.png")  # archivo fuente de la imagen del background

        tk.Frame.__init__(self, self.master)
        self.canvas = tk.Canvas(self, width=1200, height=500, bg='black')
        self.canvas.pack()
        #dibujar bg
        bgImage = tk.Label(self, image=bgMap)
        bgImage.image = bgMap
        bgImage.place(x=0, y=0)
        #Despues de aqui, pon todos los objectos q quieras y recuerda hacer el llamado para hacer el cambio
        self.BotonesMapa()
        # tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        # tk.Button(self, text="Open page one",
        #           command=lambda: master.switch_frame(LugarMenu)).pack()
        # tk.Button(self, text="Open page two",
        #           command=lambda: master.switch_frame(PageTwo)).pack()

    def BotonesMapa(self):
        boc = tk.Button(self.master, text="Bocas del toro")
        boc.place(x=40, y=75)
        coc = tk.Button(self.master, text="Coclé")
        coc.place(x=510, y=230)
        col = tk.Button(self.master, text="Colón")
        col.place(x=500, y=130)
        chi = tk.Button(self.master, text="Chiriquí")
        chi.place(x=80, y=230)
        self.dar = tk.Button(self.master, text="Darién", command=lambda: self.DetectarColision(Darien))
        self.dar.place(x=1000, y=290)
        self.her = tk.Button(self.master, text="Herrera", command=lambda: self.DetectarColision(Herrera))
        self.her.place(x=470, y=350)
        self.ls = tk.Button(self.master, text="Los Santos", command=lambda: self.DetectarColision(LosSantos))
        self.ls.place(x=510, y=450)
        pnm = tk.Button(self.master, text="Panamá")
        pnm.place(x=730, y=100)
        ver = tk.Button(self.master, text="Veraguas")
        ver.place(x=340, y=300)
        gy = tk.Button(self.master, text="Guna Yala")
        gy.place(x=980, y=80)
        ewn = tk.Button(self.master, text="Emberá\n Wounaan")
        ewn.place(x=1100, y=250)
        nb = tk.Button(self.master, text="Ngobe Bugle")
        nb.place(x=220, y=190)
        pnmo = tk.Button(self.master, text="Panamá\n Oeste")
        pnmo.place(x=620, y=160)

    def DetectarColision(self, lugar):
        self.master.userOption = lugar
        print(self.master.userOption.Name())
        self.master.switch_frame(LugarMenu)




#Esta frame se activa al seleccionar un Lugar del mapa
class LugarMenu(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Aerolinea Arthur Ryan -LugarMenu")
        logo = tk.PhotoImage(file='../logo_FISC.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, logo)
        tk.Frame.__init__(self, self.master)
        canvas = tk.Canvas(self, width=1200, height=700)
        canvas.pack()

        # Despues de aqui, pon todos los objectos q quieras y recuerda hacer el llamado para hacer el cambio

        lugarImg = tk.PhotoImage(file=self.master.userOption.getImageLink())
        lugarLabel = tk.Label(self, image=lugarImg)
        lugarLabel.image = lugarImg
        lugarLabel.place(relx=0.05, rely=0.1)

        backButtom = tk.Button(self, text="Regresar a MenuPrincipal", command=lambda: master.switch_frame(MainMenu))
        backButtom.place(relx=0.0, rely=0.0)


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        canvas = tk.Canvas(self, width=100, height=200)
        canvas.pack()
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(MainMenu)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()