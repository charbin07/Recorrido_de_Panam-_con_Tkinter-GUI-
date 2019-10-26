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