from flask import Flask, render_template, request
from coords import Coords_XYZ
from Codigos_POO_GEO.Coords_Inv.Backend.Latitudes import Latitudes
from calc_inv1 import Inverso1
from calc_inv2 import Inverso2
from calc_inv3 import Inverso3
from Bajada import NivelacionDiferencialGeodesica
from Biseccion import BisectionProgram

class MenuApp:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route('/')
        def menu():
            return render_template('menu.html')

        @self.app.route('/procesar', methods=['POST'])
        def procesar():
            valor = int(request.form['codigo'])
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
                return "Esa no es una opción dentro del menú."

            return "Operación completada."

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    menu_app = MenuApp()
    menu_app.run()
