from tkinter import *
from tkinter import ttk as tk
from tkintertable import TablesCanvas
from sqlite3 import *

class OfertasRealizadas(Frame):
    def __init__(self, raiz, bd, tabimp):
        self.raiz=raiz       
        self. bd = bd
        self.tabimp=tabimp
        self.fra = LabelFrame(self.raiz, bg='yellow', padx=5, pady =5, text ='Estadisticas Ofertas realizadas')
        self.fra.pack(side=LEFT, fill=Y)
     

    def muestradatos(self):
       data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
       'rec2': {'col1': 99.88, 'col2': 108.79, 'label': 'rec2'}
       } 
       table = TableCanvas(self.fra,data=data,width=100,height=40)
       table.show()

if __name__ == '__main__':
     raiz = Tk()
     b=OfertasRealizadas(raiz,'freebd.db','ofertasrealizadas')
     b.muestradatos()
     raiz.mainlop()
