import re #libreria python expresiones regulares

class Email(): 
    #variables de la clase
    __idCuenta = ''
    __dominio = ''
    __tipoDom = ''
    __contraseña = ''

    #constructor de la clase (apartado a)
    def __init__(self):
      #print("Datos para armar su Email \n")
        self.__idCuenta = ''
        self.__dominio = ''
        self.__tipoDom = '' 
        self.__contraseña = ''

    #retorna email(apartado b)

    def retornaEmail(self):
        #forma 1-  f"{self.idCuenta}@{self.dominio}.{self.tipoDom}" (siempre string)
        #forma 2- '{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipoDom)
        #forma 3- '{0}@{1}.{2}'.format(self.__idCuenta,self.__dominio,self.__tipoDom)
        #forma 4- "%s@%s.%s".format(self.__idCuenta,self.__dominio,self.__tipoDom)

        return '{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipoDom)
        

    #metodo get dominio (apartado c)
    def getDominio(self): 
        return self.__dominio


    #metodo crear cuenta (apartado d)
    def crearCuenta(self,email,passw=None): 
        #validar correo
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',email.lower()): #hago correo todo en minusculas
            lista1 = email.split("@") #divido el correo [idCuenta, dominio.tipoDominio]
            self.__idCuenta = lista1[0]
            lista2 = lista1[1].split(".") #estoy ubicado en dominio tipo dominio [dominio,tipodominio]
            self.__tipoDom = lista2[1]
            self.__dominio = lista2[0]
            passw = input("Ingresar contraseña para el correo ya creado: ")
            self.__contraseña = passw
            print("Su correo es : {}".format(self.retornaEmail())) #me devuelve el correo 
            print("Su contraseña es: {}".format(self.__contraseña))
            print("El dominio del email ingresado es: {}".format(self.__dominio))
            error = False  
        else:
            print("Correo incorrecto")
            error = True
        
        return error



    #ejercicio 2, clase creada para modificar la contraseña
    def setPassw(self,actual,nueva): 

        if actual == self.__contraseña:
            self.__contraseña = nueva
            print("Contraseña actual: ",self.__contraseña)
        else:
            print("Contraseñas no coinciden,no se a podido cambiar su contraseña ")


    #ejercicio 4 
    def direcEmail(self,email,password=None):
           #validar correo
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',email.lower()): #hago correo todo en minusculas
            listaX = email.split("@") #divido el correo [idCuenta, dominio.tipoDominio]
            self.__idCuenta = listaX[0]
            listaY = listaX[1].split(".") #estoy ubicado en dominio tipo dominio [dominio,tipodominio]
            self.__tipoDom = listaY[1]
            self.__dominio = listaY[0]
            if password:
                self.__contraseña = password
            else:
                self.__contraseña = input("Ingrese contraseña: ")

            print("Su correo es : {}".format(self.retornaEmail())) #me devuelve el correo 
            print("Su contraseña es: {}".format(self.__contraseña))
            print("El dominio del email ingresado es: {}".format(self.__dominio))
            error = False  
        else:
            print("Correo incorrecto")
            error = True
      
        return error


        # vif re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()): expresion regular

        # actual = input("Ingresar contraseña actual: ")

