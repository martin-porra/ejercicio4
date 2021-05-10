

class FechaHora:
    __año : ''
    __mes = ''
    __dia = ''
    __minuto = ''
    __hora = ''
    __segundos = ''

    def __init__(self,año = '2020', mes = '1', dia = '1', hora = '0', minuto = '0', segundo = '0'):
       if int(año) < 2022:
        self.__año = año
       else:
         self.__año = 2020
       if int(mes) <= 12:
         self.__mes = mes
       else:
        self.__mes = 1
       if int(dia) <= 31:
        self.__dia = dia
       else:
        self.__dia = 1
       if int(hora) <= 24:
        self.__hora = hora
       else:
         self.__hora = 0
       if int(minuto) <= 60:
        self.__minuto = minuto
       else:
        self.__minuto = 0
       if int(segundo) <= 60:
        self.__segundos = segundo
       else:
         self.__segundos = 0
       if mes == 2 and dia > 28:
         if not año % 4 and (año % 100 or  not año % 400):
           print('a')
           self.__dia = 29
         else:
             self.__dia = 28
       if mes == 4 and dia == 31:
         self.__dia = 30
       if mes == 6 and dia == 31:
         self.__dia = 30
       if mes == 9 and dia == 31:
         self.__dia = 30
       if mes == 11 and dia == 31:
         self.__dia = 30


    def Mostrar(self):
     print(  'fecha :' + str(self.__dia)  + '/' + str(self.__mes) + '/' + str(self.__año) + '  hora :' + str(self.__hora) + 'h '+ str(self.__minuto) + 'm ' + str(self.__segundos) + 's' )
    def PonerEnHora(self,hora = 25, minuto = 61, segundo = 61):
        if int(hora) <= 24:
            self.__hora = hora
        if int(minuto) <= 60:
           self.__minuto = minuto
        if int(segundo) <= 60:
           self.__segundos = segundo
    def AdelantarHora(self, hora = 0, minuto = 0):
        self.__hora = int(self.__hora) + int(hora)
        self.__minuto = int(self.__minuto) + int(minuto)
        if self.__minuto > 60:
          self.__minuto =  self.__minuto - 60
          self.__hora = self.__hora + 1
          if self.__hora > 24:
            self.__hora =   self.__hora - 24
            self.__hora = self.__hora - 1
            self.__dia = self.__dia +1
            if self.__mes == 12:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
                if self.__mes > 12:
                  self.__mes =  self.__mes  - 12
                  self.__año = self.__año + 1
            elif self.__mes == 1:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 3:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 5:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 7:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 8:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 10:
              if self.__dia > 31:
                self.__dia =  self.__dia - 31
                self.__mes = self.__mes +1
            elif self.__mes == 4:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 6:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 9:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 11:
              if self.__dia > 30:
                self.__dia = self.__dia - 30
                self.__mes = self.__mes + 1
            elif self.__mes == 2:
              if self.__dia > 28:
                if not self.__año % 4 and (self.__año % 100 or not self.__año % 400):
                   if self.__dia == 29:
                     self.__mes = 2
                     self.__dia = 29
                   else:
                     self.__mes = 3
                     self.__dia = 1
                else:
                  self.__dia = self.__dia - 28
                  self.__mes = self.__mes + 1


    def __Add__(self, FechaHora):
        suma = FechaHora.__segundos + self.__segundos
        self.__segundos = suma
        suma = FechaHora.__minuto + self.__minuto
        self.__minuto = suma
        suma = FechaHora.__hora + self.__hora
        self.__hora = suma
        suma = FechaHora.__dia + self.__dia
        self.__dia = suma
        suma = FechaHora.__mes + self.__mes
        self.__mes = suma
        suma = FechaHora.__año + self.__año
        self.__año = suma
    def seg(self):
        print(self.__segundos)