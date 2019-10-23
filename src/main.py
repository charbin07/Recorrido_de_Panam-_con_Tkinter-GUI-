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
        self.boc = tk.Button(self.master, text="Bocas del toro", command=lambda: self.DetectarColision(Bocas))
        self.boc.place(x=40, y=75)
        self.coc = tk.Button(self.master, text="Coclé", command=lambda: self.DetectarColision(Cocle))
        self.coc.place(x=510, y=230)
        self.col = tk.Button(self.master, text="Colón", command=lambda: self.DetectarColision(Colon))
        self.col.place(x=500, y=130)
        self.chi = tk.Button(self.master, text="Chiriquí", command=lambda: self.DetectarColision(Chiriqui))
        self.chi.place(x=80, y=230)
        self.dar = tk.Button(self.master, text="Darién", command=lambda: self.DetectarColision(Darien))
        self.dar.place(x=1000, y=290)
        self.her = tk.Button(self.master, text="Herrera", command=lambda: self.DetectarColision(Herrera))
        self.her.place(x=470, y=350)
        self.ls = tk.Button(self.master, text="Los Santos", command=lambda: self.DetectarColision(LosSantos))
        self.ls.place(x=510, y=450)
        self.pnm = tk.Button(self.master, text="Panamá", command=lambda: self.DetectarColision(Panama))
        self.pnm.place(x=750, y=80)
        self.ver = tk.Button(self.master, text="Veraguas", command=lambda: self.DetectarColision(Veraguas))
        self.ver.place(x=340, y=300)
        self.gy = tk.Button(self.master, text="Guna Yala", command=lambda: self.DetectarColision(Guna))
        self.gy.place(x=950, y=60)
        self.ewn = tk.Button(self.master, text="Emberá\n Wounaan", command=lambda: self.DetectarColision(Embera))
        self.ewn.place(x=1100, y=250)
        self.nb = tk.Button(self.master, text="Ngobe Bugle", command=lambda: self.DetectarColision(Ngobe))
        self.nb.place(x=220, y=190)
        self.pnmo = tk.Button(self.master, text="Panamá\n Oeste", command=lambda: self.DetectarColision(PanamaOeste))
        self.pnmo.place(x=620, y=160)

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

        #imagen del Lugar
        lugarImg = tk.PhotoImage(file=self.master.userOption.getImageLink())
        lugarLabel = tk.Label(self, image=lugarImg)
        lugarLabel.image = lugarImg
        lugarLabel.place(relx=0.025, rely=0.05, relwidth=0.45,relheight=0.7)
        leyendaLugar = tk.Label(self, text="Mapa de " + str(self.master.userOption.Name()), font={'Helvetica', 20,'bold'})
        leyendaLugar.place(relx=0.05, rely=0.8)

        #descripcion del lugar
        descriptionTextBox = tk.Text(self, font={'Helvetica', 12, 'justify'})
        descriptionTextBox.insert(tk.INSERT, self.master.userOption.getDescription())
        descriptionTextBox.config(state="disabled")

        descriptionTextBox.place(relx=0.5, rely=0.10, relwidth=0.48, relheight=0.5)

        descriptionTextBox.place(relx=0.5, rely=0.10, relwidth=0.48, relheight=0.4)


        #submenu con las zonas del Lugar(cambio a pagina 3)
        self.zones_subMenu = tk.Menubutton(self, text="zonas turisticas disponibles", font={'Arial', 16}, relief=tk.RAISED)
        self.zones_subMenu.menu = tk.Menu(self.zones_subMenu, tearoff=0)
        self.zones_subMenu["menu"] = self.zones_subMenu.menu
        #imprime las 4 Zonas turisticas disponibles en el menu
        self.zones_subMenu.menu.add_command(label=self.master.userOption.getZone(0).Name(), command=lambda: self.DetectarColision(0))
        self.zones_subMenu.menu.add_command(label=self.master.userOption.getZone(1).Name(), command=lambda: self.DetectarColision(1))
        self.zones_subMenu.menu.add_command(label=self.master.userOption.getZone(2).Name(), command=lambda: self.DetectarColision(2))
        self.zones_subMenu.menu.add_command(label=self.master.userOption.getZone(3).Name(), command=lambda: self.DetectarColision(3))
        self.zones_subMenu.place(relx=0.5, rely=0.75)

        #boton de regreso a Menu Principal
        backButtom = tk.Button(self, text="Regresar a MenuPrincipal", command=lambda: self.master.switch_frame(MainMenu))
        backButtom.place(relx=0.0, rely=0.0)



    def DetectarColision(self, userZoneIndex):
        #guarda la zona q el usuario selecciono y cambia a siguiente pantalla
<<<<<<< HEAD

        self.master.userZoneSelected = self.master.userOption.getZone(userZoneIndex)
        #print(self.master.userZoneSelected.Name())
        self.master.switch_frame(UserMenu)

        self.userZoneSelected = self.master.userOption.getZone(userZoneIndex)
        print(self.userZoneSelected.Name())
        self.master.switch_frame(UserMenu)
=======
        self.master.zone = self.master.userOption.getZone(userZoneIndex)
        print(self.master.zone.Name())
        self.master.switch_frame(Pantalla3)

>>>>>>> dev



#clase que maneja las zonas turisticas
class Pantalla3(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        canvas = tk.Canvas(self, width=1000, height=600)
        canvas.pack()

        self.master = master
        tk.Frame.__init__(self, self.master)
        canvas = tk.Canvas(self, width=1000, height=700)
        canvas.pack()


        tk.Label(self, text="Adquiera su Paquete", font={}).place(relx=0.5, rely=0.0)

        # descripcion del zona y paquete seleccionado
        descriptionTextBox = tk.Text(self, font={'Helvetica', 12, 'justify'})
        descriptionTextBox.insert(tk.INSERT, self.master.zone.getDescription())
        descriptionTextBox.config(state="disabled")
        descriptionTextBox.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.45)

        #widgets para conseguir datos de usuario
        x = 0.01
        y = 0.6
        userName = self.MakeInputBox("Nombre Apellido", "Guardar", x, y)
        id = self.MakeInputBox("Cedula", "Guardar", x, y+0.1)
        country = self.MakeInputBox("Gentilicio", "Guardar", x, y+0.2)
        phone = self.MakeInputBox("Numero de telefono", "Guardar", x, y+0.3)


        # boton de regreso a Menu Principal
        backButtom = tk.Button(self, text="Regresar a Menu de Zonas", command=lambda: self.master.switch_frame(MainMenu))
        backButtom.place(relx=0.0, rely=0.0)

    def MakeInputBox(self, labelText, buttomText, x, y):
        tk.Label(self, text=labelText).place(relx=x, rely=y)
        entry = tk.Entry(self)
        entry.place(relx=x+0.1, rely=y)
        #tk.Button(self, text=buttomText, command=lambda: self.saveValues(entry)).place(relx=x+0.25, rely=y)

    # def saveValues(self, entry):
    #     pass

    #def MakeCheckBox(self, labelText, x, y):



        #título de la pantalla 2
        titulo = tk.Label(text=self.master.userZoneSelected.Name(), font=('Helvetica', '25', 'bold'))
        titulo.place(x=400, y=3)
        #boton de regresar a pantalla anterior
        regresar = tk.Button(self, text="Regresar", command=lambda: master.switch_frame(LugarMenu))
        regresar.place(x=5, y=5)
        #boton de adquirir productos
        adquiri = tk.Button(self, text = "Adquirir Paquete")
        adquiri.place(x = 400, y= 600)
        #caja de texto
        descriptionTextBox = tk.Text(self, font={'Helvetica', 14, 'justify'})
        descriptionTextBox.insert(tk.INSERT, self.master.userZoneSelected.getDescription())
        descriptionTextBox.config(state="disable")
        descriptionTextBox.place(relx=0.5, rely=0.10, relwidth=0.48, relheight=0.5)
        #imagen del lugar
        lugarImg = tk.PhotoImage(file=self.master.userZoneSelected.getImageLink())
        lugarLabel = tk.Label(self, image=lugarImg)
        lugarLabel.image = lugarImg
        lugarLabel.place(relx=0.025, rely=0.085, relwidth=0.45, relheight=0.65)

#main thread, aqui se ejecuta el programa
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()