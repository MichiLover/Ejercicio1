import csv
from ClaseEmail import Email #traigo la clase email al main 

if __name__=='__main__':

    #apartado 1 
    print('APARTADO 1')
    nombre = input("Ingresar nombre: ")
    email = input("Ingrese email completo: ")
    newCuenta = Email()
    error = newCuenta.crearCuenta(email)

    while error: #me quedo en el while hasta que ingrese bien el correo
        email = input("Ingrese email completo: ")
        error = newCuenta.crearCuenta(email)
        
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre,newCuenta.retornaEmail()))

    print("------------------------------------------------------------------------------------\n")

    #Apartado 2
    print('APARTADO 2')
    actual = input("Ingrese su contraseña actual: ")
    nueva = input("Ingrese su contraseña nueva: ")
    newCuenta.setPassw(actual,nueva)
    print("------------------------------------------------------------------------------------\n")

    #apartado 3
    print('APARTADO 3')
    print('Mail ya ingresado')
    newCuenta2 = Email() 
    newCuenta2.crearCuenta("informatica.fcefn@gmail.com")
    print("------------------------------------------------------------------------------------\n")

    #apartado 4
    print('APARTADO 4')
    archivo = open("correo.csv")
    reader = csv.reader(archivo,delimiter=",")
    dominio = input("Ingresar un dominio: ")
    cont = 0 #contador de dominio
    bandera = True

    for fila in reader:
        if bandera:
            bandera = False
        else:
            newEmail = Email()
            error = newEmail.direcEmail(fila[0],fila[1])    
            print("\n")
            if not error:
                if newEmail.getDominio() == dominio: #comparo dominio del mail con el ingresado
                    cont += 1

    archivo.close()
    print("Cantidad de mail con dominio igual al ingresado {}".format(cont))
    print("\n")