import matplotlib.pyplot as plt

class NivelacionGeodesica:
    def __init__(self):
        self.todos = []
        self.ejex = []
        self.ejey = []

    def nivelacion_instrumental(self):
        n_est = int(input("Inserta El Numero De Estaciones: "))
        pt1 = input("Inserta El Nombre Del Punto 1: ")
        vista_mas = round(float(input("V+: ")), 6)
        cota_ini = round(float(input("Inserta La Cota Del Punto: ")), 6)
        hi = round(cota_ini + vista_mas, 6)
        self.todos = [[pt1, cota_ini]]
        self.ejex = [0]
        self.ejey = [cota_ini]
        for _ in range(n_est - 1):
            print("¿Tiene Vista Intermedia?: ")
            tiene = int(input("Si(1) o No(2): "))
            if tiene == 1:
                num_vi = int(input("¿Cuantas VI Tienes?: "))
                for _ in range(num_vi):
                    vi_nombre = input("Inserta El Nombre De La VI: ")
                    vi_valor = round(float(input("Inserta el valor de VI: ")), 6)
                    cota_vi = round(hi - vi_valor, 6)
                    self.todos.append([vi_nombre, cota_vi])
            estacion = input("Inserta El Nombre Del Punto: ")
            vista_mas = round(float(input("V+: ")), 6)
            vista_menos = round(float(input("V-: ")), 6)
            cota_este = round(hi - vista_menos, 6)
            hi_este = round(cota_este + vista_mas, 6)
            hi = round(hi_este, 6)
            self.todos.append([estacion, cota_este])
            distancia = round(float(input("Inserte la Distancia entre estas dos estaciones: ")), 6)
            calculada = round(distancia + self.ejex[-1], 6)
            self.ejex.append(calculada)
            self.ejey.append(cota_este)
        print("Cotas...")
        print("Nombre...", "Cota...")
        for i in self.todos:
            print([round(elem, 6) if isinstance(elem, float) else elem for elem in i])
        print("*" * 28)
        plt.plot(self.ejex, self.ejey, ":", color="b")
        plt.xlabel("Distancia En M")
        plt.ylabel("Altura En M (A.S.N.M)")
        plt.show()

    def nivelacion_subes_bajas(self):
        n_est = int(input("Inserta El Numero De Estaciones: "))
        pt1 = input("Inserta El Nombre De La Estacion:")
        dist_e1 = 0
        vista_mas1 = round(float(input("V+: ")), 6)
        cota_ini = round(float(input("Inserta La Cota De La Estacion:")), 6)
        self.todos = [[pt1, cota_ini]]
        self.ejex = [dist_e1]
        self.ejey = [cota_ini]
        for _ in range(n_est - 1):
            print("Tiene Vista Intermedia?")
            tiene = float(input("¿Si(1) o No(2)?: "))
            if tiene == 1:
                num_vi = int(input("¿Cuantas Tienes?: "))
                for _ in range(num_vi):
                    vi_nombre = input("Inserta El Nombre De La VI: ")
                    vi_valor = round(float(input("Inserta el valor de VI: ")), 6)
                    sube_o_baja = round(vista_mas1 - vi_valor, 6)
                    if sube_o_baja < 0:
                        cota_vi = round(cota_ini - abs(sube_o_baja), 6)
                        if sube_o_baja > 0:
                            cota_vi = round(cota_ini + abs(sube_o_baja), 6)
                        self.todos.append([vi_nombre, round(sube_o_baja, 6), cota_vi])
                    else:
                        self.todos.append([vi_nombre, round(sube_o_baja, 6), cota_ini])
            estacion = input("Inserta El Nombre De La Estacion: ")
            vista_mas = round(float(input("V+: ")), 6)
            vista_menos = round(float(input("V-: ")), 6)
            sube_o_baja = round(vista_mas1 - vista_menos, 6)
            vista_mas1 = round(vista_mas, 6)
            if sube_o_baja < 0:
                cota_este = round(cota_ini - abs(sube_o_baja), 6)
                self.ejey.append(cota_este)
                cota_ini = round(cota_este, 6)
                self.todos.append([estacion, cota_este])
            if sube_o_baja > 0:
                cota_este = round(cota_ini + abs(sube_o_baja), 6)
                self.ejey.append(cota_este)
                cota_ini = round(cota_este, 6)
                self.todos.append([estacion, round(sube_o_baja, 6), cota_este])
            distancia = round(float(input("Inserte la Distancia entre estas dos estaciones: ")), 6)
            calculada = round(distancia + self.ejex[-1], 6)
            self.ejex.append(calculada)
        print("Cotas...")
        print("Nombre...", "Cota...")
        for i in self.todos:
            print([round(elem, 6) if isinstance(elem, float) else elem for elem in i])
        print("*" * 28)
        plt.plot(self.ejex, self.ejey, ":", color="b")
        plt.show()

def main():
    print("Calculadora Geodesica - nivelación")
    print("1. Programa Nivelacion")
    seleccion = float(input("Tu Eleccion Fue: "))
    nivelacion = NivelacionGeodesica()

    if seleccion == 1:
        print("*" * 30)
        print("Programa Nivelacion Diferencial Geodesica")
        print("¿Cual Metodo Desea Utilizar?")
        print("1. Nivelacion Altura Instrumental")
        print("2. Nivelacion Subes Y Bajas")
        sub_seleccion = float(input("Tu Eleccion Es: "))
        print("*" * 30)
        if sub_seleccion == 1:
            nivelacion.nivelacion_instrumental()
        elif sub_seleccion == 2:
            nivelacion.nivelacion_subes_bajas()

if __name__ == "__main__":
    main()
