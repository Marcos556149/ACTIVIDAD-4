from ClaseFechaHora import FechaHora
if __name__=='__main__':
   pruebaTest=FechaHora()       #crea objeto para invocar al metodo test
   pruebaTest.test()
   d=int(input('Ingrese Dia: '))
   mess=int(input('Ingrese Mes: '))
   a=int(input("Ingrese Year: "))
   h=int(input('Ingrese Hora: '))
   m=int(input('Ingrese Minutos: '))
   s=int(input('Ingrese Segundos: '))
   r=FechaHora()
   r1=FechaHora(a,mess,d)
   r2=FechaHora(a,mess,d,h,m,s)
   r.Mostrar()
   r1.Mostrar()
   r2.Mostrar()
   input()
   r.PonerEnHora(5)
   r.Mostrar()
   input()
   r2.PonerEnHora(13,30)
   r2.Mostrar()
   input()
   r.PonerEnHora(14,30,25)
   r.Mostrar()
   input()
   r.AdelantarHora(3)
   r.Mostrar()
   input()
   r1.AdelantarHora(1,15)
   r1.Mostrar()
   input()



