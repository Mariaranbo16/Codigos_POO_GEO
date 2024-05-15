import math 
from math import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


print ("Programa de nivelación Diferencial Geodésica\n")
print ("¿Cuál método desea usar?\n")
print ("1. Nivelación de altura instrumental")
print ("2. Nivelación por puntos de subes y bajas\n")

Seleccion = float (input ("Tu elección fue:\n"))
print ("*"*30)

if Seleccion == 1:

    NumEst = int(input ("¿Cuál es el número de estaciones?: "))
    Est_1 = (input ("Nombre el punto 1: "))
    VisMas = float (input ("V+: "))
    CotIni = float (input ("Cota del punto: "))
    Hi = CotIni + VisMas
    print (Hi)
    Hola = [Est_1,CotIni]
    Todos = [Hola]

    ejex =[]
    ejex.append(0)
    ejey = []
    ejey.append (CotIni)

    for i in range (0, NumEst-1):
        print ("¿Tiene vista intermedia?: ")
        Tiene = int (input ("Si (1), No (2): "))

        if Tiene == 1:
            Vi = int (input ("¿Cuántas Vi tiene?: "))

            for x in range (Vi):

                VistaInt = (input("Nombre de la Vi: "))
                VstInt = (input ("Valor Vi: "))

                CotVi = Hi - VstInt 
                Holaa = [VistaInt, CotVi]
                Todos.append (Holaa)
        
        Estacion = (input ("Nombre del punto: "))
        VisMas = float (input ("V+: "))
        VisMe = float (input ("V-: "))
        CotEst = Hi - VisMe
        HiEst = CotEst + VisMas