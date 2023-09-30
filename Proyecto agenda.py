import os #Importamos la libreria OS    

#Carpeta de contactos 
CARPETA = 'contactos/'
EXTENSION = '.txt' #Extencion del archivo

#Creamos clase de contactos
class Contacto: 
    def __init__(self, nombre, telefono, categoria): #Creamos constructor 
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
        

#Creamos funcion app
def app():
    #Llamamos las funciones
    crear_directorio() #Funcion para revisar si la carpeta ya existe o no
    mostrar_menu() #Funcion para elegir menu del opcion

    #Preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Selecciona una opcion: \r\n') #Requiere la opcion
        opcion = int(opcion) #Convierte string a int

        #Ejecutar opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False 
        elif opcion == 2: 
            editar_contacto()
            preguntar = False
        elif opcion == 3: 
            mostrar_contactos()
            preguntar = False
        elif opcion == 4: 
            buscar_contacto()
            preguntar = False
        elif opcion == 5: 
            eliminar_contacto()
            preguntar = False            
        elif opcion ==6:
            print('Opcion Salir del programa, adios :)')
            exit()
        else:
            print('Opcion no valida, vuelve a intentarlo')


#Creamos funcion mostrar_menu
def mostrar_menu(): #Funcion para elegir opcion del menu Desde aqui la creamos
    print('Selecciona del menú lo que deseas hacer')
    print('(1) Agregar nuevo contacto')
    print('(2) Editar contacto')
    print('(3) Ver contactos')
    print('(4) Buscar contacto')
    print('(5) Eliminar contacto')
    print('(6) Salir del programa')

#Creamos funcion para agregar contacto
def agregar_contacto():
    print('**Opcion: Agregar contacto**')
    print('Escribe los datos para agregar un nuevo contacto')
    nombre_contacto = input('Nombre del contacto: \r\n').title()

    #Revisamos si el contacto ya existie
    existe = existe_contacto(nombre_contacto)

    if not existe: #Si el archivo no existe creara el archivo y pedira la informacion

        #Crea el archivo que quedaria Carpeta/nombre_contaco.EXTENSION 
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:#Tenemos que dar el permiso de escritura. Todo esto se llamara archivo
        #Los + sirven para unir variables, en esta caso como no se junta con string no es necesaria la f. Crea el archivo dentro de la carpeta

            #agregamos el resto de los campos
            telefono_contacto = input('Agrega el telefono \r\n')
            categoria_contacto = input('Agrega la categoria \r\n')

            #Instanciamos la clase, metemos todos estos datos dentro de la clase
            contacto = Contacto (nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribimos en el archivo
            archivo.write('Nombre: ' + nombre_contacto + '\r\n') #Escribre dentro del archivo este dato
            archivo.write('Telefono: ' + telefono_contacto + '\r\n') #Escribre dentro del archivo este dato
            archivo.write('Categoria: ' + categoria_contacto + '\r\n') #Escribre dentro del archivo este dato

            #Muestra un mensaje de exito
            print('\r\n Registro exitoso \r\n')
            app()

    else: 
        print('Este contacto ya existe. \r\n')

        #Reiniciar el programa llamando la funcion app
        app()


#Creamos funcion: mostrar_contactos
def mostrar_contactos():
    print('Opcion ver contactos \n\r')
    archivos = os.listdir(CARPETA) #Hace un listado de los archivos que esten en la carpeta 

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)] #Corre por el codigo para que nos enumere los archivos que cuenten  con     esta   extencion que le estamos diciendo

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos
                print(linea.rstrip())
                #Imprime un separador
            
            #print('\r\n')
            print('------')


#Funcion buscar contacto
def buscar_contacto():
    print('Opcion buscar contacto')
    nombre = input('Seleccione el contacto que desea buscar').title()
   
   #Valida de que el archvivo exista
    try: 
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El contacto no existe')
        print(IOError)
    
    #Reinicia la app
    app()


#Funcion eliminar contacto
def eliminar_contacto():
    print('Opcion eliminar contacto \r\n')
    nombre = input('Cual es el contacto que quieres eliminar?').title()

    try:
        os.remove(CARPETA + nombre + EXTENSION) #Esto borra el archivo
        print('\r\n Usuario eliminado correctamente')

        #Reinicia la app
        app()

    except FileNotFoundError as identifier: #Si no exite el archivo manda el siguiente error
        print('El contacto no existe')
        print(FileNotFoundError)
        print('\r\n')

        #Reinicia la app
        eliminar_contacto()

#Funcion editar contacto
def editar_contacto():
    print('**Opcion: Editar contacto**')
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    existe = existe_contacto(nombre_anterior)
    if existe:
        print('Puedes editar el contacto')
        #Datos a editar
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('Agrega el nuevo nombre \r\n')
            telefono_contacto = input('Agrega el nuevo telefono \r\n')
            categoria_contacto = input('Agrega la nueva categoria \r\n')

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: ' + nombre_contacto + '\r\n') 
            archivo.write('Telefono: ' + telefono_contacto + '\r\n')
            archivo.write('Categoria: ' + categoria_contacto + '\r\n')

        #Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

        print('El contacto se ha editado correctamente')

    else:
        print('El usuario no existe')
        app() #Reinicia la app

#Funcion crear directorio
def crear_directorio():
    if not os.path.exists(CARPETA): #si la carpeta contactos no extiste
        os.makedirs(CARPETA) #Crea la carpeta contactos
    #else:
        #print('La carpeta ya existe')

#Creamos funcion existe_contacto
def existe_contacto(nombre): 
    return os.path.isfile(CARPETA + nombre + EXTENSION)
app()