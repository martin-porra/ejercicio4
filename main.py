from clase import  FechaHora
from datetime import datetime

if __name__ == '__main__':
   strDate = '2/4/18'
   objDate = datetime.strptime(strDate, '%m/%d/%y')
   d = int(input("Ingrese Dia: "))
   mes = int(input("Ingrese Mes: "))
   a = int(input("Ingrese Año: "))
   h = int(input("Ingrese Hora: "))
   m = int(input("Ingrese Minutos: "))
   s = int(input("Ingrese Segundos: "))
   r = FechaHora()  # inicilizar día, mes, año con 1/1/2020, y hora, minutos y
   #  segundos con 0h, 0m, 0s.
   r1 = FechaHora(a, mes, d);  # inicializar con 0h 0m 0s
   r2 = FechaHora(a, mes, d, h, m, s)
   r.Mostrar()
   r1.Mostrar()
   r2.Mostrar()
   r.PonerEnHora(5)  # solamente la hora
   r.Mostrar()
   r1.PonerEnHora(13, 30)  # hora y minutos
   r1.Mostrar()
   r.PonerEnHora(14, 30, 25)  # hora, minutos y segundos
   r.Mostrar()
   r.AdelantarHora(4)  # sumar 3 horas a la hora actual
   r.Mostrar()
   r2.AdelantarHora(5, 15)  # sumar 1 hora y 15 minutos a la hora actual
   r2.Mostrar()
