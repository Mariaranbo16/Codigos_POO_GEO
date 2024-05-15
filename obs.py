import matplotlib.pyplot as plt

class NivelacionGeodesica:
    def __init__(self):
        self.todos = []
        self.ejex = []
        self.ejey = []

    def nivelacion_instrumental(self):
        n_est = int(input("Inserta El Numero De Estaciones: "))
        pt1 = input("Inserta El Nombre Del Punto 1: ")
        vista_mas = float(input("V+: "))
        cota_ini = float(input("Inserta La Cota Del Punto: "))
        hi = cota_ini + vista_mas
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
                    vi_valor = float(input("Inserta el valor de VI: "))
                    cota_vi = hi - vi_valor
                    self.todos.append([vi_nombre, cota_vi])
            estacion = input("Inserta El Nombre Del Punto: ")
            vista_mas = float(input("V+: "))
            vista_menos = float(input("V-: "))
            cota_este = hi - vista_menos
            hi_este = cota_este + vista_mas
            hi = hi_este
            self.todos.append([estacion, cota_este])
            distancia = float(input("Inserte la Distancia entre estas dos estaciones: "))
            calculada = distancia + self.ejex[-1]
            self.ejex.append(calculada)
            self.ejey.append(cota_este)
        print("Cotas...")
        print("Nombre...", "Cota...")
        for i in self.todos:
            print(i)
        print("*" * 28)
        plt.plot(self.ejex, self.ejey, ":", color="b")
        plt.xlabel("Distancia En M")
        plt.ylabel("Altura En M (A.S.N.M)")
        plt.show()

    def nivelacion_subes_bajas(self):
        n_est = int(input("Inserta El Numero De Estaciones: "))
        pt1 = input("Inserta El Nombre De La Estacion:")
        dist_e1 = 0
        vista_mas1 = float(input("V+: "))
        cota_ini = float(input("Inserta La Cota De La Estacion:"))
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
                    vi_valor = float(input("Inserta el valor de VI: "))
                    sube_o_baja = vista_mas1 - vi_valor
                    if sube_o_baja < 0:
                        cota_vi = cota_ini - abs(sube_o_baja)
                        if sube_o_baja > 0:
                            cota_vi = cota_ini + abs(sube_o_baja)
                        self.todos.append([vi_nombre, sube_o_baja, cota_vi])
            estacion = input("Inserta El Nombre De La Estacion: ")
            vista_mas = float(input("V+: "))
            vista_menos = float(input("V-: "))
            sube_o_baja = vista_mas1 - vista_menos
            vista_mas1 = vista_mas
            if sube_o_baja < 0:
                cota_este = cota_ini - abs(sube_o_baja)
                self.ejey.append(cota_este)
                cota_ini = cota_este
                self.todos.append([estacion, cota_este])
            if sube_o_baja > 0:
                cota_este = cota_ini + abs(sube_o_baja)
                self.ejey.append(cota_este)
                cota_ini = cota_este
                self.todos.append([estacion, sube_o_baja, cota_este])
            distancia = float(input("Inserte la Distancia entre estas dos estaciones: "))
            calculada = distancia + self.ejex[-1]
            self.ejex.append(calculada)
        print("Cotas...")
        print("Nombre...", "Cota...")
        for i in self.todos:
            print(i)
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
