from elipsoides import Elipsoides
from Codigos_POO_GEO.Coords_Inv.Backend.angulos import Angulos

import math as mh

elip = Elipsoides()
ang = Angulos()

class Inverso3:

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

    def cords (self):

        # Escribe las coordenadas

        print(f"Ingrese las coordenadas x,y,z")
        self.x = float(input("X: "))
        self.y = float(input("Y: "))
        self.z = float(input("Z: "))
        while self.x == 0 and self.y == 0 and self.z == 0:
            print("Error, vuelva a intentarlo, esta dentro del elipsoide de referencia.")
            self.cords()

    def longitud (self):
        
        # Halla la longitud

        self.lon = mh.degrees(mh.atan(self.y/self.x))
        if self.lon > 0 and self.lon < 360:
            self.lon = self.lon
        elif self.lon < 0 and self.lon > -360:
            self.lon += 360

    def latitud (self):

        cant = int(input("Ingrese la cantidad de veces para hacer el calculo: "))
        print("---------------- ELIPSE DE REFERENCIA -------------------")
        elip.elip()
        for i in range(0,cant):
            if i == 0:
                self.h = mh.sqrt(self.x**2 + self.y**2 + self.z**2) - mh.sqrt(elip.a*elip.b)
                self.N = elip.a
                f = self.z/mh.sqrt(self.x**2 + self.y**2)
                n = 1 + (elip.e*self.N/(self.N + self.h)) 
                self.lat = mh.degrees(mh.atan(f*n))
            else:
                self.N = elip.a/mh.sqrt(1 - elip.e*(mh.sin(self.lat))*2)
                self.h = (mh.sqrt(self.x**2 + self.y**2) / mh.cos(mh.radians(self.lat))) - self.N
                self.lat = mh.degrees(mh.atan(f*n))
                elip.lat = self.lat
                elip.calc_radios()
                self.N = elip.N

    def geograficas (self):

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