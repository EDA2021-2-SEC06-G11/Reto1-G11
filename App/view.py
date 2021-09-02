"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from controller import loadData
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Artistas en orden cronológico")
    print('3- Adquisiciones en orden cronológico')
    print('4- Obras de arte de artista por técnica')
    print('5- Obras de arte por nacionalidad de artista')
    print('6- Transportar obras de un departamento')
    print('0- Proponer una nueva exposición en el museo')


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = (controller.InitCatalog())
        controller.loadData(catalog)
        print("Número de Arttistas registrados: " + str(lt.size(catalog['Artists'])))
        print("Número de obras de arte registradas: " + str(lt.size(catalog['Artworks'])))
        print("")
        print("Primeros 3 artistas: ") 
        print(" ")
        print(str(catalog['Artists']['elements'][:3]))
        print("")
        print("Ultimos 3 artistas: ")
        print(" ")
        print(str(catalog['Artists']['elements'][-3:]))
        print("")
        print("Primeras 3 obras de arte: ")
        print("")
        print(str(catalog['Artworks']['elements'][:3]))
        print("")
        print("Ultimas 3 obras de arte: " )
        print("")
        print(str(catalog['Artworks']['elements'][-3:]))
    elif int(inputs[0]) == 2:
        anioInicial = input("Año Inicial de busqueda:")
        anioFinal = input("Año Final de busqueda:")

    elif int(inputs[0]) == 3:
        fechaInicial = input("Fecha inicial de busqueda (AAAA-MM-DD):")
        fechaFinal = input("Fecha final de busqueda (AAAA-MM-DD):")

    elif int(inputs[0]) == 4:
        nombre = input("Nombre del Artista a buscar:")

    elif int(inputs[0]) == 5:
        obra = input("Las obras del Museo:")

    elif int(inputs[0]) == 6:
        departamento = input("Departamento de obras que se quiere conocer el precio estimado de transporte:")

    elif int(inputs[0]) == 7:
        anioInicial = input("Año inicial de las obras:")
        anioFinal = input("Año final de las obras:")
        areaDisponible = input("Area disponible para la exposicion (m^2):")

    else:
        sys.exit(0)
sys.exit(0)