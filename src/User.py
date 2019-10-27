class User():
    def __init__(self, name, id, sex, country, phone, n, jubilado):
        self.name = name
        self.id = id
        self.sex = sex
        self.country = country
        self.phone = phone
        self.companions = n
        self.jubilado = jubilado

    def Name(self):
        return self.name

    def Companions(self):
        return self.companions

    def Jubilado(self):
        return self.jubilado

    def GetData(self):
        dataString = "DATOS DE USUARIO:\nNombre: " + self.name +"\nid: " + str(self.id) + "\nsexo:" + self.sex +"\npais: " + self.country + "\nphone:" + self.phone +"\nacompanantes: " +str(self.companions)
        dataString += "\nJubilado: SI" if (self.jubilado==True) else "\nJubilado: NO"
        return dataString
