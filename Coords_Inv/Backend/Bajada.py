import matplotlib.pyplot as plt

class NivelacionDiferencialGeodesica:
    # Atributos
    def __init__(self):
        self.todos = []   # Almacena toda la info total
        self.ejex = []
        self.ejey = []

    def nivelacion_instrumental(self):
        Numero_Estaciones = int(input("Numero de estaciones: "))
        Estacion1 = input("Nombre de la estación: ")
        VistaMas = round(float(input("V+: ")), 6)
        CotaIni = round(float(input("Cota de la estación: ")), 6)
        Hi = round(CotaIni + VistaMas, 6)
        self.todos = [[Estacion1, CotaIni]]
        self.ejex = [0]
        self.ejey = [CotaIni]
        for _ in range(Numero_Estaciones - 1):
            print("¿Tiene vista intermedia?: ")
            Tiene = int(input("Si(1) o No(2): "))
            if Tiene == 1:
                NumVI = int(input("¿Cuantas VI tiene?: "))
                for _ in range(NumVI):
                    VistaIntermedia = input("Nombre de la VI: ")
                    VistaInter = round(float(input("Valor de VI: ")), 6)
                    CotaVi = round(Hi - VistaInter, 6)
                    self.todos.append([VistaIntermedia, CotaVi])
            Estacion = input("Nombre del cambio: ")
            VistaMas = round(float(input("V+: ")), 6)
            VistaMenos = round(float(input("V-: ")), 6)
            CotaEste = round(Hi - VistaMenos, 6)
            HiEste = round(CotaEste + VistaMas, 6)
            Hi = round(HiEste, 6)
            self.todos.append([Estacion, CotaEste])
            Distancia = round(float(input("Distancia entre las estaciones: ")), 6)
            Calculada = round(Distancia + self.ejex[-1], 6)
            self.ejex.append(Calculada)
            self.ejey.append(CotaEste)
        self.mostrar_resultados()

    def nivelacion_subes_bajas(self):
        Numero_Estaciones = int(input("Numero de estaciones: "))
        Estacion1 = input("Nombre de la estacion: ")
        DistanciaE1 = 0
        VistaMas1 = round(float(input("V+: ")), 6)
        CotaIni = round(float(input("Cota de la estacion: ")), 6)
        self.todos = [[Estacion1, CotaIni]]
        self.ejex = [DistanciaE1]
        self.ejey = [CotaIni]
        for _ in range(Numero_Estaciones - 1):
            print("Tiene vista intermedia?")
            Tiene = float(input("¿Si(1) o No(2)?: "))
            if Tiene == 1:
                NumVI = int(input("¿Cuantas tiene?: "))
                for _ in range(NumVI):
                    VistaIntermedia = input("Nombre de la VI: ")
                    VistaInter = round(float(input("Valor de VI: ")), 6)
                    SubeOBaja = round(VistaMas1 - VistaInter, 6)
                    if SubeOBaja < 0:
                        CotaVi = round(CotaIni - abs(SubeOBaja), 6)
                        if SubeOBaja > 0:
                            CotaVi = round(CotaIni + abs(SubeOBaja), 6)
                        self.todos.append([VistaIntermedia, round(SubeOBaja, 6), CotaVi])
                    else:
                        CotaIntermedia = round(CotaIni + SubeOBaja, 6)
                        self.todos.append([VistaIntermedia, round(SubeOBaja, 6), CotaIntermedia])
            Estacion = input("Nombre del cambio: ")
            VistaMas = round(float(input("V+: ")), 6)
            VistaMenos = round(float(input("V-: ")), 6)
            SubeOBaja = round(VistaMas1 - VistaMenos, 6)
            VistaMas1 = round(VistaMas, 6)
            if SubeOBaja < 0:
                CotaEste = round(CotaIni - abs(SubeOBaja), 6)
                self.ejey.append(CotaEste)
                CotaIni = round(CotaEste, 6)
                self.todos.append([Estacion, round(CotaEste, 6)])
            if SubeOBaja > 0:
                CotaEste = round(CotaIni + abs(SubeOBaja), 6)
                self.ejey.append(CotaEste)
                CotaIni = round(CotaEste, 6)
                self.todos.append([Estacion, round(SubeOBaja, 6), round(CotaEste, 6)])
            Distancia = round(float(input("Distancia entre las estaciones: ")), 6)
            Calculada = round(Distancia + self.ejex[-1], 6)
            self.ejex.append(Calculada)
        self.mostrar_resultados()

    def mostrar_resultados(self):
        print("Cotas...")
        print("Nombre...","Cota...")
        for i in self.todos:
            print([round(elem, 6) if isinstance(elem, float) else elem for elem in i])
        print("*" * 28)
        plt.plot(self.ejex, self.ejey, linestyle='-', color='green')
        plt.xlabel("Distancia En M")
        plt.ylabel("Altura En M")
        plt.grid(True) 
        plt.title("Gráfico de Nivelación")  
        plt.show()


def main():
    print("*" * 30)
    print("Programa Nivelacion")
    print("¿Cual Metodo Desea Utilizar?")
    print("1. Altura Instrumental")
    print("2. Subes Y Bajas")
    seleccion = float(input("Tu Eleccion Es: "))
    print("*" * 30)
    nivelacion = NivelacionDiferencialGeodesica()

    if seleccion == 1:
        nivelacion.nivelacion_instrumental()
    elif seleccion == 2:
        nivelacion.nivelacion_subes_bajas()

if __name__ == "__main__":
    main()
