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
from prettytable import PrettyTable
import time

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Req1 - Listar Cronologicamente Los Artistas")
    print('3- Req2 - Listar Cronologicamente las adquiciciones')
    print('4- Req3 - Listar las tecnicas de las obras de un artista')
    print('5- Req4 - Clasificar las obras por nacionaliad de creador')
    print('6- Req5 - Costo de transporte de obras de un departamento')
    print('0- Salir del programa')


catalog = None
sorttype = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

        catalog = (controller.InitCatalog("ARRAY_LIST"))
        controller.loadData(catalog)
        print("Número de Artistas registrados: " + str(lt.size(catalog['Artists'])))
        print("Número de obras de arte registradas: " + str(lt.size(catalog['Artworks'])))
    
    elif int(inputs[0]) == 2:
        ## LISTAR CRONOLOGICAMENTE ARTISTAS
        start = time.time()

        Anoinicial = input("Indique el año inicial: ")
        Anofinal = input("Indique el año inicial: ")
        print("=============== Req No. 1 Inputs ===============")
        print("Artist born between " + str(Anoinicial) + " and " + str(Anofinal))
        print('')
        print('=============== Req No. 1 Answer ===============')
        lista = controller.getcronologicalartists(catalog, Anoinicial, Anofinal)
        print('There are ' + str(lt.size(lista)) + ' artist born between ' + str(Anoinicial) + " and " + str(Anofinal))
        print('')
        print("The first and last 3 artists in range are...")
        contador1 = 1
        contador2 = 0

        itable = PrettyTable(['ConstituentID', 'DisplayName', 'BeginDate', 'Nationality', 'Gender', 'ArtistBio', 'Wiki QID', 'ULAN'])
        while contador1 < 4:
            elemento = lt.getElement(lista, contador1)
            itable.add_row([elemento['ConstituentID'], elemento['DisplayName'], elemento['BeginDate'], elemento['Nationality'], elemento['Gender'], elemento['ArtistBio'], elemento['Wiki QID'], elemento['ULAN']])
            contador1 = contador1 + 1
        while contador2 > -3:
            elemento = lt.getElement(lista, contador2)
            itable.add_row([elemento['ConstituentID'], elemento['DisplayName'], elemento['BeginDate'], elemento['Nationality'], elemento['Gender'], elemento['ArtistBio'], elemento['Wiki QID'], elemento['ULAN']])
            contador2 = contador2 - 1
        print(itable)
        end = time.time()
        print(end - start)


    elif int(inputs[0]) == 3:
        ## LISTAR CRONOLOGICAMENTE OBRAS EN UN RANGO
        start = time.time()
        Anoinicial = str(input("Indique la fecha inicial en formato AAAA-MM-DD: "))
        Anofinal = str(input("Indique la fecha final en formato AAAA-MM-DD: "))
        lista = (controller.cronartworks(catalog, Anoinicial, Anofinal))
        print('')
        print("=============== Req No. 2 Inputs ===============")
        print("Artworks acquired between " + str(Anoinicial) + " and " + str(Anofinal))
        print('')
        print('=============== Req No. 2 Answer ===============')
        print('The MoMa acquired ' + str(lt.size(lista)) + ' unique pieces bewteen' + str(Anoinicial) + " and " + str(Anofinal))
        print("The first and last 3 artworks in range are...") 

        itable = PrettyTable(["ObjectID", "Title", "ArtistsNames", "Medium", "Dimensions", "Date", "DateAcquired", "URL"])

        contador1 = 1
        contador2 = 0

        while contador1 < 4:
            elemento = lt.getElement(lista, contador1)
            itable.add_row([elemento['ObjectID'], elemento['Title'], elemento['ArtistsNames'], elemento['Medium'], elemento['Dimensions'], elemento['Date'], elemento['DateAcquired'], elemento['URL']])
            contador1 = contador1 + 1
        while contador2 > -3:
            elemento = lt.getElement(lista, contador2)
            itable.add_row([elemento['ObjectID'], elemento['Title'], elemento['ArtistsNames'], elemento['Medium'], elemento['Dimensions'], elemento['Date'], elemento['DateAcquired'], elemento['URL']])
            contador2 = contador2 - 1
        print(itable)
        end = time.time()
        print(end - start)
        #print(table)
    elif int(inputs[0]) == 4:
        start = time.time()
        ## Listar las tecnicas de las obras de un artista
        artist = input('Introduzca el nombre del Artista: ')
        result = controller.getartwoksandtech(catalog, artist)
        print("=============== Req No. 3 Inputs ===============")
        print('Examine the work of the artist named: ' + artist)
        print('')
        print('=============== Req No. 3 Answer ===============')
        print(artist + ' with MoMA ID ' + str(result[0]['ConstituentID']) + ' has ' + str(lt.size(result[0]['Artworks'])) + ' in his/her name at the musem.')
        print('There are ' + str(result[2]) + ' different mediums/techniques in his/her working')

        

        #print = lt.getElement(result[0]['Artworks']['elements'], 1)\
        mtable = PrettyTable(['MediumName', 'Count'])
        for num in range(1, lt.size(result[1])):
            m1 = lt.getElement(result[1], num)
            mtable.add_row([m1['Medium'], m1['Number']])
            if num == 5:
                break
        medium = lt.getElement(result[1], 1)
        medium2 = medium['Medium']
        print('His/Her most used Medium/Technique is: ' + str(medium2) + ' with ' + str(medium['Number']) + ' pieces.')
        print(mtable)
        
        ttable = PrettyTable(['ObjectID', 'Title', 'Medium', 'Dimensions', 'DateAcquired', 'Department', 'Classification', 'URL'])
        
        contador = 0
        for art in range(1, lt.size(medium['Artworks'])+1):
            m1a =lt.getElement(medium['Artworks'], art)
            if contador == 4:
                break
            ttable.add_row([m1a['ObjectID'], m1a['Title'], m1a['Medium'], m1a['Dimensions'], m1a['DateAcquired'], m1a['Department'], m1a['Classification'], m1a['URL']])
            contador = contador + 1
        print('')
        print('His/Her most used Medium/Techniques is: ' + medium2 + ' with ' + str(contador) + ' pieces.')
        print('A sample of ' + str(contador) + ' ' + medium2 + ' from the collection are:')
        print(ttable)
        
        end = time.time()
        print(end - start)
            

    elif int(inputs[0]) == 5:
        print("organizando obras por nacionalidad...")
        Paises,ObrasPorPais,numPorPais = controller.organizeCountry(catalog)
        print(Paises)
        print(numPorPais)

        table = PrettyTable(["Pais","Obras"])
        
        for i in range (0,10):
            table.add_row([Paises[i],numPorPais[i]])
        print(table)


    elif int(inputs[0]) == 6:
        start = time.time()
        dep = input('Introduzca el departamento que desea explorar: ')
        result = controller.getcostfordep(catalog, dep)
        print("=============== Req No. 5 Inputs ===============")
        print('Estimate the cost to transport all artifacts in ' + dep + ' Departament')
        print('')
        print('=============== Req No. 5 Answer ===============')
        print('The MOMA is going to transport ' + str(lt.size(result[0])) + ' from the ' + dep)
        print('Estimated cargo weight (kg): ' + str((result[2])))
        print('Estimated cargo cost (USD): ' + str((round(result[3], 3))))
        print('')
        prim1 = lt.getElement(result[0], 1)
        prim2 = lt.getElement(result[0], 2)
        prim3 = lt.getElement(result[0], 3)
        prim4 = lt.getElement(result[0], 4)
        prim5 = lt.getElement(result[0], 5)
        prim1a = prim1['dep']
        prim2a = prim2['dep']
        prim3a = prim3['dep']
        prim4a = prim4['dep']
        prim5a = prim5['dep']
        #print('ObjectID: ' + prim1['ObjectID'] + ', Title:' + prim2['Title'] + ', ArtistsNames' + prim1['ConsituentID'] + ', Medium' + prim1['Medium'] + ', Date' + prim1['Date'] + ', Dimensions: ' + prim1['Dimensions'] + ', Classification:' + prim1['Classification'] + ', TransCost (USD):' + (lt.getElement(result[0], 1)) + ', URL' + )
        prim1c = lt.getElement(result[1], 1)
        prim2c = lt.getElement(result[1], 2)
        prim3c = lt.getElement(result[1], 3)
        prim4c = lt.getElement(result[1], 4)
        prim5c = lt.getElement(result[1], 5)
        prim1b = prim1c['dep']
        prim2b = prim2c['dep']
        prim3b = prim3c['dep']
        prim4b = prim4c['dep']
        prim5b = prim5c['dep']
        print('The TOP 5 most expensive items to transport are:')
        table = PrettyTable(["ObjectID", "Title", "ArtistsNames", "Medium", "Date", "Dimensions", "Classification", "Transcost (USD)", "URL"])
        table.add_row([str(prim1a["ObjectID"]), str(prim1a["Title"]), (prim1a["ArtistsNames"]['elements']), str(prim1a["Medium"]), str(prim1a["Date"]), str(prim1a["Dimensions"]), str(prim1a["Classification"]), str(prim1['price']), str(prim1a["URL"])])
        table.add_row([str(prim2a["ObjectID"]), str(prim2a["Title"]), (prim2a["ArtistsNames"]['elements']), str(prim2a["Medium"]), str(prim2a["Date"]), str(prim2a["Dimensions"]), str(prim2a["Classification"]), str(prim2['price']), str(prim2a["URL"])])
        table.add_row([str(prim3a["ObjectID"]), str(prim3a["Title"]), (prim3a["ArtistsNames"]['elements']), str(prim3a["Medium"]), str(prim3a["Date"]), str(prim3a["Dimensions"]), str(prim3a["Classification"]), str(prim3['price']), str(prim3a["URL"])])
        table.add_row([str(prim4a["ObjectID"]), str(prim4a["Title"]), (prim4a["ArtistsNames"]['elements']), str(prim4a["Medium"]), str(prim4a["Date"]), str(prim4a["Dimensions"]), str(prim4a["Classification"]), str(prim4['price']), str(prim4a["URL"])])
        table.add_row([str(prim5a["ObjectID"]), str(prim5a["Title"]), (prim5a["ArtistsNames"]['elements']), str(prim5a["Medium"]), str(prim5a["Date"]), str(prim5a["Dimensions"]), str(prim5a["Classification"]), str(prim5['price']), str(prim5a["URL"])])
        print(table)

        print('')

        print('The TOP 5 most oldests items to transport are:')
        table2 = PrettyTable(["ObjectID", "Title", "ArtistsNames", "Medium", "Date", "Dimensions", "Classification", "Transcost (USD)", "URL"])
        table2.add_row([str(prim1b["ObjectID"]), str(prim1b["Title"]), (prim1b["ArtistsNames"]['elements']), str(prim1b["Medium"]), str(prim1b["Date"]), str(prim1b["Dimensions"]), str(prim1b["Classification"]), str(prim1c['Date']), str(prim1b["URL"])])
        table2.add_row([str(prim2b["ObjectID"]), str(prim2b["Title"]), (prim2b["ArtistsNames"]['elements']), str(prim2b["Medium"]), str(prim2b["Date"]), str(prim2b["Dimensions"]), str(prim2b["Classification"]), str(prim2c['Date']), str(prim2b["URL"])])
        table2.add_row([str(prim3b["ObjectID"]), str(prim3b["Title"]), (prim3b["ArtistsNames"]['elements']), str(prim3b["Medium"]), str(prim3b["Date"]), str(prim3b["Dimensions"]), str(prim3b["Classification"]), str(prim3c['Date']), str(prim3b["URL"])])
        table2.add_row([str(prim4b["ObjectID"]), str(prim4b["Title"]), (prim4b["ArtistsNames"]['elements']), str(prim4b["Medium"]), str(prim4b["Date"]), str(prim4b["Dimensions"]), str(prim4b["Classification"]), str(prim4c['Date']), str(prim4b["URL"])])
        table2.add_row([str(prim5b["ObjectID"]), str(prim5b["Title"]), (prim5b["ArtistsNames"]['elements']), str(prim5b["Medium"]), str(prim5b["Date"]), str(prim5b["Dimensions"]), str(prim5b["Classification"]), str(prim5c['Date']), str(prim5b["URL"])])
        print(table2)

        print(prim3b["ArtistsNames"]['elements'])

        end = time.time()
        print(end - start)

    else:
        sys.exit(0)
sys.exit(0)
