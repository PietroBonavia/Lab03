class Noleggio:
    def __init__(self, codice, data, auto, cliente):
        self.codice = codice
        self.data = data
        self.auto = auto
        self.cliente = cliente


    def __str__(self):
        return f'Noleggio {self.codice} - {self.data} {self.auto} {self.cliente}'