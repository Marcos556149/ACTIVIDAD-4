class FechaHora:
    __year = 0
    __mes = 0
    __dia = 0
    __hora = 0
    __minutos = 0
    __segundos = 0
    __meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    def __init__(self,a=2020,mess=1,d=1,h=0,m=0,s=0):
        if (self.verificarHora(h,m,s))and(self.verificarFecha(a,mess,d)):
            self.__year=a
            self.__mes=mess
            self.__dia=d
            self.__hora=h
            self.__minutos=m
            self.__segundos=s
        else:
            print("ERROR, Los datos que ingreso son invalidos")
            self.__year = -1
    def test(self):
        datosCorrectos1= FechaHora(2020,5,17,20,50,58)       #Fecha y hora validas
        datosIncorrectos1= FechaHora(2017,13,18,5,13,51)   #Fecha y hora no validas, mes invalido
        datosCorrectos2= FechaHora(2016,2,29,1,4,0)       #Fecha y hora validos, año bisiesto
        datosIncorrectos2= FechaHora(2015,2,29,23,59,59)   #Fecha y hora invalidos, año no bisiesto con fecha no existente
        datosCorrectos1.Mostrar()
        input()
        datosIncorrectos1.Mostrar()
        input()
        datosCorrectos2.Mostrar()
        input()
        datosIncorrectos2.Mostrar()
        print("\nTEST REALIZADO EXITOSAMENTE\n")
    def Mostrar(self):
        if self.__year != -1:      #si la fecha es valida entonces se muestra, el atributo year tiene el valor None solo cuando los datos de ingreso no fueron validos
            print(str(self.__hora)+'/',str(self.__minutos)+'/',str(self.__segundos),'  ',str(self.__dia)+'/',str(self.__mes)+'/',str(self.__year))
        else:
            print("No es posible Mostrar por pantalla la Fecha y la Hora ya que los datos de ingreso son incorrectos")
    def verificarHora(self,h,m,s):
        if (h>=0)and(h<=23)and(m>=0)and(m<=59)and(s>=0)and(s<=59) :
            return True
        else:
            return False
    def verificarFecha(self,a,mess,d):
        if (a>0)and(mess>=1)and(mess<=12)and(d>=1)and(d<=31):
            if (mess==2)and(d==29)and(self.verificarBisiesto(a)):
                return True
            elif self.verificarMesDia(mess,d) == 0:
                return True
            else:
                return False
    def verificarBisiesto(self,a):
        if a % 4 !=0:
            return False
        elif (a % 4 == 0)and(a % 100 != 0):
            return True
        elif (a % 4 == 0)and(a % 100 == 0)and(a % 400 != 0):
            return False
        elif (a % 4 == 0)and(a % 100 == 0)and(a % 400 == 0):
            return True
    def verificarMesDia(self,mess,d):
        if ((mess==self.__meses[0])or(mess==self.__meses[2])or(mess==self.__meses[4])or(mess==self.__meses[6])or(mess==self.__meses[7])or(mess==self.__meses[9])or(mess==self.__meses[11]))and(d>31): #verifica que los meses que tienen 31 dias no se ingrese un dia mayor que 31
            return 1
        elif ((mess==self.__meses[3])or(mess==self.__meses[5])or(mess==self.__meses[8])or(mess==self.__meses[10]))and(d>30):  #verifica que en los meses que tienen 30 dias no se ingrese un dia mayor que 30
            return 2
        elif (mess==self.__meses[1])and(d>28):   #verifica que en el mes de febrero no se ingrese un dia mayor a 28
            return 3
        else:
            return 0                          #si no es ninguna de las anteriores entonces la fecha es correcta
    def PonerEnHora(self,h=0,m=0,s=0):
        if self.__year != -1:
            if self.verificarHora(h,m,s):
                self.__hora=h
                self.__minutos=m
                self.__segundos=s
            else:
                print("Datos de ingreso invalidos")
        else:
            print("No es posible PonerEnHora ya que los datos de ingreso fueron invalidos")
    def AdelantarHora(self,h=0,m=0,s=0):
        if self.__year != -1:
            self.__hora += h
            self.__minutos += m
            self.__segundos += s
            if (self.__segundos > 59)or(self.__minutos > 59)or(self.__hora > 23):      #verifica si los segundos, minutos o horas superan la cantidad maxima, de ser asi, hace las modificaciones correspondientes
                s
                cont1=0
                cont2=0
                cont3=0
                while self.__segundos > 59:                   #tambien valida si se ingresa una gran cantidad de segundos, lo mismo mas abajo para los minutos y las horas
                    cont1 += 1
                    self.__segundos -= 60
                self.__minutos += cont1
                while self.__minutos > 59:
                    cont2 += 1
                    self.__minutos -= 60
                self.__hora += cont2
                while self.__hora > 23:
                    cont3 += 1
                    self.__hora -= 24
                if cont3 > 0:
                    self.AdelantarFecha(cont3)
        else:
            print("No es posible adelantar la hora ya que los datos de ingreso no son validos")
    def AdelantarFecha(self,cont3):
        self.__dia += cont3
        if (self.verificarMesDia(self.__mes,self.__dia) == 1):
            self.__dia -= 31
            self.__mes += 1
            if self.__mes > 12:                           #el unico lugar en el que puede ocurrir el cambio de año es aqui, ya que el ultimo mes del año tiene 31 dias
                self.__mes -= 12
                self.__year += 1
        elif (self.verificarMesDia(self.__mes,self.__dia) == 2):
            self.__dia -= 30
            self.__mes += 1
        elif (self.verificarMesDia(self.__mes,self.__dia) == 3):
            if self.verificarBisiesto(self.__year):
                if self.__dia > 29:
                    self.__dia -= 29
                    self.__mes += 1
            else:
                self.__dia -= 28
                self.__mes += 1
