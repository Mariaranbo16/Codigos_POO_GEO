import math
from cmath import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

print("*"*30)
print("Programa Nivelacion Diferencial Geodesica")
print("¿Cual Metodo Desea Utilizar?")
print("1. Nivelacion Altura Instrumental")
print("2. Nivelacion Subes Y Bajas")
Slecion=float(input("Tu Eleccion Es: "))
print("*"*30)
if Slecion==1:
    Numero_Estaciones=int(input("Inserta El Numero De Estaciones: "))
    Estacion1=(input("Inserta El Nombre Del Punto 1: "))
    VistaMas=float(input("V+: "))
    CotaIni=float(input("Inserta La Cota Del Punto: "))
    Hi=CotaIni+VistaMas
    Hola=[Estacion1,CotaIni]
    Todos=[Hola]
    ejex=[]
    ejex.append(0)
    ejey=[]
    ejey.append(CotaIni)
    for i in range(0,Numero_Estaciones-1):
        print("¿Tiene Vista Intermedia?: ")
        Tiene=int(input("Si(1) o No(2): "))
        if Tiene==1:
            NumVI=int(input("¿Cuantas VI Tienes?: "))
            for x in range(NumVI):
                VistaIntermedia=(input("Inserta El Nombre De La VI: "))
                VistaInter=float(input("Inserta el valor de VI: "))
                CotaVi=Hi-VistaInter
                Holaa=[VistaIntermedia,CotaVi]
                Todos.append(Holaa)
        Estacion=(input("Inserta El Nombre Del Punto: "))
        VistaMas=float(input("V+: "))
        VistaMenos=float(input("V-: "))
        CotaEste=Hi-VistaMenos
        HiEste=CotaEste+VistaMas
        Hi=HiEste
        Holaaa=[Estacion,CotaEste]
        Todos.append(Holaaa)
        Distancia=float(input("Inserte la Distancia entre estas dos estaciones: "))
        Calculada=Distancia+(ejex[-1])
        ejex.append(Calculada)
        ejey.append(CotaEste)
    print("Cotas...")
    print("Nombre...","Cota...")
    for i in Todos:  
        print(i)
    print("*"*28)
    plt.plot(ejex,ejey, ":",color="b")
    plt.xlabel("Distancia En M")
    plt.ylabel("Altura En M (A.S.N.M)")
    plt.show()
if Slecion==2:
    Numero_Estaciones=int(input("Inserta El Numero De Estaciones: "))
    Estacion1=(input("Inserta El Nombre De La Estacion:"))
    DistanciaE1=0
    VistaMas1=float(input("V+: "))
    CotaIni=float(input("Inserta La Cota De La Estacion:"))
    Hola=[Estacion1,CotaIni]
    Todos=[Hola]
    Ejex=[]
    Ejex.append(DistanciaE1)
    Ejey=[]
    Ejey.append(CotaIni)
    for i in range(0,Numero_Estaciones-1):
        print("Tiene Vista Intermedia?")
        Tiene=float(input("¿Si(1) o No(2)?: "))
        if Tiene==1:
            NumVI=int(input("¿Cuantas Tienes?: "))
            for x in range(NumVI):
                VistaIntermedia=(input("Inserta El Nombre De La VI: "))
                VistaInter=float(input("Inserta el valor de VI: "))
                SubeOBaja=VistaMas1-VistaInter
                if SubeOBaja<0:
                    CotaVi=CotaIni-abs(SubeOBaja)
                    if SubeOBaja>0:
                        CotaVi=CotaIni+abs(SubeOBaja)
                    Holaa=[VistaIntermedia,SubeOBaja,CotaVi]
                    Todos.append(Holaa)
        Estacion=(input("Inserta El Nombre De La Estacion: "))
        VistaMas=float(input("V+: "))
        VistaMenos=float(input("V-: "))
        SubeOBaja=VistaMas1-VistaMenos
        VistaMas1=VistaMas
        if SubeOBaja<0:
            CotaEste=CotaIni-abs(SubeOBaja)
            Ejey.append(CotaEste)
            CotaIni=CotaEste
            Holaaa=[Estacion,CotaEste]
            Todos.append(Holaaa)
        if SubeOBaja>0:
            CotaEste=CotaIni+abs(SubeOBaja)
            Ejey.append(CotaEste)
            CotaIni=CotaEste
            Holaaa=[Estacion,SubeOBaja,CotaEste]
            Todos.append(Holaaa)
        Distancia=float(input("Inserte la Distancia entre estas dos estaciones: "))
        Calculada=Distancia+(Ejex[-1])
        Ejex.append(Calculada)
    print("Cotas...")
    print("Nombre...","Cota...")
    for i in Todos:
        print(i)
    print("*"*28)
    plt.plot(Ejex,Ejey, ":",color="b")
    plt.show()
