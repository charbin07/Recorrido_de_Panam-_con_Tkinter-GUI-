

class Place():
    def __init__(self, name, src, imgsrc, price=0.0):
        self.name = name
        self.description = self.getFileInfo(src)
        self.image = imgsrc
        self.zones = []
        self.pricePerPerson = price

    def getFileInfo(self, src):
        try:
            with open(src, encoding="utf-8") as f:
                # for line in f.readlines():
                text = f.read()
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

    def getPrice(self):
        return self.pricePerPerson


#provincias
LosSantos = Place("Los Santos", "../res/provincias/LosSantos/LosSantos.txt", "../res/provincias/LosSantos/LosSantos-mapa.png")
Herrera = Place("Herrera", "../res/provincias/Herrera/Herrera.txt", "../res/provincias/Herrera/Herrera-mapa.png")
Darien = Place("Darien", "../res/provincias/Darien/Darien.txt", "../res/provincias/Darien/darien-Mapa.png")
Panama = Place("Panama", "../res/provincias/Panama/panama.txt", "../res/provincias/Panama/panama.png")
PanamaOeste = Place("Panama Oeste", "../res/provincias/PanamaOeste/panamaOeste.txt", "../res/provincias/PanamaOeste/panamaOeste-mapa.png")
Veraguas = Place("Veraguas", "../res/provincias/Veraguas/veraguas.txt", "../res/provincias/Veraguas/veraguas-mapa.png")
Colon = Place("Colon", "../res/provincias/Colon/Colon.txt","../res/provincias/Colon/Mapa_de_Colon.png")
Cocle = Place("Cocle", "../res/provincias/Cocle/cocle.txt","../res/provincias/Cocle/Mapa_de_Cocle.png")
Chiriqui = Place("Chiriqui", "../res/provincias/Chiriqui/Chiriqui.txt","../res/provincias/Chiriqui/Mapa_de_Chiriqui.png")
Bocas = Place("Bocas del Toro", "../res/provincias/BocasDelToro/Bocas_del_toro.txt","../res/provincias/BocasDelToro/Bocas_del_Toro.png")

#comarcas
Embera = Place("Embera", "../res/comarcas/Embera/comarca-Embera.txt", "../res/comarcas/Embera/Embera.png")
Guna = Place("Guna Yala", "../res/comarcas/GunaYala/Guna_yala.txt", "../res/comarcas/GunaYala/comarca_Guna.png")
Ngobe = Place("Ngobe-Bugle", "../res/comarcas/Ngobe-Bugle/Ngobe-Bugle.txt", "../res/comarcas/Ngobe-Bugle/Ngobe-Bugle.png")

#zonas de Embera
Embera.AddZone(Place("Garachine", "../res/comarcas/Embera/zonas/desc/garachiné.txt", "../res/comarcas/Embera/zonas/img/Garachiné.png", 2500.0))
Embera.AddZone(Place("La Palma", "../res/comarcas/Embera/zonas/desc/La_Palma.txt", "../res/comarcas/Embera/zonas/img/La_Palma_Darien.png", 1000.0))
Embera.AddZone(Place("Puerto Indio", "../res/comarcas/Embera/zonas/desc/Puerto_Indio.txt", "../res/comarcas/Embera/zonas/img/Puerto_Indio.png", 1500.0))
Embera.AddZone(Place("Sambu", "../res/comarcas/Embera/zonas/desc/Sambú.txt", "../res/comarcas/Embera/zonas/img/Sambú.png", 500.0))
#zonas de Guna Yala
Guna.AddZone(Place("Isla Chichime", "../res/comarcas/GunaYala/zonas/desc/Isla_Chicheme.txt", "../res/comarcas/GunaYala/zonas/img/Isla_chichime.png", 1200.0))
Guna.AddZone(Place("Isla Pelicano", "../res/comarcas/GunaYala/zonas/desc/Isla_Pelicano.txt", "../res/comarcas/GunaYala/zonas/img/Isla_pelicano.png", 500.0))
Guna.AddZone(Place("Isla Perro Chico", "../res/comarcas/GunaYala/zonas/desc/Isla_Perro_Chico.txt", "../res/comarcas/GunaYala/zonas/img/Isla_Perro_Chico.png", 1200.0))
Guna.AddZone(Place("San Blas", "../res/comarcas/GunaYala/zonas/desc/San_blas.txt", "../res/comarcas/GunaYala/zonas/img/SanBlas.png", 1300.0))
#zonas de Ngobe
Ngobe.AddZone(Place("salto La Tulivieja", "../res/comarcas/Ngobe-Bugle/zonas/desc/cascada_Latulivieja.txt", "../res/comarcas/Ngobe-Bugle/zonas/img/Salto_La_tulivieja.png", 500.0))
Ngobe.AddZone(Place("Kusapin", "../res/comarcas/Ngobe-Bugle/zonas/desc/kusapin.txt", "../res/comarcas/Ngobe-Bugle/zonas/img/Kusapin.png", 100.0))
Ngobe.AddZone(Place("Salto Kiki", "../res/comarcas/Ngobe-Bugle/zonas/desc/salto_kiki.txt", "../res/comarcas/Ngobe-Bugle/zonas/img/Salto_kiki.png", 200.0))
Ngobe.AddZone(Place("salto Romelio", "../res/comarcas/Ngobe-Bugle/zonas/desc/salto_Romelio.txt", "../res/comarcas/Ngobe-Bugle/zonas/img/Salto_romelio.png", 250.0))
#zonas de Panama
Panama.AddZone(Place("Coswey Amador", "../res/provincias/Panama/zonas/decr/amador.txt", "../res/provincias/Panama/zonas/img/cosweyAmador.png", 1450.0))
Panama.AddZone(Place("Canal de Panama", "../res/provincias/Panama/zonas/decr/canaldepanama.txt", "../res/provincias/Panama/zonas/img/canaldepanama.png", 1200.0))
Panama.AddZone(Place("PanamaLaVieja", "../res/provincias/Panama/zonas/decr/panamaLavieja.txt", "../res/provincias/Panama/zonas/img/panamaLavieja.png", 1400.0))
Panama.AddZone(Place("Parque Omar", "../res/provincias/Panama/zonas/decr/parqueOmar.txt", "../res/provincias/Panama/zonas/img/parqueOmar.png", 2000.0))
#zonas de PanamaOeste
PanamaOeste.AddZone(Place("Chica", "../res/provincias/PanamaOeste/zonas/descr/chica.txt", "../res/provincias/PanamaOeste/zonas/img/chica.png", 650.0))
PanamaOeste.AddZone(Place("LagunaSanCarlos", "../res/provincias/PanamaOeste/zonas/descr/lagunaSanCarlos.txt", "../res/provincias/PanamaOeste/zonas/img/lagunaSanCarlos.png", 1200.0))
PanamaOeste.AddZone(Place("Punta Chame", "../res/provincias/PanamaOeste/zonas/descr/puntachame.txt", "../res/provincias/PanamaOeste/zonas/img/puntaChame.png", 1500.0))
PanamaOeste.AddZone(Place("WestLand", "../res/provincias/PanamaOeste/zonas/descr/westland.txt", "../res/provincias/PanamaOeste/zonas/img/westland.png", 750.0))
#zonas de Veraguas
Veraguas.AddZone(Place("Golfo de Montijo", "../res/provincias/Veraguas/zonas/descr/golfoDeMontijo.txt", "../res/provincias/Veraguas/zonas/img/GolfodeMontijo.png", 600.0))
Veraguas.AddZone(Place("parque Cerro Hoya", "../res/provincias/Veraguas/zonas/descr/parqueNacionalCerroHoya.txt", "../res/provincias/Veraguas/zonas/img/parqueCerroHoya.png", 1200.0))
Veraguas.AddZone(Place("Isla Coiba", "../res/provincias/Veraguas/zonas/descr/parqueNacionalCoiba.txt", "../res/provincias/Veraguas/zonas/img/islaCoiba.png", 2500.0))
Veraguas.AddZone(Place("reserva LaYeguada", "../res/provincias/Veraguas/zonas/descr/reservaLaYeguada.txt", "../res/provincias/Veraguas/zonas/img/reservaLaYeguada.png", 2100.0))
#zonas de Darien
Darien.AddZone(Place("Bahia Pina", "../res/provincias/Darien/zonas/descr/bahiaPiña.txt", "../res/provincias/Darien/zonas/img/bahiaPiña.png", 900.0))
Darien.AddZone(Place("Mogue", "../res/provincias/Darien/zonas/descr/mogue.txt", "../res/provincias/Darien/zonas/img/mogue.png", 500.0))
Darien.AddZone(Place("Parque Nacional Darien", "../res/provincias/Darien/zonas/descr/parqueNacionalDarien.txt", "../res/provincias/Darien/zonas/img/parqueNacionalDarien.png", 400.0))
Darien.AddZone(Place("Yaviza", "../res/provincias/Darien/zonas/descr/yaviza.txt", "../res/provincias/Darien/zonas/img/yaviza.png", 750.0))
#zonas de Herrera
Herrera.AddZone(Place("Arenal de Herrera", "../res/provincias/Herrera/zonas/descr/arenaDeHerrera.txt", "../res/provincias/Herrera/zonas/img/ArenaDeHerrera.png", 1000.0))
Herrera.AddZone(Place("El Cenegon", "../res/provincias/Herrera/zonas/descr/elCenegon.txt", "../res/provincias/Herrera/zonas/img/elCenegon.png", 600.0))
Herrera.AddZone(Place("parque Nacional Sarigua", "../res/provincias/Herrera/zonas/descr/parqueSarigua.txt", "../res/provincias/Herrera/zonas/img/parqueSarigua.png", 1200.0))
Herrera.AddZone(Place("Sarigua la Mula", "../res/provincias/Herrera/zonas/descr/sariguaLaMula.txt", "../res/provincias/Herrera/zonas/img/sariguaLaMula.png", 300.0))
#zonas de Los Santos
LosSantos.AddZone(Place("isla de Iguana", "../res/provincias/LosSantos/zonas/descr/islaIguana.txt", "../res/provincias/LosSantos/zonas/img/islaIguana.png", 500.0))
LosSantos.AddZone(Place("parque Cerro Hoya", "../res/provincias/LosSantos/zonas/descr/parqueCerroHoya.txt", "../res/provincias/LosSantos/zonas/img/parqueCerroHoya.png", 1200.0))
LosSantos.AddZone(Place("playa El Arenal", "../res/provincias/LosSantos/zonas/descr/playaArenal.txt", "../res/provincias/LosSantos/zonas/img/playaArenal.png", 750.0))
LosSantos.AddZone(Place("playa Venao", "../res/provincias/LosSantos/zonas/descr/playaVenao.txt", "../res/provincias/LosSantos/zonas/img/playaVenao.png", 900.0))
#zonas de Bocas
Bocas.AddZone(Place("Isla Bastimento","../res/provincias/BocasDelToro/zonas/descr/Bastimento.txt", "../res/provincias/BocasDelToro/zonas/imagenes/isla_bastimento.png", 2000.0))
Bocas.AddZone(Place("Isla colon", "../res/provincias/BocasDelToro/zonas/descr/isla_colon.txt", "../res/provincias/BocasDelToro/zonas/imagenes/isla_colon_bocas.png", 3000.0))
Bocas.AddZone(Place("Playa estrella", "../res/provincias/BocasDelToro/zonas/descr/playa_estrella.txt","../res/provincias/BocasDelToro/zonas/imagenes/Playa-Estrellas-4.png", 2500.0))
Bocas.AddZone(Place("Isla solarte", "../res/provincias/BocasDelToro/zonas/descr/isla_solarte.txt", "../res/provincias/BocasDelToro/zonas/imagenes/Isla-Solarte.png", 1500.0))
# #zonas de chiriqui
Chiriqui.AddZone(Place("Boquete", "../res/provincias/Chiriqui/zonas/descr/Bajo_Boquete.txt", "../res/provincias/Chiriqui/zonas/img/boquete.png", 2300.0))
Chiriqui.AddZone(Place("Cerro punta", "../res/provincias/Chiriqui/zonas/descr/Cerro_Punta.txt", "../res/provincias/Chiriqui/zonas/img/Cerro_Punta.png", 2000.0))
Chiriqui.AddZone(Place("David", "../res/provincias/Chiriqui/zonas/descr/David.txt", "../res/provincias/Chiriqui/zonas/img/David.png", 1000.0))
Chiriqui.AddZone(Place("Las lajas", "../res/provincias/Chiriqui/zonas/descr/Las_Lajas.txt","../res/provincias/Chiriqui/zonas/img/Las_Lajas.png", 2500.0))
# #zonas de cocle
Cocle.AddZone(Place("La india dormida", "../res/provincias/Cocle/zonas/descr/india_dormida.txt","../res/provincias/Cocle/zonas/img/La_india_dormida.png", 400.0))
Cocle.AddZone(Place("Museo del caño", "../res/provincias/Cocle/zonas/descr/museo_del_caño.txt","../res/provincias/Cocle/zonas/img/El-Caño.png", 500.0))
Cocle.AddZone(Place("Playa Farallon", "../res/provincias/Cocle/zonas/descr/playa_farallon.txt","../res/provincias/Cocle/zonas/img/Playa_farallon.png", 750.0))
Cocle.AddZone(Place("Valle de Anton", "../res/provincias/Cocle/zonas/descr/valle_de_anton.txt","../res/provincias/Cocle/zonas/img/valle_de_anton.png", 1400.0))
#zonas de colon
Colon.AddZone(Place("Fuerte San Lorenzo", "../res/provincias/Colon/zonas/descr/Fuerte_San_Lorenzo.txt","../res/provincias/Colon/zonas/img/Fuerte_san_lorenzo .png",2000.0 ))
Colon.AddZone(Place("Gamboa", "../res/provincias/Colon/zonas/descr/Gamboa.txt","../res/provincias/Colon/zonas/img/Gamboa.png", 1400.0))
Colon.AddZone(Place("Lago Gatun", "../res/provincias/Colon/zonas/descr/lago_gatun.txt","../res/provincias/Colon/zonas/img/Lago_gatun.png", 1200.0))
Colon.AddZone(Place("Portobelo", "../res/provincias/Colon/zonas/descr/portobelo.txt","../res/provincias/Colon/zonas/img/Portobelo.png", 600.0))
