from coords import Coords_XYZ
from Latitudes import Latitudes
from calc_inv1 import Inverso1
from calc_inv2 import Inverso2
from calc_inv3 import Inverso3

cords = Coords_XYZ()
inv1 = Inverso1()
inv2 = Inverso2()
inv3 = Inverso3()
lats = Latitudes()

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
Ingrese el codigo que desea usar: """))
        
        if valor == 1: cords.calc_2D()
        elif valor == 2: cords.calc_3D()
        elif valor == 3: lats.geocentrica()
        elif valor == 4: lats.reducida()
        elif valor == 5: inv1.geograficas()
        elif valor == 6: inv2.geograficas()
        elif valor == 7: inv3.geograficas()

        else: 
            print("Esa no es una opción dentro del menú.")
            codigos.interactuador(self)
        
codigos = Menu()
codigos.interactuador()