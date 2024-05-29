from elipsoides import Elipsoides
from Codigos_POO_GEO.Coords_Inv.Backend.angulos import Angulos

import math as mh

elip = Elipsoides()
ang = Angulos()

class Inverso1:

    def __init__(self):
        
        self.x = 0
        self.y = 0
        self.z = 0
        self.e = 0
        self.a = 0
        self.N = 0
        self.lat = 0
        self.lon = 0
        self.h = 0

    def coords (self):

        # Escribe las coordenadas

        print(f"Ingrese las coordenadas x,y,z")
        self.x = float(input("X: "))
        self.y = float(input("Y: "))
        self.z = float(input("Z: "))
        while self.x == 0 and self.y == 0 and self.z == 0:
            print("Error, vuelva a intentarlo, esta dentro del elipsoide de referencia.")
            self.coords()

    def longitud (self):
        
        # Halla la longitud

        self.lon = mh.degrees(mh.atan(self.y/self.x))
        if self.lon > 0 and self.lon < 360:
            self.lon = self.lon
        elif self.lon < 0 and self.lon > -360:
            self.lon += 360

    def latitud (self):

        cant = int(input("Ingrese la cantidad de veces para hacer el calculo: "))
        # Con h = 0
        x = self.z / mh.sqrt(self.x**2 + self.y**2)
        y = 1 + (self.e / 1 - self.e)
        for i in range(0,cant):
            if i == 0:
                self.lat = mh.degrees(mh.atan(x*y))
                elip.elip()
                self.e = elip.e
                self.a = elip.a
                elip.lat = self.lat
                elip.lon = self.lon
                elip.calc_radios()
                self.N = elip.N
            else:
                k = self.e * self.N * mh.sin(mh.radians(self.lat)) / mh.sqrt(self.x**2 + self.y**2)
                self.lat = mh.degrees(mh.atan(x + k))
                elip.lat = self.lat
                elip.calc_radios()
                self.N = elip.N
                self.h = (mh.sqrt(self.x**2 + self.y**2) / mh.cos(mh.radians(self.lat))) - self.N

    def geograficas (self):

        self.coords()
        self.longitud()
        self.latitud()
        ang.decimal = self.lat
        ang.sexagesimales()
        print(f"La latitud es: {ang.gra}º {ang.min}' {ang.seg:.4f}\'' ")
        ang.decimal = self.lon
        ang.sexagesimales()
        print(f"La longitud es: {ang.gra}º {ang.min}' {ang.seg:.4f}\'' ")
        print(f"La altura es: {self.h}")