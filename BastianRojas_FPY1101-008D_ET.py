#prueba

import os
import time
import random
import csv

trabajadores = ['juan perez', 'maria Garcia', 'Carlos Lopez', 'Ana martines', 'pedro rodrijez', 'laura hernandes', 'miguel sanchez', 'isabel gomez', 'francisco Diaz', 'elena fernandez']
trabajadores_dic = {
    'juan perez' : 0,
    'maria garcia' : 0,
    'carlos lopes' : 0,
    'ana martines' : 0,
    'pedro rodrijes' : 0,
    'laura hernandes' : 0,
    'miguel sanchez' : 0,
    'isabel gomez' : 0,
    'francisco Diaz' : 0,
    'elena fernandez' : 0,
}
sueldos_menores = {}
sueldos_normales = {}
sueldos_mayores = {}
trabajador = []
nada = ('nombre empleado', 'sueldo base', 'descuento salud', 'descuento AFP', 'sueldo liquido')
bl = "─" * 36
contador = True
valor = 0
desc_salud = 0
desc_afp = 0
desc1 = 0.07
desc2 = 0.12

existe = os.path.exists('reporte_sueldos.csv')

if existe == True:
    os.system("cls")
elif existe == False:
    with open('reporte_sueldos.csv', 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(nada)




def borrar(b):
    time.sleep(b)
    os.system("cls")

def menu1():
    global contador
    while contador == True:
        print(f"menu del trabajador \n{bl}")
        print(f"1) asignar sueldos aleatorios \n2) clasificar sueldos \n3) ver estadisticas \n4) reporte de sueldos \n5) salir del programa \n{bl}")
        try:
            eleguir = int(input("──> "))
        except ValueError:
            print("error en la opcion")
            borrar(1)
            continue
        if eleguir in [1,2,3,4,5]:
            borrar(0.5)
            return(eleguir)
        else:
            print("no es una opcion")
            borrar(1)

def salir_programa():
    global contador
    contador = False
    borrar(0.5)
    print("Finalizando programa… Desarrollado por Bastian Rojas RUT 21.919.711-k")

def generar_sueldo():
    global valor
    for nombre in trabajadores_dic:
        s = random.randrange(300000,2500000)
        trabajadores_dic[nombre] = s
        valor = trabajadores_dic.get(nombre)
        print(f"valor generado para {nombre}")
        borrar(0.5)
    print("todos los sueldos an sido generados")
    borrar(1)

def reporte_de_sueldos():
    global desc_salud, desc_afp, desc1, desc2
    print(*nada)
    for nombre in trabajadores_dic:
        trabajador.append(nombre)
        valor = trabajadores_dic.get(nombre)
        trabajador.append(valor)
        desc_salud = valor - (valor * desc1)
        trabajador.append(desc_salud)
        desc_afp = valor - (valor * desc2)
        trabajador.append(desc_afp)
        print(*trabajador)
        with open('reporte_sueldos.csv', 'a', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow(trabajador)
        trabajador.clear()

        

while contador == True:
    x = menu1()
    #generar los sueldos
    if x == 1:
        generar_sueldo()

    #clasificar sueldos
    if x == 2:
        print(" ")
    #ver estadisticas 
    if x == 3:
        print(" ")

    #reporte de sueldos
    if x == 4:
        reporte_de_sueldos()
    #SALIR
    elif x == 5:
        salir_programa()
