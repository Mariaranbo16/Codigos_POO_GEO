# A partir de dos coordenadas hallar la tercera: Bisección
import math
import matplotlib.pyplot as plt

# Definimos la clase
class BisectionProgram:
    # Inicialización del objeto por los atributos.
    def __init__(self):
        print("Programa Bisección - Cálculos de Np y Ep mediante el método no exacto")
        self.NA = float(input("Ingrese Norte de A: "))
        self.EA = float(input("Ingrese Este de A: "))
        self.NB = float(input("Ingrese Norte de B: "))
        self.EB = float(input("Ingrese Este de B: "))
        self.alphaG = float(input("Ingresa los Grados de la α: "))
        self.alphaM = float(input("Ingresa los Minutos de la α: "))
        self.alphaS = float(input("Ingresa los Segundos de la α: "))
        self.alphaD = float(self.alphaG + (self.alphaM / 60) + (self.alphaS / 3600))
        self.bethaG = float(input("Ingresa los Grados de la β: "))
        self.bethaM = float(input("Ingresa los Minutos de la β: "))
        self.bethaS = float(input("Ingresa los Segundos de la β: "))
        self.bethaD = float(self.bethaG + (self.bethaM / 60) + (self.bethaS / 3600))

    # Calculando la distancia de A a B
    def calculate_bisection(self):
        print("Programa Bisección - Cálculos de Np y Ep mediante el método no exacto")
        if self.NB == self.NA:
            AB = abs(self.EB - self.EA)
        elif self.EB == self.EA:
            AB = abs(self.NB - self.NA)
        else:
            AB = math.sqrt((self.NB - self.NA) ** 2 + (self.EB - self.EA) ** 2)
        alpbet = self.alphaD + self.bethaD
        # Cálculo de ángulos totales
        AP = (AB * math.sin(math.radians(self.bethaD))) / math.sin(math.radians(alpbet))
        if self.NB == self.NA:
            alphaAB = 0
        elif self.EB == self.EA:
            alpha2AB = 90
        else:
            alphaAB = math.atan(math.radians(self.EB - self.EA) / math.radians(self.NB - self.NA))
        alphaAB2 = math.degrees(alphaAB)

        if self.NB < self.NA and self.EB < self.EA:
            AzimutB = 180 + abs(alphaAB2)
        elif self.NB > self.NA and self.EB < self.EA:
            AzimutB = 360 - abs(alphaAB2)
        elif self.NB > self.NA and self.EB > self.EA:
            AzimutB = abs(alphaAB2)
        elif self.NB < self.NA and self.EB > self.EA:
            AzimutB = 180 - abs(alphaAB2)
        elif self.NB == self.NA and self.EA > self.EB:
            AzimutB = 270
        elif self.NB == self.NA and self.EA < self.EB:
            AzimutB = 90
        elif self.EB == self.EA and self.NA > self.NB:
            AzimutB = 180
        elif self.EB == self.EA and self.NB > self.NA:
            AzimutB = 0
        AzimuthP = AzimutB + self.alphaD

        if AzimuthP < 0:
            AzimuthP = 360 - abs(AzimuthP)
        if AzimuthP < 90:
            alphaAP = abs(AzimuthP)
            DeltaE = AP * math.sin((alphaAP * math.pi) / 180)
            DeltaN = AP * math.cos((alphaAP * math.pi) / 180)
            NorteP = self.NA + abs(DeltaN)
            EsteP = self.EA + abs(DeltaE)
            print("Np = ", NorteP)
            print("Ep = ", EsteP)
        if AzimuthP > 90 and AzimuthP < 180:
            alphaAP = 180 - abs(AzimuthP)
            DeltaE = AP * math.sin((alphaAP * math.pi) / 180)
            DeltaN = AP * math.cos((alphaAP * math.pi) / 180)
            NorteP = self.NA - abs(DeltaN)
            EsteP = self.EA + abs(DeltaE)
            print("Np = ", NorteP)
            print("Ep = ", EsteP)
        if AzimuthP > 180 and AzimuthP < 270:
            alphaAP = abs(AzimuthP) - 180
            DeltaE = AP * math.sin((alphaAP * math.pi) / 180)
            DeltaN = AP * math.cos((alphaAP * math.pi) / 180)
            NorteP = self.NA - abs(DeltaN)
            EsteP = self.EA - abs(DeltaE)
            print("Np = ", NorteP)
            print("Ep = ", EsteP)
        if AzimuthP > 270 and AzimuthP < 360:
            alphaAP = 360 - abs(AzimuthP)
            DeltaE = AP * math.sin((alphaAP * math.pi) / 180)
            DeltaN = AP * math.cos((alphaAP * math.pi) / 180)
            NorteP = self.NA + abs(DeltaN)
            EsteP = self.EA - abs(DeltaE)
            print("Np = ", NorteP)
            print("Ep = ", EsteP)

        # Gráfico de la bisección
        # Coordenadas Este
        Ejex = [self.EA, self.EB, EsteP, self.EA]
        # Coordenadas Norte 
        Ejey = [self.NA, self.NB, NorteP, self.NA]

        plt.annotate("A", xy=(self.EA, self.NA))
        plt.annotate("B", xy=(self.EB, self.NB))
        plt.annotate("P", xy=(EsteP, NorteP))
        plt.xlabel("Este")
        plt.ylabel("Norte")
        plt.plot(Ejex, Ejey, linestyle="--", color="green")
        plt.show()
