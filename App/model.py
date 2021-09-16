"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import quicksort as sb
from DISClib.Algorithms.Sorting import mergesort as sc
from DISClib.Algorithms.Sorting import insertionsort as sd
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newcatalog(listtype):
    catalog = { 'Artists': None,
                'Artworks': None}
    catalog['Artists'] = lt.newList(listtype) #, comparefunction = cmp_artist
    catalog['Artworks'] = lt.newList(listtype) #, comparefunction =  cmp_artworks

    return catalog
# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    #filtered = {'ArtistID': artist['ConstituentID'], 'Artist': artist['DisplayName'], 'Nationality': artist['Nationality'], 'Birthdate': int(artist['BeginDate'])}
    lt.addLast(catalog['Artists'], artist)

def addArtwork(catalog, artwork):
    #filtered = {'ArtistID': artwork['ConstituentID'], 'ObjectID': artwork['ObjectID'], 'Title': artwork['Title'], 'Date': artwork['Date'], 'Medium': artwork['Medium'], 'Classification': artwork['Classification'], 'Dimensions': artwork['Dimensions'], 'Weight': artwork['Weight (kg)'], 'CreditLine': artwork['CreditLine']}
    lt.addLast(catalog['Artworks'], artwork)


# Funciones para creacion de datos


# Funciones de consulta

def getagerange(catalog, date1, date2):
    artists = catalog["Artists"]
    cronartists = lt.newList()
    for men in range(date1, date2):
        if ((men['Birthdate'] >= date1) and (men['Birthdate'] <= date2)):
            trueartist = lt.getElement(artists, men)
            lt.addLast(cronartists, trueartist)
    return cronartists


def cronartwork(catalog, number, date1, date2, sorttype):
    if lt.size(catalog['Artworks']) >= number:
        sublist = lt.subList((catalog['Artworks']), 1, number)
        sublist = sublist.copy()
        c = lt.size(sublist) - 1
        while c > -1:
            element = lt.getElement(sublist, c)

            if element['DateAcquired'] < date1 or element['DateAcquired'] > date2:
                lt.deleteElement(sublist, c)

            c = c - 1
        if sorttype == 'Insertion':
            start_time = time.process_time()
            sd.sort(sublist, cmpArtworkByDateAcquired)
            stop_time = time.process_time()

        elif sorttype == 'Merge':
            start_time = time.process_time()
            sc.sort(sublist, cmpArtworkByDateAcquired)
            stop_time = time.process_time()

        elif sorttype == 'Quick Sorts':
            start_time = time.process_time()
            sb.sort(sublist, cmpArtworkByDateAcquired)
            stop_time = time.process_time()

        elif sorttype == 'Shell':
            start_time = time.process_time()
            sa.sort(sublist, cmpArtworkByDateAcquired)
            stop_time = time.process_time()

        else:
            start_time = time.process_time()
            sa.sort(sublist, cmpArtworkByDateAcquired)
            stop_time = time.process_time()

    else:
        return 'N/A'
    elapsed_time_mseg = str((stop_time - start_time)*1000)
    return sublist, elapsed_time_mseg

# Funciones utilizadas para comparar elementos dentro de una lista

def compareages(artist1, artist2):
     return (float(artist1['Birthdate']) > float(artist2['Birthdate']))

def cmpArtworkByDateAcquired(artwork1, artwork2):
    return (artwork1['DateAcquired'] < artwork2['DateAcquired'])



# Funciones de ordenamiento

def cronfilter(catalog):
    sa.sort(catalog['Artistas'], compareages)