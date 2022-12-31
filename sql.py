"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""
import sqlite3
from os import system 

def crearBaseDeDatos():
    conexion = sqlite3.connect("OpenBootcamp.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("""
        CREATE TABLE alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dni VARCHAR(8) UNIQUE NOT NULL,
            nombre VARCHAR(10)  NOT NULL,
            apellido VARCHAR(10) NOT NULL,
            edad INTEGER NOT NULL)""")
    except sqlite3.OperationalError:
        print("Table Alumnos already Exists")
    else:
        print("La tabla ya esta creada")
    
    conexion.close()

def agregarAlumno():
    print("Insertar los siguientes datos del Alumno")
    dni = input("dni_> : ")
    nombre = input("Name_> : ")
    apellido = input("Apellido_> : ")
    edad = input("Edad_> : ")

    alumno = [dni,nombre,apellido,edad]
    conexion = sqlite3.connect("OpenBootcamp.db")
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO alumnos VALUES (NULL,?,?,?,?)",alumno)

    conexion.commit()
    conexion.close()

def mostrarAlumnos():
    print("Lista de alumnos: >")

    conexion = sqlite3.connect("OpenBootcamp.db")
    cursor = conexion.cursor()

    alumnos = cursor.execute("SELECT * FROM alumnos").fetchall()
    
    for alumno in alumnos:
        print(f"""N°: {alumno[0]} / DNI: {alumno[1]} / Alumno: {alumno[2]}  {alumno[3]} / Edad: {alumno[4]}""")

    conexion.commit()
    conexion.close()

crearBaseDeDatos()
while(True):
    print("AppList")
    opcion = input("""
    Introduce una Opcion:
    \t[1] Agregar Alumno
    \t[2] Mostrar Lista
    \t[3] Salir
    """)

    if opcion == "1":
        system("cls")
        agregarAlumno()
    elif opcion == "2":
        system("cls")
        mostrarAlumnos()
    elif opcion == "3":
        print("Cerrando..")
        break
    else:
        print("Opcion incorrecta, intenta de nuevo")
    