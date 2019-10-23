

class Place():
    def __init__(self, name, src, imgsrc):
        self.name = name
        self.description = self.getFileInfo(src)
        self.image = imgsrc
        self.zones = []

    def getFileInfo(self, src):
        try:
            with open(src) as f:
                # for line in f.readlines():
                text = f.read()
                #print(f"Archivo Leido file:{src}")
        except FileNotFoundError:
            text = None
            print(f"archivo no encontrado file:{src}")
        return text

    def AddZone(self, place):
        self.zones.append(place)

    def Name(self):
        return self.name

    def getImageLink(self):
        return self.image

    def getDescription(self):
        return self.description

    def getZone(self, index):
        return self.zones[index]


#provincias
LosSantos = Place("Los Santos", "../res/provincias/LosSantos/LosSantos.txt", "../res/provincias/LosSantos/LosSantos-mapa.png")
Herrera = Place("Herrera", "../res/provincias/Herrera/Herrera.txt", "../res/provincias/Herrera/Herrera-mapa.png")
Darien = Place("Darien", "../res/provincias/Darien/Darien.txt", "../res/provincias/Darien/darien-Mapa.png")
Panama = Place("Panama", "../res/provincias/Panama/panama.txt", "../res/provincias/Panama/panama.png")
PanamaOeste = Place("Panama Oeste", "../res/provincias/PanamaOeste/panamaOeste.txt", "../res/provincias/PanamaOeste/panamaOeste-mapa.png")
Veraguas = Place("Veraguas", "../res/provincias/Veraguas/veraguas.txt", "../res/provincias/Veraguas/veraguas-mapa.png")
Colon = Place("Colon", "../res/provincias/Colon/Colon.txt","/home/charbin07/PycharmProjects/Python/Prueba de tkinter/res/provincias/Colon/Mapa_de_Colon.png")
Cocle = Place("Cocle", "../res/provincias/Cocle/cocle.txt","/home/charbin07/PycharmProjects/Python/Prueba de tkinter/res/provincias/Cocle/Mapa_de_Cocle.png")
Chiriqui = Place("Chiriqui", "../res/provincias/Chiriqui/Chiriqui.txt","/home/charbin07/PycharmProjects/Python/Prueba de tkinter/res/provincias/Chiriqui/Mapa_de_Chiriqui.png")
Bocas = Place("Bocas del Toro", "../res/provincias/BocasDelToro/Bocas_del_toro.txt","/home/charbin07/PycharmProjects/Python/Prueba de tkinter/res/provincias/BocasDelToro/Bocas_del_Toro.png")

#comarcas
Embera = Place("Embera", "../res/comarcas/Embera/comarca-Embera.txt", "../res/comarcas/Embera/Embera.png")
Guna = Place("Guna Yala", "../res/comarcas/GunaYala/Guna_yala.txt", "../res/comarcas/GunaYala/comarca_Guna.png")
Ngobe = Place("Ngobe-Bugle", "../res/comarcas/Ngobe-Bugle/Ngobe-Bugle.txt", "../res/comarcas/Ngobe-Bugle/Ngobe-Bugle.png")

#zonas de Embera
Embera.AddZone(Place("Garachine", "../res/comarcas/Embera/zonas/desc/garachiné.txt", "../res/comarcas/Embera/zonas/img/Garachiné.png"))
Embera.AddZone(Place("La Palma", "../res/comarcas/Embera/zonas/desc/La_Palma.txt", "../res/comarcas/Embera/zonas/img/La_Palma_Darien.png"))
Embera.AddZone(Place("Puerto Indio", "../res/comarcas/Embera/zonas/desc/Puerto_Indio.txt", "../res/comarcas/Embera/zonas/img/Puerto_Indio.png"))
Embera.AddZone(Place("Sambu", "../res/comarcas/Embera/zonas/desc/Sambú.txt", "../res/comarcas/Embera/zonas/img/Sambú.png"))
#zonas de Guna Yala
Guna.AddZone(Place("Isla Chichime", "../res/comarcas/GunaYala/zonas/desc/Isla_Chicheme.txt", "../res/comarcas/GunaYala/zonas/img/Isla_chichime.png"))
Guna.AddZone(Place("Isla Pelicano", "../res/comarcas/GunaYala/zonas/desc/Isla_Pelicano.txt", "../res/comarcas/GunaYala/zonas/img/Isla_pelicano.png"))
Guna.AddZone(Place("Isla Perro Chico", "../res/comarcas/GunaYala/zonas/desc/Isla_Perro_Chico.txt", "../res/comarcas/GunaYala/zonas/img/Isla_Perro_Chico.png"))
Guna.AddZone(Place("San Blas", "../res/comarcas/GunaYala/zonas/desc/San_blas.txt", "../res/comarcas/GunaYala/zonas/img/SanBlas.png"))
#zonas de Ngobe
Ngobe.AddZone(Place("salto La Tulivieja", "../res/comarcas/Ngobe-Bugle/zonas/desc/cascada_Latulivieja.txt", "../res/comarcas/Ngobe-Bugle/zonas/img/Salto_La_tulivieja.png"))
Ngobe.AddZone(Place("Kusapin", "../res/comarcas/Ngobe-Bugle/zonas/desc/kusapin.txt", "../res/comarcas/Ngobe-Bugle/zonas/img/Kusapin.png"))
Ngobe.AddZone(Place("Salto Kiki", "../res/comarcas/Ngobe-Bugle/zonas/desc/salto_kiki.txt", "../res/comarcas/Ngobe-Bugle/zonas/img/Salto_kiki.png"))
Ngobe.AddZone(Place("salto Romelio", "../res/comarcas/Ngobe-Bugle/zonas/desc/salto_Romelio.txt", "../res/comarcas/Ngobe-Bugle/zonas/img/Salto_romelio.png"))

#zonas de Panama
Panama.AddZone(Place("Coswey Amador", "../res/provincias/Panama/zonas/decr/amador.txt", "../res/provincias/Panama/zonas/img/cosweyAmador.png"))
Panama.AddZone(Place("Canal de Panama", "../res/provincias/Panama/zonas/decr/canaldepanama.txt", "../res/provincias/Panama/zonas/img/canaldepanama.png"))
Panama.AddZone(Place("PanamaLaVieja", "../res/provincias/Panama/zonas/decr/panamaLavieja.txt", "../res/provincias/Panama/zonas/img/panamaLavieja.png"))
Panama.AddZone(Place("Parque Omar", "../res/provincias/Panama/zonas/decr/parqueOmar.txt", "../res/provincias/Panama/zonas/img/parqueOmar.png"))
#zonas de PanamaOeste
PanamaOeste.AddZone(Place("Chica", "../res/provincias/PanamaOeste/zonas/descr/chica.txt", "../res/provincias/PanamaOeste/zonas/img/chica.png"))
PanamaOeste.AddZone(Place("LagunaSanCarlos", "../res/provincias/PanamaOeste/zonas/descr/lagunaSanCarlos.txt", "../res/provincias/PanamaOeste/zonas/img/lagunaSanCarlos.png"))
PanamaOeste.AddZone(Place("Punta Chame", "../res/provincias/PanamaOeste/zonas/descr/puntachame.txt", "../res/provincias/PanamaOeste/zonas/img/puntaChame.png"))
PanamaOeste.AddZone(Place("WestLand", "../res/provincias/PanamaOeste/zonas/descr/westland.txt", "../res/provincias/PanamaOeste/zonas/img/westland.png"))
#zonas de Veraguas
Veraguas.AddZone(Place("Golfo de Montijo", "../res/provincias/Veraguas/zonas/descr/golfoDeMontijo.txt", "../res/provincias/Veraguas/zonas/img/GolfodeMontijo.png"))
Veraguas.AddZone(Place("parque Cerro Hoya", "../res/provincias/Veraguas/zonas/descr/parqueNacionalCerroHoya.txt", "../res/provincias/Veraguas/zonas/img/parqueCerroHoya.png"))
Veraguas.AddZone(Place("Isla Coiba", "../res/provincias/Veraguas/zonas/descr/parqueNacionalCoiba.txt", "../res/provincias/Veraguas/zonas/img/islaCoiba.png"))
Veraguas.AddZone(Place("reserva LaYeguada", "../res/provincias/Veraguas/zonas/descr/reservaLaYeguada.txt", "../res/provincias/Veraguas/zonas/img/reservaLaYeguada.png"))
#zonas de Darien
Darien.AddZone(Place("Bahia Pina", "../res/provincias/Darien/zonas/descr/bahiaPiña.txt", "../res/provincias/Darien/zonas/img/bahiaPiña.png"))
Darien.AddZone(Place("Mogue", "../res/provincias/Darien/zonas/descr/mogue.txt", "../res/provincias/Darien/zonas/img/mogue.png"))
Darien.AddZone(Place("Parque Nacional Darien", "../res/provincias/Darien/zonas/descr/parqueNacionalDarien.txt", "../res/provincias/Darien/zonas/img/parqueNacionalDarien.png"))
Darien.AddZone(Place("Yaviza", "../res/provincias/Darien/zonas/descr/yaviza.txt", "../res/provincias/Darien/zonas/img/yaviza.png"))
#zonas de Herrera
Herrera.AddZone(Place("Arenal de Herrera", "../res/provincias/Herrera/zonas/descr/arenaDeHerrera.txt", "../res/provincias/Herrera/zonas/img/ArenaDeHerrera.png"))
Herrera.AddZone(Place("El Cenegon", "../res/provincias/Herrera/zonas/descr/elCenegon.txt", "../res/provincias/Herrera/zonas/img/elCenegon.png"))
Herrera.AddZone(Place("parque Nacional Sarigua", "../res/provincias/Herrera/zonas/descr/parqueSarigua.txt", "../res/provincias/Herrera/zonas/img/parqueSarigua.png"))
Herrera.AddZone(Place("Sarigua la Mula", "../res/provincias/Herrera/zonas/descr/sariguaLaMula.txt", "../res/provincias/Herrera/zonas/img/sariguaLaMula.png"))
#zonas de Los Santos
LosSantos.AddZone(Place("isla de Iguana", "../res/provincias/LosSantos/zonas/descr/islaIguana.txt", "../res/provincias/LosSantos/zonas/img/islaIguana.png"))
LosSantos.AddZone(Place("parque Cerro Hoya", "../res/provincias/LosSantos/zonas/descr/parqueCerroHoya.txt", "../res/provincias/LosSantos/zonas/img/parqueCerroHoya.png"))
LosSantos.AddZone(Place("playa El Arenal", "../res/provincias/LosSantos/zonas/descr/playaArenal.txt", "../res/provincias/LosSantos/zonas/img/playaArenal.png"))
LosSantos.AddZone(Place("playa Venao", "../res/provincias/LosSantos/zonas/descr/playaVenao.txt", "../res/provincias/LosSantos/zonas/img/playaVenao.png"))
