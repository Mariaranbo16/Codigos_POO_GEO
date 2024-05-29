import math as mh
from Codigos_POO_GEO.Coords_Inv.Backend.angulos import Angulos
from elipsoides import Elipsoides

elipsoide = Elipsoides()
angulos = Angulos()

class Coords_XYZ:

    def __init__(self):
        
        self.lat = 0
        self.lon = 0
        self.h = 0
        self.N = 0
        self.e = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def calc_2D(self):
        
        if self.lat == 0:
            print("Ingrese la latitud")
            angulos.grados()
            self.lat = angulos.decimal
            print("Ingrese la longitud")
            angulos.grados()
            self.h = float(input("Ingrese la altura (h): "))
            self.lon = angulos.decimal
            elipsoide.elip()
            self.e = elipsoide.e
            elipsoide.lat = self.lat
            elipsoide.lon = self.lon
            elipsoide.calc_radios()
            self.N = elipsoide.N
        else:
            print("Ingrese la longitud")
            angulos.grados()
            self.h = float(input("Ingrese la altura (h): "))
            self.lon = angulos.decimal
            elipsoide.elip()
            self.e = elipsoide.e
            elipsoide.lat = self.lat
            elipsoide.lon = self.lon
            elipsoide.calc_radios()
            self.N = elipsoide.N

        cos_fi = mh.cos(mh.radians(self.lat))
        sin_fi = mh.sin(mh.radians(self.lat))
        
        self.x = (self.N+self.h)*cos_fi
        self.y = (self.N*(1-self.e)+self.h)*sin_fi

        #Imprime las coordenadas cartesianas
        print(f"X: {self.x}")
        print(f"Z: {self.y}")

    def calc_3D(self):

        if self.lat == 0 and self.h == 0:
            print("Ingrese la latitud")
            angulos.grados()
            self.lat = angulos.decimal
            print("Ingrese la longitud")
            angulos.grados()
            self.h = float(input("Ingrese la altura (h): "))
            self.lon = angulos.decimal
            elipsoide.elip()
            self.e = elipsoide.e
            elipsoide.lat = self.lat
            elipsoide.lon = self.lon
            elipsoide.calc_radios()
            self.N = elipsoide.N
        else:
            print("Ingrese la longitud")
            angulos.grados()
            self.h = float(input("Ingrese la altura (h): "))
            self.lon = angulos.decimal
            elipsoide.elip()
            self.e = elipsoide.e
            elipsoide.lat = self.lat
            elipsoide.lon = self.lon
            elipsoide.calc_radios()
            self.N = elipsoide.N

        cos_fi = mh.cos(mh.radians(self.lat))
        sin_fi = mh.sin(mh.radians(self.lat))
        cos_lon = mh.cos(mh.radians(self.lon))
        sin_lon = mh.sin(mh.radians(self.lon))
        
        self.x = (self.N+self.h)*cos_fi*cos_lon
        self.y = (self.N+self.h)*cos_fi*sin_lon
        k = self.N*(1-self.e)
        c = self.h
        self.z = (k+c)*sin_fi

        #Imprime las coordenadas cartesianas
        print(f"X: {self.x}")
        print(f"Y: {self.y}")
        print(f"Z: {self.z}")
