from tkinter import *
from tkinter import messagebox
from enumeradores import Idiomas
from sqlite3 import *
from sitio import Sitio

class Usuario():
    cantusuario=0
    """"Clase para definir los usurios de los sitios de frrelancers"""
    def __init__(self, raiz,nombre,alias,email,skype,web,webpropia,linkedin):
        #super(Usuario,self).__init__()
        #self.configure(text='Edicion de Sitios',bg='gray')
        self.master=raiz
        self.nombre=nombre
        self.alias = alias
        self.skype= skype
        self.email=email
        self.webpropia=web
        self.linkedin=linkedin
        cantusuario+=1
        """"
        self.pack()
        self.frbut=tk.Frame(self,bg='yellow')
        self.pack(side=tk.LEFT)
        self.frbutidi =tk.LabelFrame(self,bg='blue',text='Idiomas')
        self.frbutidi.pack(side=tk.LEFT,fill=tk.Y)
        self.frbutip =tk.LabelFrame(self,bg='lightyellow',text="Tipos")
        self.frbutip.pack(side=tk.LEFT,fill=tk.Y)
        self.fredit= tk.Frame(self,bg="white")
        self.fredit.pack(side=tk.LEFT, fill=tk.Y, expand=1)
        self.freditbut= tk.Frame(self.fredit,bg='gray')
        #self.freditbut.pack() """

class UsuarioSitio(Usuario,Sitio):
    fechainscripcion = 0


    def __init__(self, alias, sitio, fechainscripcion,nivel,costo,periodo,suscripcion ):
        super(Usuario,self).__init__()
        self.fechainscripcion= fechainscripcion
        self.nivel =nivel                           # no depende pago
        self.suscripcion = suscripcion              # depende de pago
        self.costo =costo
        self.periodo = periodo
        self.proyectosperiodo

class PeriodoSitioUsuario (UsurioSitio, inicio,fin):
    """ Clase que lleva la cantidad de ofertas realizadas en un periodo clasico del sitio"""
    cantproyectos = 0
    cantperiodos= 0

    def __init__(self, alias, sitio, inacripcion, proyectoshabperiodo, ):
        self.proyectoshabperiodo = 0
        self.cantofertasperiodo = 0
        self.ofertasrealperiodo = 0
        self.repuestasperiodo =0
        self.trabajosperiodo =0


if __name__ == '__main__':
    raiz = tk.Tk()
    b=Sitio(raiz,'',[],[],3)
    #b.muestra_checkbut()
    raiz.mainloop()    

