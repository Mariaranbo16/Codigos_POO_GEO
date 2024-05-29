class Angulos:

    def __init__(self):
        
        self.decimal = 0
        self.gra = 0
        self.min = 0
        self.seg = 0

    def grados(self):

        print("Ingrese en grados sexagesimales: ")
        self.gra = float(input("Grados: "))
        self.min = float(input("Minutos: "))
        self.seg = float(input("Segundos: "))

        if self.gra < 0:
            self.decimal = 360+(self.gra - (self.min / 60) - (self.seg / 3600))
        else:
            self.decimal = self.gra + (self.min / 60) + (self.seg / 3600)

    def sexagesimales (self):

        self.gra = int(self.decimal)
        minutos_decimales = (self.decimal - self.gra) * 60
        self.min = int(minutos_decimales)
        self.seg = round((minutos_decimales - self.min) * 60,4)
         # Verificación y ajuste de segundos
        if self.seg >= 60:
            self.min += 1
            self.seg -= 60

        # Verificación y ajuste de minutos
        if self.min >= 60:
            self.gra += 1
            self.min -= 60

        # Verificación y ajuste de grados
        if self.gra >= 360:
            self.gra -= 360

        
