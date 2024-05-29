from calc_inv1 import Inverso1
from elipsoides import Elipsoides
from Codigos_POO_GEO.Coords_Inv.Backend.angulos import Angulos
import math as mh

ang = Angulos()
elip = Elipsoides()
inv1 = Inverso1()

class Inverso2:

    def __init__(self):

        self.lat = 0
        self.lon = 0
        self.h = 0
        self.x = 0
        self.y = 0
        self.z = 0
    
    def cords(self):

        # Escribe las coordenadas

        print(f"Ingrese las coordenadas x,y,z")
        self.x = float(input("X: "))
        self.y = float(input("Y: "))
        self.z = float(input("Z: "))
        while self.x == 0 and self.y == 0 and self.z == 0:
            print("Error, vuelva a intentarlo, esta dentro del elipsoide de referencia.")
            self.cords()

    def longitud(self):

        # Halla la longitud

        self.lon = mh.degrees(mh.atan(self.y/self.x))
        if self.lon > 0 and self.lon < 360:
            self.lon = self.lon
        elif self.lon < 0 and self.lon > -360:
            self.lon += 360

    def latitud(self):

        print("-------- ELIPSOIDE DE REFERENCIA ---------")
        elip.elip()
        f = self.z*elip.a
        c = elip.b*mh.sqrt(self.x**2 + self.y**2)
        cosito = mh.atan(f/c)
        k = self.z + (elip.e2*elip.b*(mh.sin(cosito))**3)
        m = mh.sqrt(self.x**2 + self.y**2)
        z = elip.e*elip.a*(mh.cos(cosito))**3
        self.lat = mh.degrees(mh.atan(k/(m-z)))
        elip.lat = self.lat
        elip.calc_radios()
        self.h = (mh.sqrt(self.x**2 + self.y**2) / mh.cos(mh.radians(self.lat))) - elip.N

    def geograficas(self):

        self.cords()
        self.longitud()
        self.latitud()
        ang.decimal = self.lat
        ang.sexagesimales()
        print(f"La latitud es: {ang.gra}º {ang.min}' {ang.seg:.4f}\'' ")
        ang.decimal = self.lon
        ang.sexagesimales()
        print(f"La longitud es: {ang.gra}º {ang.min}' {ang.seg:.4f}\'' ")
        print(f"La altura es: {self.h}")
