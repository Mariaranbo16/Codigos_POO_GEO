import math as mh
from Codigos_POO_GEO.Coords_Inv.Backend.angulos import Angulos
from elipsoides import Elipsoides

ang = Angulos()
elip = Elipsoides()

class Latitudes:

    def __init__(self):

        self.detic = 0
        self.centric = 0
        self.reduc = 0
        self.e = 0


    def geocentrica(self):
        print("---------------- COORDENADA GEODÉSICA ------------------")
        ang.grados()
        self.detic = ang.decimal
        ang.sexagesimales()
        print(f"La coordenada geodésica es: {ang.gra}° {ang.min}' {ang.seg:.4f}\'' ")
        print("----------------- ELIPSOIDE DE REFERENCIA ---------------")
        elip.elip()
        self.e = elip.e
        print("----------------- COORDENADA GEOCÉNTRICA ---------------")
        self.centric = mh.degrees(mh.atan((1-self.e)*(mh.tan(mh.radians(self.detic)))))
        ang.decimal = self.centric
        ang.sexagesimales()
        print(f"La coordenada geocéntrica es: {ang.gra}° {ang.min}' {ang.seg:.4f}\'' ")
        k = elip.a*mh.sqrt(1-self.e)
        t = mh.sqrt(1-(self.e*(mh.cos(mh.radians(self.centric)))**2))
        rg = k/t
        print(f"X: {rg * mh.cos(mh.radians(self.centric))}")
        print(f"Z: {rg * mh.sin(mh.radians(self.centric))}")

    def reducida(self):
        
        print("-----------------COORDENADA GEODÉSICA-------------------")
        ang.grados()
        self.detic = ang.decimal
        ang.sexagesimales()
        print(f"La coordenada geodésica es: {ang.gra}° {ang.min}' {ang.seg:.4f}\'' ")
        print("----------------- ELIPSOIDE DE REFERENCIA ---------------")
        elip.elip()
        self.e = elip.e
        print("----------------- COORDENADA REDUCIDA ---------------")
        self.reduc = mh.degrees(mh.atan((mh.sqrt(1-self.e))*(mh.tan(mh.radians(self.detic)))))
        ang.decimal = self.reduc
        ang.sexagesimales()
        print(f"La coordenada reducida es: {ang.gra}° {ang.min}' {ang.seg:.4f}\'' ")
        print(f"X: {elip.a * mh.cos(mh.radians(self.reduc))}")
        print(f"Z: {elip.b * mh.sin(mh.radians(self.reduc))}")