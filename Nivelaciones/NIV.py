import matplotlib.pyplot as plt

class NivelacionDiferencialGeodesica:
    def __init__(self):
        self.todos = []
        self.ejex = []
        self.ejey = []

    def nivelacion_instrumental(self):
        Numero_Estaciones = int(input("Inserta El Numero De Estaciones: "))
        Estacion1 = input("Inserta El Nombre Del Punto 1: ")
        VistaMas = float(input("V+: "))
        CotaIni = float(input("Inserta La Cota Del Punto: "))
        Hi = CotaIni + VistaMas
        self.todos = [[Estacion1, CotaIni]]
        self.ejex = [0]
        self.ejey = [CotaIni]
        for _ in range(Numero_Estaciones - 1):
            print("¿Tiene Vista Intermedia?: ")
            Tiene = int(input("Si(1) o No(2): "))
            if Tiene == 1:
                NumVI = int(input("¿Cuantas VI Tienes?: "))
                for _ in range(NumVI):
                    VistaIntermedia = input("Inserta El Nombre De La VI: ")
                    VistaInter = float(input("Inserta el valor de VI: "))
                    CotaVi = Hi - VistaInter
                    self.todos.append([VistaIntermedia, CotaVi])
            Estacion = input("Inserta El Nombre Del Punto: ")
            VistaMas = float(input("V+: "))
            VistaMenos = float(input("V-: "))
            CotaEste = Hi - VistaMenos
            HiEste = CotaEste + VistaMas
            Hi = HiEste
            self.todos.append([Estacion, CotaEste])
            Distancia = float(input("Inserte la Distancia entre estas dos estaciones: "))
            Calculada = Distancia + self.ejex[-1]
            self.ejex.append(Calculada)
            self.ejey.append(CotaEste)
        self.mostrar_resultados()

    def nivelacion_subes_bajas(self):
        Numero_Estaciones = int(input("Inserta El Numero De Estaciones: "))
        Estacion1 = input("Inserta El Nombre De La Estacion:")
        DistanciaE1 = 0
        VistaMas1 = float(input("V+: "))
        CotaIni = float(input("Inserta La Cota De La Estacion:"))
        self.todos = [[Estacion1, CotaIni]]
        self.ejex = [DistanciaE1]
        self.ejey = [CotaIni]
        for _ in range(Numero_Estaciones - 1):
            print("Tiene Vista Intermedia?")
            Tiene = float(input("¿Si(1) o No(2)?: "))
            if Tiene == 1:
                NumVI = int(input("¿Cuantas Tienes?: "))
                for _ in range(NumVI):
                    VistaIntermedia = input("Inserta El Nombre De La VI: ")
                    VistaInter = float(input("Inserta el valor de VI: "))
                    SubeOBaja = VistaMas1 - VistaInter
                    if SubeOBaja < 0:
                        CotaVi = CotaIni - abs(SubeOBaja)
                        if SubeOBaja > 0:
                            CotaVi = CotaIni + abs(SubeOBaja)
                        self.todos.append([VistaIntermedia, SubeOBaja, CotaVi])
            Estacion = input("Inserta El Nombre De La Estacion: ")
            VistaMas = float(input("V+: "))
            VistaMenos = float(input("V-: "))
            SubeOBaja = VistaMas1 - VistaMenos
            VistaMas1 = VistaMas
            if SubeOBaja < 0:
                CotaEste = CotaIni - abs(SubeOBaja)
                self.ejey.append(CotaEste)
                CotaIni = CotaEste
                self.todos.append([Estacion, CotaEste])
            if SubeOBaja > 0:
                CotaEste = CotaIni + abs(SubeOBaja)
                self.ejey.append(CotaEste)
                CotaIni = CotaEste
                self.todos.append([Estacion, SubeOBaja, CotaEste])
            Distancia = float(input("Inserte la Distancia entre estas dos estaciones: "))
            Calculada = Distancia + self.ejex[-1]
            self.ejex.append(Calculada)
        self.mostrar_resultados()

    def mostrar_resultados(self):
        print("Cotas...")
        print("Nombre...","Cota...")
        for i in self.todos:
            print(i)
        print("*" * 28)
        plt.plot(self.ejex, self.ejey, ":", color="b")
        plt.xlabel("Distancia En M")
        plt.ylabel("Altura En M (A.S.N.M)")
        plt.show()

def main():
    print("*" * 30)
    print("Programa Nivelacion Diferencial Geodesica")
    print("¿Cual Metodo Desea Utilizar?")
    print("1. Nivelacion Altura Instrumental")
    print("2. Nivelacion Subes Y Bajas")
    seleccion = float(input("Tu Eleccion Es: "))
    print("*" * 30)
    nivelacion = NivelacionDiferencialGeodesica()

    if seleccion == 1:
        nivelacion.nivelacion_instrumental()
    elif seleccion == 2:
        nivelacion.nivelacion_subes_bajas()

if __name__ == "__main__":
    main()
