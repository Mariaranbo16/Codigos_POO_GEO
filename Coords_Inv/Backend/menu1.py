from coords import Coords_XYZ
from Codigos_POO_GEO.Coords_Inv.Backend.Latitudes import Latitudes
from calc_inv1 import Inverso1
from calc_inv2 import Inverso2
from calc_inv3 import Inverso3
from Bajada import NivelacionDiferencialGeodesica
from Biseccion import BisectionProgram

class Menu:

    def interactuador(self):

        valor = int(input("""----- CODIGOS DE GEODESIA ------- 
1) Coordenadas XY en Latitud Geodésica
2) Coordenadas XYZ
3) Coordenadas XZ en Latitud Geocéntrica
4) Coordenadas XZ en Latitud Reducida
5) Primer Metodo Inverso
6) Segundo Metodo Inverso
7) Tercer Metodo Inverso 
8) Nivelación por método altimetrico
9) Nivelación por método subes-bajas
10) Programa de Bisección
Ingrese el codigo que desea usar: """))
        
        if valor == 1: 
            cords = Coords_XYZ()
            cords.calc_2D()
        elif valor == 2: 
            cords = Coords_XYZ()
            cords.calc_3D()
        elif valor == 3: 
            lats = Latitudes()
            lats.geocentrica()
        elif valor == 4: 
            lats = Latitudes()
            lats.reducida()
        elif valor == 5: 
            inv1 = Inverso1()
            inv1.geograficas()
        elif valor == 6: 
            inv2 = Inverso2()
            inv2.geograficas()
        elif valor == 7: 
            inv3 = Inverso3()
            inv3.geograficas()
        elif valor == 8: 
            niv1 = NivelacionDiferencialGeodesica()
            niv1.nivelacion_instrumental()
        elif valor == 9: 
            niv1 = NivelacionDiferencialGeodesica()
            niv1.nivelacion_subes_bajas()
        elif valor == 10:  
            bi = BisectionProgram()
            bi.calculate_bisection()

        else: 
            print("Esa no es una opción dentro del menú.")
            codigos.interactuador(self)
        
codigos = Menu()
codigos.interactuador()