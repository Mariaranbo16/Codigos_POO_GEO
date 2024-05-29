import math as mh

class Elipsoides:

    def __init__(self):

        self.lat = 0
        self.lon = 0
        self.az = 0
        self.a = 0
        self.f = 0
        self.e = 0
        self.b = 0
        self.e2 = 0
        self.N = 0
        self.R = 0
        self.ro_az = 0
        self.rad_med_curv = 0

    def elip (self):

        print("""Seleccione el elipsoide que desea trabajar: 
1) WGS 84 / GRS 80 
2) Internacional 
3) Clarke 1866 """)
        
        selec = int(input("Seleccione una opciòn: "))

        #WGS 84 / GRS 80
        if selec == 1:

            self.a = 6378137
            self.e = 0.00669438
            self.b = self.a*(mh.sqrt(1-self.e))
            self.f = 1 - (self.b / self.a)
            self.e2 = (self.a**2/self.b**2) - 1

        #Internacional
        elif selec == 2:

            self.a = 6378388
            self.e = 0.00672267
            self.b = self.a*(mh.sqrt(1-self.e))
            self.f = 1 - (self.b / self.a)
            self.e2 = (self.a**2/self.b**2) - 1

        #Clarke 1866
        elif selec == 3:

            self.a = 6378206.4
            self.e = 0.00676865
            self.b = self.a*(mh.sqrt(1-self.e))
            self.f = 1 - (self.b / self.a)
            self.e2 = (self.a**2/self.b**2) - 1

    def calc_radios(self):
        
        sinfi = mh.sin(mh.radians(self.lat))
        sinaz = mh.sin(mh.radians(self.az))
        cosaz = mh.cos(mh.radians(self.az))
        self.N = (self.a/mh.sqrt((1-(self.e*(sinfi**2)))))
        self.R= (self.a*(1-self.e))/(1-(self.e*(sinfi**2)))**(3/2)
        self.ro_az = (self.R*self.N)/((self.R*(cosaz**2))+(self.N*(sinaz**2)))
        self.rad_med_curv = mh.sqrt(self.R*self.N)