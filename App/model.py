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


from DISClib.DataStructures.singlelinkedlist import newList
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import quicksort as sb
from DISClib.Algorithms.Sorting import mergesort as sc
from DISClib.Algorithms.Sorting import insertionsort as sd
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
    catalog['Productions'] = lt.newList(listtype) 

    return catalog
# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    lt.addLast(catalog['Artists'], artist)
    prodfilter = {'ConstituentID': artist['ConstituentID'], 'Artist': artist['DisplayName'], 'Artworks': lt.newList('ARRAY_LIST')}
    lt.addLast(catalog['Productions'], prodfilter)


def addArtwork(catalog, artwork,):
    artists = lt.iterator(catalog['Productions'])
    artistnum = artwork['ConstituentID'][1:-1].split(',')
    for men in artists:
        for artistn in artistnum:
            if artistn == men['ConstituentID']:
                lt.addLast(men['Artworks'], artwork)

    artists = lt.iterator(catalog['Artists'])

    #filtered = {'ArtistID': artwork['ConstituentID'], 'ObjectID': artwork['ObjectID'], 'Title': artwork['Title'], 'Date': artwork['Date'], 'Medium': artwork['Medium'], 'Classification': artwork['Classification'], 'Dimensions': artwork['Dimensions'], 'Weight': artwork['Weight (kg)'], 'CreditLine': artwork['CreditLine']}
    artists = lt.iterator(catalog['Artists'])
    constentIdArtwork = artwork['ConstituentID']
    Ids = constentIdArtwork.split(", ")
    Ids = LimpiarStringsId(Ids)
    nameArtist = None
    countryArtist = None
    for men in artists:
        constituentId = men['ConstituentID']
        for id in Ids:
            if id == (constituentId):
                    nameArtist = men['DisplayName']
                    countryArtist = men['Nationality']
                    
            
    artwork.update({'ArtistsNames': nameArtist,'Nationality':countryArtist})
    lt.addLast(catalog['Artworks'], artwork)

# Funciones para creacion de datos

def LimpiarStringsId(Array):
    arrayRespuesta = []
    ## Hay dos casos, uno en el que el array es solo un numero y el otro en el que es dos o mas
    if Array.__len__() == 1:
        filt1 = Array[0].replace("[","")
        filt2 = filt1.replace("]","")
        arrayRespuesta.append(filt2)
    else:
        filt1 = Array[0].replace("[","")
        Array[0] = filt1
        filt2 = Array[-1].replace("]","")
        Array[-1] = filt2
        arrayRespuesta = Array
    return arrayRespuesta


# Funciones de consulta

def getagerange(catalog, date1, date2):
    artists = lt.iterator(catalog['Artists'])
    cronartists = lt.newList("ARRAY_LIST")
    for men in artists:
        if (int(men['BeginDate']) >= int(date1) and int(men['BeginDate']) <= int(date2)):
            lt.addLast(cronartists, men)
    sa.sort(cronartists, compareages)
    return cronartists

def cronartwork(catalog, date1, date2):
    tamano = lt.size(catalog["Artworks"])
    sublist = lt.subList((catalog['Artworks']), 1, tamano)
    sublist = sublist.copy()
    c = lt.size(sublist) - 1
    while c > -1:
        element = lt.getElement(sublist, c)
        if element['DateAcquired'] < date1 or element['DateAcquired'] > date2:
            lt.deleteElement(sublist, c)
        sa.sort(sublist, cmpArtworkByDateAcquired)
        c = c-1
    return sublist

def getartwoksandtech(catalog, artist):
    prod = lt.iterator(catalog['Productions'])
    for element in prod:
        if element['Artist'] == artist:
            bruh = element
    sa.sort(bruh['Artworks'], comparetechniques)
    
    
    popularity = lt.newList("ARRAY_LIST")
    comparator = lt.iterator(bruh['Artworks'])
    art1 = None
    art2 = None
    n = 0
    tech_num = 0
    artlist = lt.newList("ARRAY_LIST")
    for artwork in comparator:
        
        art1 = artwork['Medium']
        if art1 != art2:
            tech_num = tech_num + 1
            if art2 != None:
                lt.addLast(popularity, dic)
            n = 1
            artlist = lt.newList("ARRAY_LIST")
            lt.addLast(artlist, artwork)
            dic = {"Medium": artwork['Medium'], 'Number': n, 'Artworks': artlist}
            art2 = art1
        else:
            n = n + 1
            art2 = art1
            lt.addLast(artlist, artwork)
            dic = {"Medium": artwork['Medium'], 'Number': n, 'Artworks': artlist}
    if art1 == None:
        tech_num = 0
    elif art1 == art2:
        lt.addLast(popularity, dic)
        
    sa.sort(popularity, comparetechniques2)

    return bruh, popularity, tech_num

def dimensionsprocessor(dimenciones):
    dimenciones = dimenciones.split('""')
    return dimenciones

def getcostfordepa(catalog, departament):
    indep = lt.newList('ARRAY_LIST')
    inold = lt.newList('ARRAY_LIST')
    dep = lt.iterator(catalog['Artworks'])
    t_cost = 0.0
    t_weight = 0.0
    for depo in dep:
        size = ''
        cost = 0
        if depo["Department"] == departament:
            
            if depo['Height (cm)'] != '' and depo['Width (cm)'] != '':
                size = float(depo['Height (cm)']) * float(depo['Width (cm)'])/10000

            if depo['Depth (cm)'] != '' and depo['Depth (cm)'] != '0':
                if depo['Diameter (cm)'] !='':
                    size = float(depo['Depth (cm)']) * (float(depo['Diameter (cm)']))/1000000
                elif (depo['Height (cm)'] != '' and depo['Height (cm)'] != '0') and (depo['Width (cm)'] != '0' and depo['Width (cm)'] != ''):
                     size = float(depo['Height (cm)']) * float(depo['Width (cm)']) * float(depo['Depth (cm)'])/1000000 
            
            if depo['Circumference (cm)'] != '' and depo['Circumference (cm)'] != '0':
                size = ((float(depo['Circumference (cm)'])/2)**2)/3.14
                if depo['Diameter (cm)'] !='' and depo['Diameter (cm)'] !='0':
                        size = float(depo['Circumference (cm)']) * float(depo['Diameter (cm)'])/10000 
                        if depo['Length (cm)'] != '' and depo['Length (cm)'] != '0':
                            size = float(depo['Circumference (cm)']) * float(depo['Diameter (cm)']) * float(depo['Length (cm)'])/1000000
            if size == '' or size == 0:
                cost = 48.00
            elif (depo['Weight (kg)']) != '' and float(depo['Weight (kg)']) > size*72:
                size = float(depo['Weight (kg)'])

            
            if cost != 48.00:
                cost = size*72.00

            lt.addLast(indep, {'dep': depo, 'price': cost})
            if depo['Date'] != '' and depo['Date'] != '0':
                lt.addLast(inold, {'dep': depo, 'Date': depo['Date']})
            t_cost = t_cost + cost
            if depo['Weight (kg)'] != '':
                t_weight = t_weight + float(depo['Weight (kg)'])
        sa.sort(indep, comparecost)
        sa.sort(inold, compareage)
    return indep, inold, t_weight, t_cost

def organizeCountry(catalog):
    Artworks = catalog["Artworks"]
    iterator = lt.iterator(Artworks)
    ## Primero toca organizar las obras en listas por sus paises
    Paises = []
    ObrasPorPais = []
    for artwork in iterator:
        tamañoPaises = Paises.__len__()
        ## Caso incial de los arrays
        if tamañoPaises == 0:
            Paises.append(artwork["Nationality"])
            ObrasPorPais.append([artwork])
        else:
            ## Mirar en todo los paises a ver si hay un lugar donde poner esta obra
            for index in range(0,tamañoPaises):
                ## Caso en el que encuentra el pais donde deberia poner la obra
                if str(artwork["Nationality"]) == str(Paises[index]):
                    ## La obra se coloca en el index actual de obras por pais en la lista de ese pais
                    ObrasPorPais[index].append(artwork)
                    break
                ## Si ya llego al final de la lista y no encontro donde poner la artowrk creele una
                # nueva categoria y guardela ahi    
                elif index == tamañoPaises-1 and str(artwork["Nationality"]) != str(Paises[index]):
                    Paises.append(artwork["Nationality"])
                    ObrasPorPais.append([artwork])


    ## Ahora tenemos que organizar en terminos de que tan grande sea cada categoria
    numObrasPorPais = []
    ## Llenamos un nuevo array con los tamaños de los arrays
    for iteracion in ObrasPorPais:
        size = iteracion.__len__()
        numObrasPorPais.append(size)

    ## Organizamos el array teniendo en cuenta sus size mayor a menor
    nombresOrdenados = []
    ObrasOrdenadas = []
    numObrasOrdenadas = []
    iterador = 0
    sentinela = numObrasPorPais.__len__()
    while sentinela > 0:
        max = 0
        for i in range(0, numObrasPorPais.__len__()):
            pais = numObrasPorPais[i]
            if pais >= max:
                max = pais
                iterador = i
        nombresOrdenados.append(Paises[iterador])
        ObrasOrdenadas.append(ObrasPorPais[iterador])
        numObrasOrdenadas.append(max)
        numObrasPorPais.pop(iterador)
        Paises.pop(iterador)
        ObrasPorPais.pop(iterador)
        sentinela = numObrasPorPais.__len__()

    return nombresOrdenados,ObrasOrdenadas,numObrasOrdenadas

# Funciones utilizadas para comparar elementos dentro de una lista

def compareages(artist1, artist2):
     return ((artist1['BeginDate'] < artist2['BeginDate']))

def cmpArtworkByDateAcquired(artwork1, artwork2):
    return (artwork1['DateAcquired'] < artwork2['DateAcquired'])

def comparetechniques2(art1, art2):
    return (art1['Number'] > art2['Number'])

def comparetechniques(art1, art2):
    return (art1['Medium'] < art2['Medium'])

def comparecost(art1, art2):
    return (art1['price'] > art2['price'])

def compareage(art1, art2):
    return (art1['Date'] < art2['Date'])


# Funciones ordenamiento