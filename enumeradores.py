#!/usr/bin/python
#-*- coding: utf-8 -*-

from enum import Enum
import sqlite3

Animal = Enum('Animal','ANT BEE CAT DOG')


Idiomas = Enum('Idiomas', 'Español English Frances Portugues Aleman Italiano Ruso Chino')
SitiosF = Enum('Sitios','Workana  Freelancer Twago')
NivelSitio = Enum('Niveles','Inicial R1 R2 R3 R4 R5') 
AreasTrab = Enum('Areas_Trabajo','Escritura Programación Traducción Diseño Enseñanza Administrativo Ingenieria' )
Habilidades = Enum('Habilidades', 'Delphi C C++ Python Django Flask HTML CSS JavaScript Autocad Fortran')


PagoXMembresia = []
OfertasxMembresia = []
PeriodoOfertasXMembresia = Enum('PeriodoOferta','NoDefinido Semanal Mensual Ilimatada')

class TipoProyecto(Enum):
    Horario = 1
    Plazo = 2
    Concurso = 3
    Venta = 4
    TrabajosSitu =5
    BusquedadAnonima = 6

def llenatabla(enum):
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    query="CREATE TABLE IF NOT EXISTS {} ({} INTEGER PRIMARY KEY, {} TEXT)".format(enum.__name__,'id'+enum.__name__,'nom'+enum.__name__)
    print(query)
    curs.execute(query)
    db.commit()

    for e in enum:
        print(enum.__name__,'id'+enum.__name__,'nom'+enum.__name__,e.value,e.name)
        #1 query="INSERT INTO 'Habilidades' VALUES(?,?)"
        #query="INSERT INTO  VALUES(?,?)"(enum.__name__,e.value,e.name)
        #print(query)
        curs.execute("INSERT INTO {} VALUES(?,?)".format(enum.__name__),(e.value,e.name))
        #curs.execute(query)
        db.commit() 
    db.close
    
def verenum(enum):
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    curs.execute("SELECT * FROM {}".format(enum.__name__))
    a = curs.fetchall()
    print(a)     
    db.close
    return a

def copyvaluesdict(dict):
        lista=[]
        listaerror =[]
        for sel in dict.values():
            try: lista.append(sel.get())
            except:
                print('lerror: ',listaerror)
                listaerror.append(type(sel))
        print(lista)
        # id=updatesitio(lista)
        #if id!=lista[0]: # no hay problemas se retorno el mismo rowguid
            #messagebox.showerror('Error','No se pudo salvar el sitio')
        return lista

if __name__ == '__main__':
    
    print(type(Animal.BEE.name), type(Animal.BEE.value))
    llenatabla(Habilidades)
    verenum(Habilidades)
    