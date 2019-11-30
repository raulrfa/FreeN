import tkinter as tk
from tkinter import ttk as ttk
from tkinter import messagebox
#from tkintertable.Tables import TableCanvas
from tkintertable import TableCanvas, TableModel
import sqlite3 

import enumeradores
import LabelInput as li
from sitio_backend import salvarprelproyectodb, editprelproyectosdb
import datetime

class Proyecto(tk.Frame):
    """Clase para definir los proyectos"""
    def __init__(self, raiz,refsitio,nomsitio,idsitio):
        super(Proyecto,self).__init__()
        self.nomsitio =nomsitio
        self.idsitio = idsitio
        self.refsitio=refsitio
        self.frediproy=raiz
        self.frediprelproy=raiz
        self.deatacched={}

        self.prelproy={'idprelproyecto':tk.IntVar(),'idsitio':tk.IntVar(),'fechavisita':tk.StringVar(),'url':tk.StringVar(),
        'copy':tk.StringVar(), 'copyofer':tk.StringVar()}

        self.prelproyval={'idprelproyecto':-1,'idsitio':0,'fechavisita':'','url':'',
        'copy':'', 'copyofer':''}


        # se incluye none coo un valor de id nuevo para un proypreliminar
      
        if self.prelproyval['idprelproyecto']==None:
            print( 'nONE')



        self.prelproyv={}


        self.proyecto={
            'idProyecto'        :  tk.IntVar(),
            'idsitio'           :  tk.IntVar(),
            'nomproyecto'       :  tk.StringVar(),
            'descripcion'       :  tk.StringVar(),
            'moneda'            :  tk.StringVar(),
            'nomproponente'     :  tk.StringVar(),
            'paisproponente'    :  tk.StringVar(),
            'proyectospagados'  :  tk.IntVar(),
            'numhabilidades'    :  tk.IntVar(),
            'numpreguntas'      :  tk.IntVar(),
            'ofertamax'         :  tk.IntVar(),
            'ofertamin'         :  tk.IntVar(),
            'ofertapromedio'    :  tk.IntVar(),
            'cantofertantes'    :  tk.IntVar(),
            'requisitosesp'     :  tk.StringVar(),
            'valormax'          :  tk.IntVar(),
            'valormin'          :  tk.IntVar(),
            'creacion'          :  tk.StringVar()}

        """ 
        for value in self.sitio:
            if type(self.sitio.values)==type(tk.StringVar()):
                self.sitio.values=StringVar.set('')
            else:
                self.sitio.values=tk.IntVar.set(0)"""
        #print (list(self.sitio.keys()))
        #print(list(self.sitio.values()))

    def newprelproy(self):
        self.prelproy['idprelproyecto'].set(-1)
        self.prelproy['idsitio'].set(self.idsitio)
        self.prelproy['fechavisita'].set(str(datetime.datetime.now())) 
        textaux= 'Proyecto de {} registrado el dia {}'.format(self.nomsitio,self.prelproy['fechavisita'] )
        tk.Label(self.frediprelproy,text=textaux).grid(row=2,column=1)
        self.prelproyv['url']=li.LabelInput(self.frediprelproy,'Url', input_var=self.prelproy['url'])
        self.prelproyv['url'].grid(row=4, column=1)
        self.prelproyv['copy']=li.LabelInput(self.frediprelproy,'Copia del Proyecto', input_class=tk.Text,input_args={"height": 10,"width": 60})
        self.prelproyv['copy'].grid(row=6,column=1)
        self.prelproyv['copyofer']=li.LabelInput(self.frediprelproy,'Copia de la Oferta', input_class=tk.Text,input_args={"height": 10,"width": 60})
        self.prelproyv['copyofer'].grid(row=18,column=1)
        self.prelproyv['copy'].set(self.prelproy['copyofer'].get())
        self.prelproyv['copyofer'].set('END',self.prelproy['copy'].get())

    def editprelproy(self):
        #se incluye en este procedimeinto ls varibles derivadas o los etrey ls demas entran como variables de contro de tkinter
        self.prelproy['idsitio'].set(self.idsitio.get())
        self.prelproy['fechavisita'].set(str(datetime.datetime.now())) 
        self.prelproyv['copy'].set(self.prelproy['copy'])
        self.prelproyv['copyofer'].set(self.prelproy['copyofer'])
        
    
    def salvarprelproy(self,event):
        self.prelproy['copy'].set(self.prelproyv['copy'].get())
        self.prelproy['copyofer'].set(self.prelproyv['copyofer'].get())
        lista=enumeradores.copyvaluesdict(self.prelproy)
        self.prelproy['idsitio'].set(salvarprelproyectodb(lista))
        
    """
    def muestra_proy(self,event):
       i=0
       if isinstance(event,integer):
           k=event
       else:
           k=20

       i+=1
       li.LabelInput(self.frediproy,'Nombre del Proyecto', input_var=self.proyecto['nomproyecto']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Descripcion', input_class=ttk.Entry,input_var=self.proyecto['descripcion']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,"País",input_class=ttk.Combobox, input_var=self.proyecto['paisproponente'],
       input_args={"values": ["Argentina", "Australia", "USA","Francia", "Alemania"]}).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Moneda', input_var=self.proyecto['moneda']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,"Nombre Proponente", input_var=self.proyecto['nomproponente']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Proyectos pagados', input_var=self.proyecto['proyectospagados']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Numero Habilidades', input_var=self.proyecto['numhabilidades']).grid(row=i % k,column=(i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Numero Preguntas', input_var=self.proyecto['numpreguntas']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Valor Mínimo', input_var=self.proyecto['valormin']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Valor Máximo', input_var=self.proyecto['valormax']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Fecha Creacion', input_var=self.proyecto['creacion']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Cantidad Ofertas', input_var=self.proyecto['cantofertantes']).grid(row=i % k,column=(i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Oferta Mínima', input_var=self.proyecto['ofertamin']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Oferta Máxima', input_var=self.proyecto['ofertamax']).grid(row=i % k, column= (i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Oferta Promedio', input_var=self.proyecto['ofertapromedio']).grid(row=1 % k,column=(i//k)+1)
       i+=1
       li.LabelInput(self.frediproy,'Requisitos Especiales', input_var=self.proyecto['numhabilidades']).grid(row=i % k, column= (i//k)+1)
       #li.LabelInput(self.frediproy,'Numero Preguntas', input_var=self.proyecto['numpreguntas']).grid(row=19,column=1)
       #li.LabelInput(self.frediproy,'Cantidad Ofertas', input_var=self.proyecto['cantofertantes']).grid(row=20,column=1)
    """
    def muestra_proy(self,event):
       li.LabelInput(self.frediproy,'Nombre del Proyecto', input_var=self.proyecto['nomproyecto']).grid(row=1, column=1)
       li.LabelInput(self.frediproy,'Descripcion', input_class=ttk.Entry,input_var=self.proyecto['descripcion']).grid(row=2, 		column=1)
       li.LabelInput(self.frediproy,"País",input_class=ttk.Combobox, input_var=self.proyecto['paisproponente'],
       input_args={"values": ["Argentina", "Australia", "USA","Francia", "Alemania"]}).grid(row=3,column=1)
       li.LabelInput(self.frediproy,'Moneda', input_var=self.proyecto['moneda']).grid(row=4,column=1)
       li.LabelInput(self.frediproy,"Nombre Proponente", input_var=self.proyecto['nomproponente']).grid(row=5,column=1)
       li.LabelInput(self.frediproy,'Proyectos pagados', input_var=self.proyecto['proyectospagados']).grid(row=8,column=1)
       li.LabelInput(self.frediproy,'Numero Habilidades', input_var=self.proyecto['numhabilidades']).grid(row=9,column=1)
       li.LabelInput(self.frediproy,'Numero Preguntas', input_var=self.proyecto['numpreguntas']).grid(row=10,column=1)
       li.LabelInput(self.frediproy,'Valor Mínimo', input_var=self.proyecto['valormin']).grid(row=11,column=1)
       li.LabelInput(self.frediproy,'Valor Máximo', input_var=self.proyecto['valormax']).grid(row=12,column=1)
       li.LabelInput(self.frediproy,'Fecha Creacion', input_var=self.proyecto['creacion']).grid(row=13,column=1)
       li.LabelInput(self.frediproy,'Cantidad Ofertas', input_var=self.proyecto['cantofertantes']).grid(row=14,column=1)
       
       li.LabelInput(self.frediproy,'Oferta Mínima', input_var=self.proyecto['ofertamin']).grid(row=15,column=1)
       li.LabelInput(self.frediproy,'Oferta Máxima', input_var=self.proyecto['ofertamax']).grid(row=16,column=1)
       li.LabelInput(self.frediproy,'Oferta Promedio', input_var=self.proyecto['ofertapromedio']).grid(row=17,column=1)
       li.LabelInput(self.frediproy,'Requisitos Especiales', input_var=self.proyecto['numhabilidades']).grid(row=18,column=1)
       #li.LabelInput(self.frediproy,'Numero Preguntas', input_var=self.proyecto['numpreguntas']).grid(row=19,column=1)
       #li.LabelInput(self.frediproy,'Cantidad Ofertas', input_var=self.proyecto['cantofertantes']).grid(row=20,column=1)
  
    def changemaster(self):
        print(self.Master.get())
        listtprov=list(self.deatacched(item,'',self.listprel.index(item)))
        self.deatacched={}# hed.keys())
        for item in listprov:
            self.listprel.reattach()
            # se reatachea el item al list prel y se quita del dccionario

        if self.Master.get()==True: 
            try:
                #self.antdeatached=self.deatacched
                #self.deatacched ={}
                idsitio=self.refsitio.gridsitio.item(self.refsitio.gridsitio.focus())['values'][0]  
                for itemid in self.listprel.get_children():
                    if self.listprel.item(itemid)['values'][1]!=idsitio:  
                        # en el dicccionario deatached se incluye el iid generdo automatico y el indice
                        self.deatacched[itemid]=self.listprel.index(itemid)
                        self.listprel.detach(itemid)                    
            except:
                messagebox.showwarning('Advertencia','No ha seleccionado sitio')
        #listaproy=editprelproyectosdb(id)
        #self.llenagrid(listaproy)


       

  

    def muestraproyectos(self,frameshow,listaproyectos):
        def selectItem(event):
                curItem = self.listprel.focus()
                #idprelproy=self.listprel.item(curItem)['values'][0]
                fila=listaproyectos[int(curItem)-1]  # los enumeradores y bd el primer rticulo tiene id 1
                f=0
                for val in self.prelproy.values():
                    val.set(fila[f])
                    f+=1

 
    
                
      
        self.titleprel = tk.Label(frameshow, text="Proyectos del sitio "+self.nomsitio, font=("Arial",14))
        self.titleprel.grid(row=3, column=0)
        self.Master=tk.BooleanVar()
        self.ocultar=tk.IntVar()
        self.ocultar.set(0)
        self.Master.set(False)
        colspro = ['Orden', '#sitio', 'Fecha','URL','Copy', 'Oferta','','','','','']
        self.listprel = ttk.Treeview(frameshow, columns=colspro, displaycolumns=(0,1,2,3,4,5),height=8, padding=1, show="headings")
        self.listprel.grid(row=4, column=0, columnspan=10)
        for col in colspro:
            if colspro.index(col) in (0,1):
                self.listprel.column(col,width=15,anchor=tk.W)
            elif colspro.index(col) in (4,5):
                self.listprel.column(col,width=200,anchor=tk.W)   
            else: 
                self.listprel.column(col,width=80,anchor=tk.W)
            self.listprel.heading(col, text=col)
        self.but1=tk.Radiobutton(frameshow, text="Sitio", variable=self.Master, value=True, command= self.changemaster)
        self.but1.grid(row=3,column=3)
        self.but2=tk.Radiobutton(frameshow, text="Todos", variable=self.Master, value=False,command= self.changemaster)
        self.but2.grid(row=3,column=4)
  

        self.butshow=tk.Checkbutton(frameshow,text='Ocultar', variable=self.ocultar,command=self.ocultarlistprel).grid(row=3,column=5)
        self.llenagrid(listaproyectos)
        
        self.listprel.bind('<<TreeviewSelect>>', selectItem)

    def ocultarlistprel(self):
        if self.ocultar.get()==1:
            self.listprel.config(height=1)
            self.refsitio.listBox.config(height=27)
        else:
            self.listprel.config(height=18)
            self.refsitio.listBox.config(height=15)

    def llenagrid(self, listaproyectos):
        for row in self.listprel.get_children():
            self.listprel.delete(row)
        for i, (id,name,fecha,url,copy,copyofer) in enumerate(listaproyectos, start=1):
            self.listprel.insert("", "end", i,values=(id, name,fecha,url,copy,copyofer))


if __name__ == '__main__':
    raiz = tk.Tk()
    b=Proyecto(raiz,None,'Workana',2)
    b.newprelproy()
    #b.muestra_checkbut()
    raiz.mainloop()           



      
    
        
