import tkinter as tk
from src.Place import *
from src.User import *
from dataclasses import dataclass
#struct q almacena informacion acerca de las compras de un usuario
#me permite crear el carrito de compras
@dataclass
class Comprador:
    userName: str
    compas: int
    zone: str
    payMethod: str
    totalPrice: float

listaDeCompradores = []

#constantes
DESCUENTO_JUBILADO        = 10/100.0
DESCUENTO_PERSONAS        = 15/100.0
DESCUENTO_COMPRA_SUPERIOR = 5/100.0


#Clase base que controla los frames, recursos y switches del programa

class SampleApp(tk.Tk):
    def __init__(self):
        #setea tkinter
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(PresentationFrame) #frame por defecto

    def switch_frame(self, frame_class):
        #Destruye el frame actual y lo reemplaza con uno nuevo
        new_frame = frame_class(self)#setea el nuevo frame
        if self._frame is not None:
            self._frame.destroy()#destruye el actual
        #invoca el frame en pantalla
        self._frame = new_frame
        self._frame.pack()

    #Coleccion de funciones utiles para crear widgets
    def MakeButtom(self, textField, _x, _y, callbackFunc, *args):
        tk.Button(self.master, text=textField, command=lambda: callbackFunc(*args)).place(x=_x, y=_y)

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

#Cada subclase q herede de tk.Frame representa un frame de del programa
class PresentationFrame(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.master.title("Kalidoso Tours- Proyecto1 Algoritmos")
        logo = tk.PhotoImage(file='../logo_FISC.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, logo)

        self.canvas = tk.Canvas(self, width=1000, height=500)
        self.canvas.pack()
        #informacion referente a presentacion
        y = 5
        tk.Label(self, text="Universidad Tecnológica de Panamá\n\nProyecto#1: Algoritmo como estrategia para la solución de problemas\n\nFacilitador: Ing. Samuel Jiménez\n\nIntegrantes:\n\nXavier Lamela 8-956-720\nClyde Harbin 8-927-1305\nLuis Chávez 8-947-1001\nCarlos Bernal 8-896-2198\n\nSemetre 2, 2019\n\nFecha: 30 de octubre de 2019", font=('Helvetica', '10', 'bold')).place(x=290, y=100)

        self.master.MakeImage('../logo_FISC.png', 0, 0, 0.25, 0.25)
        # boton para cerrar el programa
        tk.Button(self, text="Continuar", command=lambda: self.master.switch_frame(MainMenu)).place(relx=0.48, rely=0.85)


#Esta es el frame  de entrada del programa
class MainMenu(tk.Frame):
    def __init__(self, master): #master representa la clase padre, todos las subclases deben incluirlo
        #setup del frame y recursos
        self.master = master
        tk.Frame.__init__(self, self.master)
        #definir logo y titulo de la app
        self.master.title("Kalidoso Tours- Proyecto1 Algoritmos")
        logo = tk.PhotoImage(file='../logo_FISC.png')
        self.master.tk.call('wm','iconphoto', self.master._w, logo)

        #Despues de aqui, pon todos los objectos q quieras y recuerda hacer el llamado para hacer el cambio
        self.canvas = tk.Canvas(self, width=1200, height=500)
        self.canvas.pack()

        #dibujar bg
        self.DibujarBg("../Mapa_de_Panama_1.png")

        #accede a lista de compradores
        self.master.MakeButtom("Carrito", 1100, 5, self.PrintLista)

        #hacer transicion a siguiente frame
        self.BotonesMapa()

        #boton para cerrar el programa
        tk.Button(self, text="Quit", command=self.CloseApp).place(relx=0.96, rely=0.01)

    def DibujarBg(self, src):
        bgMap = tk.PhotoImage(file=src)  # archivo fuente de la imagen del background
        bgImage = tk.Label(self, image=bgMap)
        bgImage.image = bgMap
        bgImage.place(x=0, y=0)

    def BotonesMapa(self):
        tk.Button(self.master, text="Bocas del toro", command=lambda: self.CapturePlace(Bocas)).place(x=30, y=70)
        tk.Button(self.master, text="Coclé", command=lambda: self.CapturePlace(Cocle)).place(x=510, y=230)
        tk.Button(self.master, text="Colón", command=lambda: self.CapturePlace(Colon)).place(x=500, y=130)
        tk.Button(self.master, text="Chiriquí", command=lambda: self.CapturePlace(Chiriqui)).place(x=80, y=210)
        tk.Button(self.master, text="Darién", command=lambda: self.CapturePlace(Darien)).place(x=1000, y=290)
        tk.Button(self.master, text="Herrera", command=lambda: self.CapturePlace(Herrera)).place(x=450, y=350)
        tk.Button(self.master, text="Los Santos", command=lambda: self.CapturePlace(LosSantos)).place(x=510, y=420)
        tk.Button(self.master, text="Panamá", command=lambda: self.CapturePlace(Panama)).place(x=750, y=80)
        tk.Button(self.master, text="Veraguas", command=lambda: self.CapturePlace(Veraguas)).place(x=340, y=300)
        tk.Button(self.master, text="Guna Yala", command=lambda: self.CapturePlace(Guna)).place(x=950, y=60)
        tk.Button(self.master, text="Emberá\n Wounaan", command=lambda: self.CapturePlace(Embera)).place(x=1100, y=250)
        tk.Button(self.master, text="Ngobe Bugle", command=lambda: self.CapturePlace(Ngobe)).place(x=220, y=190)
        tk.Button(self.master, text="Panamá\n Oeste", command=lambda: self.CapturePlace(PanamaOeste)).place(x=620, y=160)

    def PrintLista(self):
        top = tk.Toplevel(width=700, height=200, bg='gray', bd=1)
        x = 10
        tk.Label(top, text="USUARIO\t\tCOMPAÑIA\tZONA\t\tFORMA DE PAGO\t\tTOTAL", font=('Helvetica', '10', 'bold')).place(x=x, y=25)
        y = 25
        if listaDeCompradores != 0:
            for comprador in listaDeCompradores:
                y += 30
                tk.Label(top, fg='green', text=comprador.userName +"\t\t\t" +
                                   str(comprador.compas) +"\t\t"+
                                   comprador.zone + "\t\t" +
                                   comprador.payMethod +"\t\t" +
                                   str(comprador.totalPrice),
                         font=('Helvetica', '10', 'bold')).place(x=x, y=y)
        top.mainloop()

    def CapturePlace(self, lugar):
        self.master.userOption = lugar
        print(self.master.userOption.Name())
        self.master.switch_frame(LugarMenu)

    def CloseApp(self):
        self.master.quit()


#Esta frame se activa al seleccionar un Lugar del mapa
class LugarMenu(tk.Frame):
    def __init__(self, master):
        self.master = master

        tk.Frame.__init__(self, self.master)
        canvas = tk.Canvas(self, width=1000, height=700)
        canvas.pack()

        # título de la pantalla Menu
        tk.Label(text=self.master.userOption.Name(), font=('Helvetica', '25', 'bold')).place(x=500, y=0)

        #imagen del Lugar7
        self.master.MakeImage(self.master.userOption.getImageLink(),  0.025, 0.10, 0.45, 0.5)


        #descripcion de provincia 0 comarca
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
        self.zones_subMenu.place(relx=0.65, rely=0.65)

        #boton de regreso a Menu Principal
        backButtom = tk.Button(self, text="< Regresar a MenuPrincipal", command=lambda: self.master.switch_frame(MainMenu))
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
        tk.Label(text=self.master.userZoneSelected.Name(), font=('Helvetica', '25', 'bold')).place(x=400, y=0)

        #Descripcion de la zona escogida
        self.master.MakeTextBox(self.master.userZoneSelected.getDescription(), 0.5, 0.10, 0.45, 0.5)
        #imagen de la zona seleccionada
        self.master.MakeImage(self.master.userZoneSelected.getImageLink(), 0.025, 0.10, 0.45, 0.5)

        # boton de adquirirButtomr productos
        adquirirButtom = tk.Button(self, text="Adquirir Paquete", command=lambda: self.master.switch_frame(UserDataMenu))
        adquirirButtom.place(relx=0.65, rely=0.65)
        # boton de regresar a pantalla anterior
        tk.Button(self, text="< Regresar", command=lambda: self.master.switch_frame(LugarMenu)).place(x=5, y=5)


#clase que maneja los datos del usuario y metodo de pagos
class UserDataMenu(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        canvas = tk.Canvas(self, width=1000, height=700)
        canvas.pack()
        tk.Label(self, text="Adquiera su Paquete", font=('Helvetica', '25', 'bold')).place(x=400, y=0)

        # descripcion de zona y precio de paquete seleccionado
        self.master.MakeTextBox(self.master.userZoneSelected.getDescription() + "Precio x Persona:$" + str(self.master.userZoneSelected.getPrice()), 0.15, 0.1, 0.75, 0.45)

        #widgets para conseguir datos de usuario
        x = 0.01
        y = 0.6
        userName   = self.master.MakeInputBox("Nombre\nCompleto ", x, y)
        id         = self.master.MakeInputBox("Cédula", x, y+0.1)
        country    = self.master.MakeInputBox("Gentilicio", x, y+0.2)
        phone      = self.master.MakeInputBox("Teléfono", x, y+0.3)
        jubilado   = self.master.MakeCheckBox("¿Jubilado?", 0.3, y)
        companions = self.master.MakeSpinBox("N° de \nacompañantes ", 0, 10, 0.3, y+0.1)
        sex        = self.master.MakeRadioButtom("Sexo","Masculino","Femenino", 0.3, y+0.2)
        dataArray  = [userName, id, sex, country, phone, companions, jubilado]

        # boton de captura de dato(ABONO) y cambio a siguiente frame
        tk.Button(self, text="ABONAR", command=lambda: self.CaptureUserData(dataArray, 1)).place(relx=0.70, rely=0.80)
        # boton de captura de dato(RESERVAR) y cambio a siguiente frame
        tk.Button(self, text="PAGAR", command=lambda: self.CaptureUserData(dataArray, 2)).place(relx=0.80, rely=0.80)

        # boton de regreso a Menu Principal
        backButtom = tk.Button(self, text="< Regresar a Menu de Zonas", command=lambda: self.master.switch_frame(ZonaMenu))
        backButtom.place(relx=0.0, rely=0.0)

    def CaptureUserData(self, userData, formaPago):
        #obj que almacena todos los datos del usuario
        self.master.USER = User(userData[0].get(), userData[1].get(), userData[2].get(), userData[3].get(), userData[4].get(), userData[5].get(), userData[6].get())
        if formaPago == 1:
            self.master.switch_frame(FacturaAbonoFrame)
        else:
            self.master.switch_frame(FacturaPagoFrame)


class FacturaAbonoFrame(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)
        canvas = tk.Canvas(self, width=1000, height=700)
        canvas.pack()
        tk.Label(self, text="Factura Final", font=('Helvetica', '25', 'bold')).place(x=400, y=0)

        # obtiene el subtotal a partir del precio x cabeza
        SUBTOTAL = self.master.userZoneSelected.getPrice() * (self.master.USER.Companions() + 1) if (
                    self.master.USER.Companions() > 0) else self.master.userZoneSelected.getPrice()
        # calcula el total final de la factura factura final
        self.TOTALFINAL = self.CalcularPrecioFinal(SUBTOTAL)
        # Imprime la factura en pantalla
        self.master.MakeTextBox(
            "Empresa: Kalidoso Tours\n" +
            "Ubicacion:" + self.master.userOption.Name() + ", " + self.master.userZoneSelected.Name() +
            "\nDescripcion de Zona: " + self.master.userZoneSelected.getDescription() + "\n" +
            self.master.USER.GetData() +
            "\nSUBTOTAL: $" + str(SUBTOTAL) +
            "\nDescuento Jubilado(10%): $" + str(self.descuentoJubilado) + "\tDescuento x personas(15%): $" + str(
                self.decuentoCompanions) + "\tDescuento x precio(5%): $"
            + str(self.descuentoPrecio) +
            "\nTOTAL: $" + str(self.TOTALFINAL),
            0.05, 0.1, 0.9, 0.50)

        #casilla donde el usuario pone su abono inicial
        abono = self.master.MakeInputBox("Abono Inicial: ", 0.25, 0.75)
        tk.Button(self, text="Aceptar Abono", command=lambda: self.CaptureTransaction(abono)).place(relx=0.45, rely=0.85)

        #boton de regreso
        tk.Button(self, text="< Regresar", command=lambda: self.master.switch_frame(UserDataMenu) ).place(x=5, y=5)

    def CalcularPrecioFinal(self, subTotal):
        # variables para almacenar los futuros descuentos
        self.descuentoJubilado = 0.0
        self.decuentoCompanions = 0.0
        self.descuentoPrecio = 0.0
        # Verificamos y calculamos si se pueden aplicar descuentos
        if (self.master.USER.jubilado):
            self.descuentoJubilado = subTotal * DESCUENTO_JUBILADO

        if (self.master.USER.Companions() >= 3):
            self.decuentoCompanions = subTotal * DESCUENTO_PERSONAS

        if (self.master.userZoneSelected.getPrice() > 2000.0):
            self.descuentoPrecio = subTotal * DESCUENTO_COMPRA_SUPERIOR
        # retoramos el precio Final
        return subTotal - (self.descuentoJubilado + self.decuentoCompanions + self.descuentoPrecio)

    def CaptureTransaction(self, amount):
        # crea una ventana emergente con el mensaje fina; y muestra la cantidad adeudada
        top = tk.Toplevel(width=700, height=200, bg='gray', bd=1)
        x = 10
        # si el abono es mayor entonces, No tiene deuda
        if float(amount.get()) >= self.TOTALFINAL:
            listaDeCompradores.append(
                Comprador(self.master.USER.Name(), self.master.USER.Companions(), self.master.userZoneSelected.Name(),
                          "ABONO", 0))
            tk.Label(top, text="Usted a abonado " + str(amount.get()) + ", Su deuda ha sido cancelada, puede gozar de los beneficios!",
                     font=('Helvetica', '10', 'bold')).place(x=x, y=25)
        else:
            listaDeCompradores.append(
                Comprador(self.master.USER.Name(), self.master.USER.Companions(), self.master.userZoneSelected.Name(),
                            "ABONO", self.TOTALFINAL - float(amount.get())))
            tk.Label(top, text="Usted a abonado " + str(amount.get()) + ", Cancele su deuda para gozar de beneficios",
                     font=('Helvetica', '10', 'bold')).place(x=x, y=25)
        self.master.switch_frame(MainMenu)
        top.mainloop()


class FacturaPagoFrame(tk.Frame):
    def __init__(self, master):
        self.master = master#permite recuperar datos de otras clases
        tk.Frame.__init__(self, master)
        canvas = tk.Canvas(self, width=1000, height=700)
        canvas.pack()
        #titulo
        tk.Label(self, text="Factura Final", font=('Helvetica', '25', 'bold')).place(x=400, y=0)
        #obtiene el subtotal a partir del precio x cabeza
        SUBTOTAL = self.master.userZoneSelected.getPrice() * (self.master.USER.Companions() + 1) if (self.master.USER.Companions() > 0) else self.master.userZoneSelected.getPrice()
        #calcula el total final de la factura factura final
        self.TOTALFINAL = self.CalcularPrecioFinal(SUBTOTAL)
        #Imprime la factura en pantalla
        self.master.MakeTextBox(
            "Empresa: Kalidoso Tours\n" +
            "Ubicacion:" + self.master.userOption.Name() + ", " + self.master.userZoneSelected.Name() +
            "\nDescripcion de Zona: " + self.master.userZoneSelected.getDescription() + "\n" +
            self.master.USER.GetData() +
            "\nSUBTOTAL: $" + str(SUBTOTAL) +
            "\nDescuento Jubilado(10%): $" + str(self.descuentoJubilado) + "\tDescuento x personas(15%): $" + str(self.decuentoCompanions) + "\tDescuento x precio(5%): $"
            + str(self.descuentoPrecio) +
            "\nTOTAL: $" + str(self.TOTALFINAL),
            0.05, 0.1, 0.9, 0.70)
        # boton de regreso a Menu Principal
        tk.Label(self, text="Felicidades por su compra, Le Esperamos!!!", font=('Helvetica', '15', 'bold'), fg='green').place(relx=0.25, rely=0.80)
        tk.Button(self, text="Aceptar",
                               command=lambda: self.CaptureTransaction()).place(relx=0.45, rely=0.85)
        #boton de regreso
        tk.Button(self, text="< Regresar", command=lambda: self.master.switch_frame(UserDataMenu)).place(x=5, y=5)

    def CalcularPrecioFinal(self, subTotal):
        #variables para almacenar los futuros descuentos
        self.descuentoJubilado = 0.0
        self.decuentoCompanions = 0.0
        self.descuentoPrecio = 0.0
        #Verificamos y calculamos si se pueden aplicar descuentos
        if (self.master.USER.jubilado):
            self.descuentoJubilado = subTotal * DESCUENTO_JUBILADO

        if (self.master.USER.Companions() >= 3):
            self.decuentoCompanions = subTotal * DESCUENTO_PERSONAS

        if (self.master.userZoneSelected.getPrice() > 2000.0):
            self.descuentoPrecio = subTotal * DESCUENTO_COMPRA_SUPERIOR
        #retoramos el precio Final
        return subTotal - (self.descuentoJubilado + self.decuentoCompanions + self.descuentoPrecio)

    #al activarse capturamos al usuario y volvemos al menu
    def CaptureTransaction(self):
        listaDeCompradores.append(Comprador(self.master.USER.Name(), self.master.USER.Companions(), self.master.userZoneSelected.Name(), "PAGO", self.TOTALFINAL))
        self.master.switch_frame(MainMenu)


#main thread, aqui se ejecuta el programa
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()