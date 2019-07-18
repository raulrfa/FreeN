#!/usr/bin/python
#-*- coding: utf-8 -*-

from enum import Enum

Animal = Enum('Animal','ANT BEE CAT DOG')

Idiomas = Enum('Idiomas', 'Espanol English Frances Portugues Aleman Italiano Ruso Chino')
SitiosF = Enum('Sitios','Workana  Freelancer Twago')
NivelSitio = Enum('Niveles','Inicial R1 R2 R3 R4 R5') 
AreasTrab = Enum('Areas Trabajo','Escritura Programación Traducción Diseño Enseñanza Administrativo Ingenieria' )
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
    
