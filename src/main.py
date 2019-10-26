import tkinter as tk
from src.Place import *
from src.User import *

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

    #Coleccion de funciones utiles para crear widgets
    def MakeInputBox(self, labelText, x, y):
        tk.Label(self, text=labelText).place(relx=x, rely=y)
        data = tk.StringVar()
        tk.Entry(self, textvariable=data).place(relx=x + 0.1, rely=y)
        return data

    def MakeCheckBox(self, labelText, x, y):
        stateValue = tk.IntVar()
        tk.Checkbutton(self, text=labelText, variable=stateValue, onvalue=1, offvalue=0).place(relx=x, rely=y)
        return stateValue

    def MakeRadioButtom(self, tittleText, val1, val2, x, y):
        tk.Label(self, text=tittleText).place(relx=x, rely=y)
        data = tk.StringVar()
        data.set(val1)
        tk.Radiobutton(self, text=val1, variable=data, value=val1).place(relx=x, rely=y + 0.05)
        tk.Radiobutton(self, text=val2, variable=data, value=val2).place(relx=x + 0.25, rely=y + 0.05)
        return data

    def MakeSpinBox(self, labelText, f, t, x, y):
        tk.Label(self, text=labelText).place(relx=x, rely=y)
        data = tk.IntVar()
        tk.Spinbox(self, from_=f, to=t, textvariable=data).place(relx=x + 0.1, rely=y)
        return data

    def MakeTextBox(self, text, x, y, w, h):
        tb = tk.Text(self, font={'Helvetica', 16})
        tb.insert(tk.INSERT, text)
        tb.config(state="disabled")
        tb.place(relx=x, rely=y, relwidth=w, relheight=h)

    def MakeImage(self, imgsrc, x, y, w, h):
        img = tk.PhotoImage(file=imgsrc)
        imgObj = tk.Label(self, image=img)
        imgObj.image = img
        imgObj.place(relx=x, rely=y, relwidth=w, relheight=h)


#Cada subclase representa un subframde del programa
class MainMenu(tk.Frame):
    def __init__(self, master): #master representa la clase padre, todos las subclases deben incluirlo
        #setup del frame y recursos
        self.master = master
        tk.Frame.__init__(self, self.master)
        #definir logo y titulo de la app
        self.master.title("Aerolinea Arthur Ryan- Proyecto1 Algoritmos")
        logo = tk.PhotoImage(file='../logo_FISC.png')
        self.master.tk.call('wm','iconphoto', self.master._w, logo)

        #Despues de aqui, pon todos los objectos q quieras y recuerda hacer el llamado para hacer el cambio
        self.canvas = tk.Canvas(self, width=1200, height=500, bg='black')
        self.canvas.pack()

        #dibujar bg
        self.DibujarBg("../Mapa_de_Panama_1.png")
        #hacer transicion a siguiente frame
        self.BotonesMapa()

    def DibujarBg(self, src):
        bgMap = tk.PhotoImage(file=src)  # archivo fuente de la imagen del background
        bgImage = tk.Label(self, image=bgMap)
        bgImage.image = bgMap
        bgImage.place(x=0, y=0)

    def BotonesMapa(self):
        tk.Button(self.master, text="Bocas del toro", command=lambda: self.CapturePlace(Bocas)).place(x=40, y=75)
        tk.Button(self.master, text="Coclé", command=lambda: self.CapturePlace(Cocle)).place(x=510, y=230)
        tk.Button(self.master, text="Colón", command=lambda: self.CapturePlace(Colon)).place(x=500, y=130)
        tk.Button(self.master, text="Chiriquí", command=lambda: self.CapturePlace(Chiriqui)).place(x=80, y=230)
        tk.Button(self.master, text="Darién", command=lambda: self.CapturePlace(Darien)).place(x=1000, y=290)
        tk.Button(self.master, text="Herrera", command=lambda: self.CapturePlace(Herrera)).place(x=470, y=350)
        tk.Button(self.master, text="Los Santos", command=lambda: self.CapturePlace(LosSantos)).place(x=510, y=450)
        tk.Button(self.master, text="Panamá", command=lambda: self.CapturePlace(Panama)).place(x=750, y=80)
        tk.Button(self.master, text="Veraguas", command=lambda: self.CapturePlace(Veraguas)).place(x=340, y=300)
        tk.Button(self.master, text="Guna Yala", command=lambda: self.CapturePlace(Guna)).place(x=950, y=60)
        tk.Button(self.master, text="Emberá\n Wounaan", command=lambda: self.CapturePlace(Embera)).place(x=1100, y=250)
        tk.Button(self.master, text="Ngobe Bugle", command=lambda: self.CapturePlace(Ngobe)).place(x=220, y=190)
        tk.Button(self.master, text="Panamá\n Oeste", command=lambda: self.CapturePlace(PanamaOeste)).place(x=620, y=160)

    def CapturePlace(self, lugar):
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
        self.master.MakeImage(self.master.userOption.getImageLink(), 0.025, 0.05, 0.45, 0.7)
        leyendaLugar = tk.Label(self, text="Mapa de " + str(self.master.userOption.Name()), font={'Helvetica', 20,'bold'})
        leyendaLugar.place(relx=0.05, rely=0.8)

        #descripcion del lugar
        self.master.MakeTextBox(self.master.userOption.getDescription(), 0.5, 0.10, 0.48, 0.5)

        #submenu con las zonas del Lugar(cambio a pagina 3)
        self.zones_subMenu = tk.Menubutton(self, text="zonas turisticas disponibles", font={'Arial', 16}, relief=tk.RAISED)
        self.zones_subMenu.menu = tk.Menu(self.zones_subMenu, tearoff=0)
        self.zones_subMenu["menu"] = self.zones_subMenu.menu
        #imprime las 4 Zonas turisticas disponibles en el menu
        self.zones_subMenu.menu.add_command(label=self.master.userOption.getZone(0).Name(), command=lambda: self.CapturePlace(0))
        self.zones_subMenu.menu.add_command(label=self.master.userOption.getZone(1).Name(), command=lambda: self.CapturePlace(1))
        self.zones_subMenu.menu.add_command(label=self.master.userOption.getZone(2).Name(), command=lambda: self.CapturePlace(2))
        self.zones_subMenu.menu.add_command(label=self.master.userOption.getZone(3).Name(), command=lambda: self.CapturePlace(3))
        self.zones_subMenu.place(relx=0.5, rely=0.75)

        #boton de regreso a Menu Principal
        backButtom = tk.Button(self, text="Regresar a MenuPrincipal", command=lambda: self.master.switch_frame(MainMenu))
        backButtom.place(relx=0.0, rely=0.0)

    def CapturePlace(self, userZoneIndex):
        #guarda la zona q el usuario selecciono y cambia a siguiente pantalla
        self.master.userZoneSelected = self.master.userOption.getZone(userZoneIndex)
        print(self.master.userZoneSelected.Name())
        self.master.switch_frame(ZonaMenu)

#clase que maneja las zonas turisticas
class ZonaMenu(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)
        canvas = tk.Canvas(self, width=1000, height=700)
        canvas.pack()

        #título de la pantalla 2
        tk.Label(text='Área turística', font=('Helvetica', '25', 'bold')).place(x=400, y=0)

        #Descripcion de la zona escogida
        self.master.MakeTextBox(self.master.userZoneSelected.getDescription(), 0.5, 0.10, 0.48, 0.5)

        #imagen del lugar
        lugarImg = tk.PhotoImage(file=self.master.userZoneSelected.getImageLink())
        lugarLabel = tk.Label(self, image=lugarImg)
        lugarLabel.image = lugarImg
        lugarLabel.place(relx=0.025, rely=0.085, relwidth=0.45, relheight=0.65)

        # boton de adquirirButtomr productos
        adquirirButtom = tk.Button(self, text="Adquirir Paquete", command= lambda: self.master.switch_frame(UserDataMenu))
        adquirirButtom.place(relx=0.5, rely=0.7)
        # boton de regresar a pantalla anterior
        regresar = tk.Button(self, text="Regresar", command=lambda: self.master.switch_frame(LugarMenu))
        regresar.place(x=5, y=5)


#clase que maneja los datos del usuario y metodo de pagos
class UserDataMenu(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        canvas = tk.Canvas(self, width=1000, height=700)
        canvas.pack()
        tk.Label(self, text="Adquiera su Paquete").place(relx=0.5, rely=0.0)

        # descripcion del zona y paquete seleccionado
        self.master.MakeTextBox(self.master.userZoneSelected.getDescription(), 0.25, 0.1, 0.5, 0.45)

        #widgets para conseguir datos de usuario
        x = 0.01
        y = 0.6
        userName   = self.master.MakeInputBox("Nombre Apellido", x, y)
        id         = self.master.MakeInputBox("Cedula", x, y+0.1)
        country    = self.master.MakeInputBox("Gentilicio", x, y+0.2)
        phone      = self.master.MakeInputBox("Numero de telefono", x, y+0.3)
        jubilado   = self.master.MakeCheckBox("Jubilado?", 0.25, y)
        companions = self.master.MakeSpinBox("N° de acompañantes", 1, 10, 0.25, y+0.1)
        sex        = self.master.MakeRadioButtom("Sexo", "Masculino", "Femenino", 0.25, y+0.2)
        dataArray  = [userName, id, sex, country, phone, companions, jubilado]

        # boton de captura de dato(ABONO) y cambio a siguiente frame
        abonarButtom = tk.Button(self, text="ABONAR", command=lambda: self.CaptureUserData(dataArray, 1))
        abonarButtom.place(relx=0.70, rely=0.80)
        # boton de captura de dato(RESERVAR) y cambio a siguiente frame
        reservaButtom = tk.Button(self, text="RESERVAR", command=lambda: self.CaptureUserData(dataArray, 2))
        reservaButtom.place(relx=0.80, rely=0.80)
        # boton de regreso a Menu Principal
        backButtom = tk.Button(self, text="Regresar a Menu de Zonas", command=lambda: self.master.switch_frame(MainMenu))
        backButtom.place(relx=0.0, rely=0.0)

    def CaptureUserData(self, userData, formaPago):
        #obj que almacena todos los datos del usuario
        self.master.USER = User(userData[0].get(), userData[1].get(), userData[2].get(), userData[3].get(), userData[4].get(), userData[5].get(), userData[6].get())


#main thread, aqui se ejecuta el programa
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()