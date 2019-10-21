

class Place():

    def __init__(self, name, src, imgsrc):
        self.name = name
        self.description = self.getFileInfo(src)
        self.image = imgsrc
        #self.zones = zones

    def getFileInfo(self, src):
        try:
            with open(src) as f:
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


LosSantos = Place("Los Santos", "../res/LosSantos.txt", "../res/LosSantos-mapa.png")
Herrera = Place("Herrera", "../res/Herrera.txt", "../res/Herrera-mapa.png")
Darien = Place("Darien", "../res/Darien.txt", "../res/darien-Mapa.png")

