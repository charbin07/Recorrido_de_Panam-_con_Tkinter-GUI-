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
    def __init__(self, master): #master representa la clase padre, todos las subclases deben incluirlo
        #setup del frame y recursos
        self.master = master# de esta forma de incluye
        self.master.title("Aerolinea Arthur Ryan- Proyecto1 Algoritmos")
        logo = tk.PhotoImage(file='../logo_FISC.png')
        self.master.tk.call('wm','iconphoto', self.master._w, logo)

        tk.Frame.__init__(self, self.master)
        self.canvas = tk.Canvas(self, width=1200, height=500, bg='black')
        self.canvas.pack()
        #dibujar bg
        bgMap = tk.PhotoImage(file="../Mapa_de_Panama_1.png")  # archivo fuente de la imagen del background
        bgImage = tk.Label(self, image=bgMap)
        bgImage.image = bgMap
        bgImage.place(x=0, y=0)
        #Despues de aqui, pon todos los objectos q quieras y recuerda hacer el llamado para hacer el cambio
        self.BotonesMapa()

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

        tk.Frame.__init__(self, self.master)
        canvas = tk.Canvas(self, width=1200, height=700)
        canvas.pack()

        # Despues de aqui, pon todos los objectos q quieras y recuerda hacer el llamado para hacer el cambio
        #imagen del Lugar
        lugarImg = tk.PhotoImage(file=self.master.userOption.getImageLink())
        lugarLabel = tk.Label(self, image=lugarImg)
        lugarLabel.image = lugarImg
        lugarLabel.place(relx=0.025, rely=0.05, relwidth=0.45,relheight=0.7)
        leyendaLugar = tk.Label(self, text="Mapa de " + str(self.master.userOption.Name()), font={'Helvetica', 20, 'bold'})
        leyendaLugar.place(relx=0.05, rely=0.8)

        #descripcion del lugar
        descriptionTextBox = tk.Text(self, font={'Helvetica', 14, 'justify'})
        descriptionTextBox.insert(tk.INSERT, self.master.userOption.getDescription())
        descriptionTextBox.config(state="disabled")
        descriptionTextBox.place(relx=0.5, rely=0.10, relwidth=0.48, relheight=0.5)

        #submenu con las zonas del Lugar(cambio a pagina 3)
        self.zones_subMenu = tk.Menubutton(self, text="zonas disponibles", font={'Arial', 16}, relief=tk.RAISED)
        self.zones_subMenu.menu = tk.Menu(self.zones_subMenu, tearoff=0)
        self.zones_subMenu["menu"] = self.zones_subMenu.menu

        self.zones_subMenu.menu.add_command(label='zona1', command=lambda: self.DetectarColision())
        self.zones_subMenu.menu.add_command(label='zona2', command=lambda: self.DetectarColision())
        self.zones_subMenu.menu.add_command(label='zona3', command=lambda: self.DetectarColision())
        self.zones_subMenu.menu.add_command(label='zona4', command=lambda: self.DetectarColision())
        self.zones_subMenu.place(relx=0.5, rely=0.75)

        #boton de regreso a Menu Principal
        backButtom = tk.Button(self, text="Regresar a MenuPrincipal", command=lambda: self.master.switch_frame(MainMenu))
        backButtom.place(relx=0.0, rely=0.0)

    def DetectarColision(self):
        self.master.switch_frame(PageTwo)

#clase que maneja las zonas turisticas
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        canvas = tk.Canvas(self, width=1000, height=600)
        canvas.pack()
        #título de la pantalla 2
        titulo = tk.Label(text='Área turística', font=('Helvetica', '30', 'bold'))
        titulo.place(x=400, y=0)
        #boton de regresar a pantalla anterior
        regresar = tk.Button(self, text="Regresar", command=lambda: master.switch_frame(LugarMenu))
        regresar.place(x=5, y=5)
        #boton de adquirir productos
        adquiri = tk.Button(self, text = "Adquirir Paquete")
        adquiri.place(x = 400, y= 500)
        #caja de texto
        descriptionTextBox = tk.Text(self, font={'Helvetica', 14, 'justify'})
        descriptionTextBox.config(state="disabled")
        descriptionTextBox.place(relx=0.5, rely=0.10, relwidth=0.48, relheight=0.5)

#main thread, aqui se ejecuta el programa
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()