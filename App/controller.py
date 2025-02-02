﻿"""
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
 """

import config as cf
import model
import csv

from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def InitCatalog(tipolista):
    catalog = model.newcatalog(tipolista)
    return catalog


# Funciones para la carga de datos
def loadData(catalog):
    loadArtists(catalog)
    loadArtwork(catalog)

def loadArtists(catalog):
    artistfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtwork(catalog):
    artworkfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworkfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)



# Funciones de ordenamiento




# Funciones de consulta sobre el catálogo

def getcronologicalartists(catalog, date1, date2):
    return model.getagerange(catalog, date1, date2)

def cronartworks(catalog, date1, date2,):
    return model.cronartwork(catalog, date1, date2)

def getagerange(catalog, date1, date2):
    artists = catalog["Artists"]
    cronartists = lt.newList()
    for men in artists:
        print(men)
        mena = men['elements']
        if ((men['Birthdate'] >= date1) and (men['Birthdate'] <= date2)):
            trueartist = lt.getElement(artists, mena)
            lt.addLast(cronartists, trueartist)
    return cronartists

def getartwoksandtech(catalog, artist):
    return model.getartwoksandtech(catalog, artist)

def getcostfordep(catalog, departament):
    return model.getcostfordepa(catalog, departament)


def organizeCountry(catalog):
    return model.organizeCountry(catalog)