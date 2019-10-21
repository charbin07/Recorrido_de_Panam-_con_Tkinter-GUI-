

class Place():
    def __init__(self, name, src, imgsrc):
        self.name = name
        self.description = self.getFileInfo(src)
        self.image = imgsrc
        #self.zones = zones

    def getFileInfo(self, src):
        try:
            with open(src) as f:
                # for line in f.readlines():
                text = f.read()
                print(f"Archivo Leido file:{src}")
        except FileNotFoundError:
            text = None
            print(f"archivo no encontrado file:{src}")
        return text

    def Name(self):
        return self.name

    def getImageLink(self):
        return self.image

    def getDescription(self):
        return self.description

#provincias
LosSantos = Place("Los Santos", "../res/provincias/LosSantos/LosSantos.txt", "../res/provincias/LosSantos/LosSantos-mapa.png")
Herrera = Place("Herrera", "../res/provincias/Herrera/Herrera.txt", "../res/provincias/Herrera/Herrera-mapa.png")
Darien = Place("Darien", "../res/provincias/Darien/Darien.txt", "../res/provincias/Darien/darien-Mapa.png")
Panama = Place("Panama", "../res/provincias/Panama/panama.txt", "../res/provincias/Panama/panama.png")
PanamaOeste = Place("Panama Oeste", "../res/provincias/PanamaOeste/panamaOeste.txt", "../res/provincias/PanamaOeste/panamaOeste-mapa.png")
Veraguas = Place("Veraguas", "../res/provincias/Veraguas/veraguas.txt", "../res/provincias/Veraguas/veraguas-mapa.png")

#comarcas
Embera = Place("Embera", "../res/comarcas/Embera/comarca-Embera.txt", "../res/comarcas/Embera/Embera.png")
Guna = Place("Guna Yala", "../res/comarcas/GunaYala/Guna_yala.txt", "../res/comarcas/GunaYala/comarca_Guna.png")
Ngobe = Place("Ngobe-Bugle", "../res/comarcas/Ngobe-Bugle/Ngobe-Bugle.txt", "../res/comarcas/Ngobe-Bugle/Ngobe-Bugle.png")







