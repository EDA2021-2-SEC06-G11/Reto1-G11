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
#from prettytable import PrettyTable

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
sorttype = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipolista = input('Elija el tipo de lista, sea ya ARRAY_LIST o LINKED_LIST:')
        print("Cargando información de los archivos ....")
        catalog = (controller.InitCatalog(tipolista))
        controller.loadData(catalog)
        print("Número de Artistas registrados: " + str(lt.size(catalog['Artists'])))
        print("Número de obras de arte registradas: " + str(lt.size(catalog['Artworks'])))
        print("Primeros 3 artistas: " + str(catalog['Artists']['elements'][:3]))
        print("Ultimos 3 artistas: " + str(catalog['Artists']['elements'][-3:]))
        print("Primeras 3 obras de arte: " + str(catalog['Artworks']['elements'][:3]))
        print("Ultimas 3 obras de arte: " + str(catalog['Artworks']['elements'][-3:]))
    
    elif int(inputs[0]) == 2:
        sorttype = input("ingrese el tipo de sort que desea: Insertion, Shell, Merge o Quick Sorts: ")

    elif int(inputs[0]) == 3:
        Anoinicial = str(input("Indique la fecha inicial en formato AAAA-MM-DD: "))
        Anofinal = str(input("Indique la fecha final en formato AAAA-MM-DD: "))
        sublistnum = int(input("Indique el tamaño de la lista: "))
        lista = (controller.cronartworks(catalog, sublistnum, Anoinicial, Anofinal, sorttype))
        listah = lista[0]['elements']
        lista2 = lista[0]
        tiempo = lista[1]
        print('')
        print("=============== Req No. 2 Inputs ===============")
        print("Artworks acquired between " + str(Anoinicial) + " and " + str(Anofinal))
        print('')
        print('=============== Req No. 2 Answer ===============')
        print('The MoMa acquired ' + str(lt.size(lista2)) + ' unique pieces bewteen' + str(Anoinicial) + " and " + str(Anofinal))
        print("The first and last 3 artworks in range are...")

        #table = PrettyTable(["ObjectID", "Title", "ArtistsNames", "Medium", "Dimensions", "Date", "DateAcquired", "URL"])

        #table.add__row([listah[0]["ObjectID"], listah[0]["Title"], listah[0]["ArtistsNames"], listah[0]["Medium"], listah[0]["Dimensions"], listah[0]["Date"], listah[0]["DateAcquired"], listah[0]["URL"]])
        #table.add__row([listah[1]["ObjectID"], listah[1]["Title"], listah[1]["ArtistsNames"], listah[1]["Medium"], listah[1]["Dimensions"], listah[1]["Date"], listah[1]["DateAcquired"], listah[1]["URL"]])
        #table.add__row([listah[2]["ObjectID"], listah[2]["Title"], listah[2]["ArtistsNames"], listah[2]["Medium"], listah[2]["Dimensions"], listah[2]["Date"], listah[2]["DateAcquired"], listah[2]["URL"]])
        #table.add__row([listah[-1]["ObjectID"], listah[-1]["Title"], listah[-1]["ArtistsNames"], listah[-1]["Medium"], listah[-1]["Dimensions"], listah[-1]["Date"], listah[-1]["DateAcquired"], listah[-2]["URL"]])
        #table.add__row([listah[-2]["ObjectID"], listah[-2]["Title"], listah[-2]["ArtistsNames"], listah[-2]["Medium"], listah[-2]["Dimensions"], listah[-2]["Date"], listah[-2]["DateAcquired"], listah[-2]["URL"]])
        #table.add__row([listah[-3]["ObjectID"], listah[-3]["Title"], listah[-3]["ArtistsNames"], listah[-3]["Medium"], listah[-3]["Dimensions"], listah[-3]["Date"], listah[-3]["DateAcquired"], listah[-3]["URL"]])
        
        #Se corrompio la libreria de Prettytable, en el reto se arreglara este inconveniente, al no ser vital para la medicion de tiempo de los sorts. Gracias por su comprension. :)
        
        
        print(listah[:3])
        print(listah[-3:])
        print('')
        print('El tiempo gastado en organizar los datos es: ' + tiempo + ' milisegundos')

    else:
        sys.exit(0)
sys.exit(0)
