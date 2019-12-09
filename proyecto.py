import tkinter as tk
from tkinter import ttk as ttk
from tkinter import messagebox
#from tkintertable.Tables import TableCanvas
from tkintertable import TableCanvas, TableModel
import sqlite3 

import enumeradores
import LabelInput as li
from sitio_backend import salvarprelproyectodb, editprelproyectosdb, editproyectosdb
import datetime

class Proyecto(tk.Frame):
    """Clase para definir los proyectos"""
    def __init__(self,refsitio,idsitio):
        super(Proyecto,self).__init__()
        self.nomsitio =refsitio.nomsitio
        self.idsitio = idsitio
        self.refsitio=refsitio
        self.frediproy=refsitio.frediproy
        self.frediprelproy=refsitio.frediprelproy
        #self.refsitio.enablebutproyectos()
        self.deatacched={}

        self.prelproy={'idprelproyecto':tk.IntVar(),'idsitio':tk.IntVar(),'fechavisita':tk.StringVar(),'url':tk.StringVar(),
        'copy':tk.StringVar(), 'copyofer':tk.StringVar(),'keywords':tk.StringVar()}

        self.prelproyval={'idprelproyecto':-1,'idsitio':0,'fechavisita':'','url':'',
        'copy':'', 'copyofer':'','keywords':''}


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
        self.prelproyv['fechavisita']=li.LabelInput(self.frediprelproy,'Fecha', input_var=self.prelproy['fechavisita'])
        self.prelproyv['fechavisita'].grid(row=3,column=1)
        self.prelproyv['url']=li.LabelInput(self.frediprelproy,'URL', input_var=self.prelproy['url'])
        self.prelproyv['url'].grid(row=4, column=1)
        self.prelproyv['keywords']=li.LabelInput(self.frediprelproy,'Palabras Claves',input_var=self.prelproy['keywords'])
        self.prelproyv['keywords'].grid(row=5,column=1)
        self.prelproyv['copy']=li.LabelInput(self.frediprelproy,'Copia del Proyecto', input_class=tk.Text,input_args={"height": 15,"width": 60})
        self.prelproyv['copy'].grid(row=6,column=1,rowspan=10)
        self.prelproyv['copyofer']=li.LabelInput(self.frediprelproy,'Copia de la Oferta', input_class=tk.Text,input_args={"height": 15,"width": 60})
        self.prelproyv['copyofer'].grid(row=18,column=1,rowspan=10)
        self.prelproyv['copy'].set(self.prelproy['copyofer'].get())
        self.prelproyv['copyofer'].set('END',self.prelproy['copy'].get())
        

    def editprelproy(self):
        #se incluye en este procedimeinto ls varibles derivadas o los etrey ls demas entran como variables de contro de tkinter
        self.prelproy['idsitio'].set(self.idsitio)
        self.prelproy['fechavisita'].set(str(datetime.datetime.now())) 
        self.prelproyv['copy'].set(self.prelproy['copy'].get())
        self.prelproyv['copyofer'].set(self.prelproy['copyofer'].get())
        
    
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
        print(self.Master.get(),self.deatacched)
        if self.deatacched!={}:
            listprov=self.deatacched.values()
            #listtprov=list(self.deatacched(item,'',self.listprel.index(item))) # esto da error parede estaba mal
            self.deatacched={} # hed.keys())
            for item in listprov:
                self.listprel.reattach(item,'',self.listprel.index(item))
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
                print(self.Master.get(),self.deatacched)

            except:
                messagebox.showwarning('Advertencia','No ha seleccionado sitio')
        self.changetitles()        
        #listaproy=editprelproyectosdb(id)
        #self.llenagrid(listaproy)


    def selectItemprel(self,event, listaproyectos):
        curItem = self.listprel.focus()
        #idprelproy=self.listprel.item(curItem)['values'][0]
        fila=listaproyectos[int(curItem)-1]  # los enumeradores y bd el primer rticulo tiene id 1
        f=0
        for val in self.prelproy.values():
            val.set(fila[f])
            f+=1
        self.editprelproy()

    def selectItemproy(self,event, listaproyectos):
        curItem = self.gridproy.focus()
        #idprelproy=self.listprel.item(curItem)['values'][0]
        fila=listaproyectos[int(curItem)-1]  # los enumeradores y bd el primer rticulo tiene id 1
        f=0
        for val in self.proyecto.values():
            val.set(fila[f])
            f+=1

            

    def muestraproyectos(self,frameshow,listaproyectos):     
        self.titleprel = tk.Label(frameshow, text="Proyectos del sitio "+self.nomsitio, font=("Arial",14))
        self.titleprel.grid(row=3, column=0)
        self.Master=tk.BooleanVar()
        self.ocultar=tk.IntVar()
        self.ocultar.set(0)
        self.Master.set(False)
        self.showproyecto=tk.BooleanVar()
        self.showproyecto.set(False)
        #colspro = ['Orden', '#sitio', 'Fecha','URL','Copy', 'Oferta']
        # columns=colspro, displaycolumns=(0,1,2,3,4,5),  >> pasado a ist proy
        self.but1=tk.Radiobutton(frameshow, text="Sitio", variable=self.Master, value=True, command= self.changemaster)
        self.but1.grid(row=3,column=3)
        self.but2=tk.Radiobutton(frameshow, text="Todos", variable=self.Master, value=False,command= self.changemaster)
        self.but2.grid(row=3,column=4)
        self.butshow=tk.Checkbutton(frameshow,text='Ocultar', variable=self.ocultar,command=self.ocultarlistprel).grid(row=3,column=5)
        self.butproyectos=tk.Checkbutton(frameshow,text='Proyectos', variable=self.showproyecto,command=self.listproy).grid(row=3,column=6)
        self.listprel = ttk.Treeview(frameshow,height=8, padding=1, show="headings")
        self.listprel.grid(row=4, column=0, columnspan=10)
        self.configureprel()
        self.gridproy = ttk.Treeview(frameshow,height=8, padding=1, show="headings")
        self.gridproy.grid(row=5, column=0, columnspan=10)
        self.configureproy()
        self.listproy()
        #self.llenagrid(listaproyectos) # show.proyecto muestra el proyecto True, False Muestra el preliminar
        self.listprel.bind('<<TreeviewSelect>>',lambda event,arg=self.listaproyecto: self.selectItemprel(event,arg))
        self.gridproy.bind('<<TreeviewSelect>>',lambda event,arg=self.listaproyecto: self.selectItemproy(event,arg))

    
    def configureprel(self):
        colspro = ['Orden', '#sitio', 'Fecha','URL','Copy', 'Oferta']
        self.listprel['columns'] =colspro
        self.listprel['displaycolumns']=(0,1,2,3,4,5)
        
        for col in colspro:
            if colspro.index(col) in (0,1):
                self.listprel.column(col,width=15,anchor=tk.W)
            elif colspro.index(col) in (4,5):
                self.listprel.column(col,width=200,anchor=tk.W)   
            else: 
                self.listprel.column(col,width=80,anchor=tk.W)
            self.listprel.heading(col, text=col)
        
    def configureproy(self):
        colspro = ('idproy','idsit','idclie','nomproy','descr','mon','nompr','paispr','propag','numhab','numpr','valmin','valmax','ofmax','ofmin','ofpr','cantof','reqesp','crea','skills','ratprop','ref')
        self.gridproy['columns']=colspro
        self.gridproy['displaycolumns']= (1,3,5,6,7,8,10,11,4)
        for col in colspro:
            if colspro.index(col) in (0,1,5):
                self.gridproy.column(col,width=15,anchor=tk.W)
            elif colspro.index(col) in (3,6,7,8,9,10,11,13):
                self.gridproy.column(col,width=80,anchor=tk.W)   
            elif colspro.index(col)==4: 
                self.gridproy.column(col,width=200,anchor=tk.W)
            self.gridproy.heading(col, text=col)
            print(self.gridproy.column(col))
        if self.idsitio==-1: self.idsitio=0  # para probar quitar despues
         
        
    def ocultarlistprel(self):
        if self.ocultar.get()==1:
            self.listprel.config(height=1)
            self.refsitio.gridsitio.config(height=27)
            self.gridproy.config(height=1)
        else:
            self.listprel.config(height=18)
            self.gridproy.config(height=18)
            self.refsitio.gridsitio.config(height=15)

    def changetitles(self):
        if self.Master==True:
            var2= ' del sitio '+ self.nomsitio
        else:
            var2= ''
        if self.showproyecto.get()==True:
            var1='Proyectos'
        else:
            var1='Preliminares'
        self.titleprel['text']= var1 + var2

    
    def listproy(self):                    
        if self.showproyecto.get()==True:
            self.frediprelproy.pack_forget()
            self.frediproy.pack()
            self.listprel.grid_forget()
            self.gridproy.grid(row=5,column=0,columnspan=10)                       
            self.listaproyecto=  editproyectosdb(self.idsitio)              
            self.llenagrid (self.listaproyecto)

        else:     
            
            self.frediprelproy.pack()
            self.frediproy.pack_forget()
            self.listprel.grid(row=4,column=0,columnspan=10)
            self.gridproy.grid_forget()
            #self.refsitio.enablebutpreliminares()                      
            self.listaproyecto=  editprelproyectosdb(self.idsitio)              
            self.llenagrid (self.listaproyecto) 
        self.changetitles()
        
        

       
            
    def llenagrid(self, listaproyectos):
        if self.showproyecto.get()==False:    
            for i, (id,name,fecha,url,copy,copyofer,keyword) in enumerate(listaproyectos, start=1):
                print (i,id,name)
                self.listprel.insert("", "end", i,values=(id,name,fecha,url,copy,copyofer,keyword))
        else:
            for i, (idproyecto,idsitio,idcliente,nomproyecto,descripcion,moneda,nomproponente,paisproponente,proyectospagados,numhabilidades,numpreguntas,valormin,valormax,ofertamax,ofertamin,ofertapromedio,cantofertantes,requisitosesp,creacion,skills,ratingproponente,referencia) in enumerate(listaproyectos, start=1):
                self.gridproy.insert("", "end", i,values=(idproyecto,idsitio,idcliente,nomproyecto,descripcion,moneda,nomproponente,paisproponente,proyectospagados,numhabilidades,numpreguntas,valormin,valormax,ofertamax,ofertamin,ofertapromedio,cantofertantes,requisitosesp,creacion,skills,ratingproponente,referencia))



if __name__ == '__main__':
    raiz = tk.Tk()
    b=Proyecto(raiz,-1)
    b.newprelproy()
    #b.muestra_checkbut()
    raiz.mainloop()           



      
    
        
