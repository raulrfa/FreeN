from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox
from enumeradores import Idiomas, Habilidades
from sqlite3 import *
from sitio_backend import *
from proyecto import Proyecto
import dictsit
from StartDriveApi import *
import LabelInput as li
import hndwindows

class Busqproywin:
#Busqproywin(self.sitio['idsitio'].get(),self.sitio['nomsitio'].get(),idioma,habilidades,self.sitio['urlproy'].get(),self.sitio['nombusq'].get(),'freebd.db')
    def __init__(self, idfreelancer, idsitio, sitio,idioma, tema, xdict, urlproy, tiplogin, nombusq,clavebusq,bd):
        """ Ventana flotante para editar coverofertas y poder rectificarla t y salvarla a
        la base de datos."""
        print(id,idioma,sitio, tema,urlproy, nombusq,clavebusq, sep='   ')
        proymark=[]
        self.idfreelancer= idfreelancer
        self.idsitio = idsitio
        self.sitio=sitio
        self.lenguaje = idioma
        self.habi = tema
        self.urlproy = dictsit.tab_lista= dictsit.tab_proy= dictsit.tab_ofer=urlproy
        dictsit.init_driver()       
        self.raiz = Tk()
        self.filtro = '' # posible uso de filtro
        self.click=1 # paso a diferentes paginas iniciales 
        self.tiplogin=tiplogin
        self.nombusq=nombusq
        self.clavebusq=clavebusq
        self.handle=hndwindows.WindowMgr()
        self.login=False
        self.drproy=None
        self.drofer=None

        # Define las dimensiones de la ventana, que se ubicará en 
        # el centro de la pantalla. Si se omite esta línea la
        # ventana se adaptará a los widgets que se coloquen en
        # ella. 
        # todo: gewwn 
        #  esta feo

        #self.raiz.geometry('1200x600') # anchura x altura

        # Asigna un color de fondo a la ventana. Si se omite
        # esta línea el fondo será gris

        self.raiz.configure(bg = 'cyan')

        # Asigna un título a la ventana

        self.raiz.title('Editor de busquedas: ' + str(self.idsitio) )       
        w = self.raiz.winfo_screenwidth()
        h = self.raiz.winfo_screenheight()
        self.raiz.geometry("%dx%d+0+0" % (w, h))




        
        # Define un botón en la parte inferior de la ventana
        # que cuando sea presionado hará que termine el programa.
        # El primer parámetro indica el nombre de la ventana 'raiz'
        # donde se ubicará el botón
        self.proyecto={
            'nomproyecto'       :  StringVar(),
            'descripcion'       :  StringVar(),
            'idproyecto'        :  IntVar(),
            'idfreelancer'      :  IntVar(),
            'creacion'          :  StringVar(),
            'idsitio'           :  IntVar(),
            'skills'            :  StringVar(),
            'nomproponente'     :  StringVar(),
            'paisproponente'    :  StringVar(),
            'ratingproponente'  :  StringVar(),
            'moneda'            :  StringVar(),
            'presupuestos'      :  StringVar(),
            'proyectospagados'  :  IntVar(),            
            'numhabilidades'    :  IntVar(),
            'numpreguntas'      :  IntVar(),
            'ofertamax'         :  IntVar(),
            'ofertamin'         :  IntVar(),
            'ofertapromedio'    :  IntVar(),
            'cantofertantes'    :  StringVar(),
            'requisitosesp'     :  StringVar(),
            'valormax'          :  IntVar(),
            'valormin'          :  IntVar(),
            
            'referencia'        :  StringVar(),
           # '.descripcion'      :  StringVar(),
            '.deadline'         :  StringVar(),
            '.expdate'          :  StringVar(),
            '.ofertar'          :  StringVar(),
            'ultimologin'       :  StringVar(),
            'proyectospagados'  :  IntVar(),}

        self.widgproy = {
            'nomproyecto'       :  [Text,4,25],
            'descripcion'       :  [Text,10,50],
            'skills'            :  [Text,6,20] }

        self.oferta={
            'idoferta'          :  IntVar(),
            'idproyecto'        :  IntVar(),
            'creacion'          :  StringVar(),
            'mensajes'          :  StringVar(),
            'coverletter'       :  StringVar(),
            'ganttoferta'       :  StringVar(),
            'answers'           :  StringVar(),
            'plazo'             :  StringVar(),               
            'moneda'            :  StringVar(), 
            'valoroferta'       :  IntVar(),
            'costooferta'       :  IntVar(),
            'devengado'         :  IntVar(),
            'fechaofer'         :  StringVar(),
            'cantmensajes'      :  IntVar(),
            'fechaultmensaje'   :  StringVar(),
            'requisitosesp'     :  StringVar(),
            'includedfile'      :  StringVar(),
            'referenciaofer'    :  StringVar()}
            
        
        self.widgofer         = {
            'mensajes'          :  [Text,4,30,None],
            'coverletter'       :  [Text,10,30,None],
            'ganttoferta'       :  [Text,6,30,None],
            'answers'           :  [Text,4,30,None]}

        self.creaframes()
        self.muestraforma()
        self.raiz.mainloop()

    def muestra_proy(self,printvacio,columnas,heightmax):
       for widg in self.frediproy.winfo_children():
            widg.destroy()
       cols=[]
       for col in range(columnas): cols.append(0)
       for key in self.proyecto.keys():
          print(key,cols) 
          if printvacio or (isinstance(self.proyecto[key],IntVar) and self.proyecto[key].get()!=0) or (isinstance(self.proyecto[key],StringVar) and self.proyecto[key].get()!=''):
                 
                if key in self.widgproy:                      
                    textprov =li.LabelInput(self.frediproy,key,input_class=self.widgproy[key][0],input_args={'height':self.widgproy[key][1],'width':self.widgproy[key][2]})
                    textprov.set(self.proyecto[key].get())
                    for col in range(len(cols)):
                        if cols[col]+self.widgproy[key][1]//2<heightmax:
                            textprov.grid(row=cols[col], column=col,rowspan=self.widgproy[key][1]//2)#,columnspan=3 )
                            print('posiciontext ', key, cols[col], col)
                            cols[col]+=self.widgproy[key][1]//2
                            break
                        else:
                            continue                           
                    
                    #textprov.widgproy[key].insert('1,0',self.proyecto[key])
                    
                else:
                    textprov=li.LabelInput(self.frediproy,key,input_var=self.proyecto[key])
                    for col in range(len(cols)):
                        if cols[col]<heightmax:
                           textprov.grid(row=cols[col], column=col)
                           print('posic wid',key, cols[col], col)
                           cols[col]+=1
                           break
                        else:
                            continue                           
                                              
                    
    def muestra_ofer(self,xdict,printvacio,printnoindict,columnas,heightmax):
       for widg in self.froferta.winfo_children():
            widg.destroy()
       cols=[]
       for col in range(columnas): cols.append(0)       
       for key in self.oferta.keys():
          if (printnoindict or "#"+key in xdict.keys()):
            print(key,cols) 
            if printvacio or (isinstance(self.oferta[key],IntVar) and self.oferta[key].get()!=None) or (isinstance(self.oferta[key],StringVar) and self.oferta[key].get()!=''):
                    
                    if key in self.widgofer:                      
                        textprov =li.LabelInput(self.froferta,key,input_class=self.widgofer[key][0],input_args={'height':self.widgofer[key][1],'width':self.widgofer[key][2]})
                        textprov.set(self.oferta[key].get())
                        self.widgofer[key][3]=textprov  # se guardan los inputs
                        for col in range(len(cols)):
                            if cols[col]+self.widgofer[key][1]//2<heightmax:
                                textprov.grid(row=cols[col], column=col,rowspan=self.widgofer[key][1]//2)#,columnspan=3 )
                                print('posiciontext ', key, cols[col], col)
                                cols[col]+=self.widgofer[key][1]//2
                                break
                            else:
                                continue                           
                        
                        #textprov.widgproy[key].insert('1,0',self.oferta[key])                        
                    else:                    
                        textprov=li.LabelInput(self.froferta,key,input_var=self.oferta[key])
                        for col in range(len(cols)):
                            if cols[col]<heightmax:
                                textprov.grid(row=cols[col], column=col)
                                print('posic wid',key, cols[col], col)
                                cols[col]+=1
                                break
                            else:
                                continue                           
                        
             


        
    def llenagrid(self, columns, listaproyectos):
        #print(listaproyectos)
        for row in self.listprel.get_children():
            self.listprel.delete(row)
        columns=columns
        tit=tuple(columns)
        for i, (tit) in enumerate(listaproyectos, start=1):
            self.listprel.insert("", "end", i,values=(tit))
        self.listprel.selection_set(str(1))    
        self.listprel.focus(str(1))    
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
    """
    def creaframes(self):
        self.frcompose = Frame(self.raiz, bg='yellow')
        self.frcompose.pack(side=TOP, fill=Y,expand=1)
        
        self.frlist = LabelFrame(self.frcompose, bg='gray', padx=5,pady =5, text ='Idioma/Tema')
        self.frlist.pack(side=LEFT, fill=Y)
        self.frlistinside=Frame(self.frlist, bg='gray') # internal frame to fothet
        self.frlistinside.pack(side=LEFT, fill=Y)
        self.frlistbut=Frame(self.frlistinside,bg='gray')
        self.frlistbut.pack(side=BOTTOM)
        self.fredit = Frame(self.frcompose, bg='lightblue', padx=5,pady =5)
        self.fredit.pack(side=LEFT, fill=Y)
        self.froferta=LabelFrame(self.frcompose, bg='gray', padx=5,pady =5, text ='Oferta')
        self.froferta.pack(side=LEFT, fill=Y)
        self.frbusqedit=Frame(self.fredit)
        self.frbusqedit.pack(side=TOP)        
        self.frencedit=Frame(self.fredit) # contiene solo la grid pra que no se olvid ela posicion
        self.frencedit.pack(side=TOP)
        self.frgridprel=Frame(self.fredit,padx=5,pady=5) # contiene solo la grid pra que no se olvid ela posicion
        self.frgridprel.pack(side=TOP)
        self.frediproy=Frame(self.fredit,bg='gray')
        self.frediproy.pack(side=TOP,expand=Y)
        self.frmenubut = Frame(self.fredit, bg='black', padx=2,pady =2)
        self.frmenubut.pack(side=TOP, fill=X) 

    def muestraforma(self):        
        self.lbidio = Listbox(self.frlistinside,exportselection=False,selectmode=MULTIPLE,width=8, height=30)
        self.lbidio.pack(side=LEFT,expand=0,fill=Y)
        for idio in self.lenguaje:
            self.lbidio.insert(END,idio) # despues se analiza si se coge de bd
            #self.lbidio.insert(END,Idiomas(i).name[0:3].upper())
        #if self.lenguaje!=None:
            #self.lbidio.selection_set(self.lbidio.get(0,END).index(self.lenguaje))    
        self.var_hab=StringVar()
        self.listahab=enumeradores.verenum(Habilidades)
        print('listahab', self.listahab)
        #self.var_tema.set(listahab)
        self.lbtema = Listbox(self.frlistinside,exportselection=False,selectmode=MULTIPLE,listvariable=self.var_hab,width=8, height=30)
        for item in self.listahab:
             self.lbtema.insert(END,item[1])
        self.lbtema.pack(side=LEFT,expand=0,fill=Y)
        #self.var_tema.set(['salu','pres', 'expe', 'cert', 'refe', 'extras', 'desp','todo'])
        #if self.habi!=None:
            #self.lbtema.selection_set(self.lbtema.get(0,END).index(self.habi))
        self.textlab1=Label(self.frencedit,text='URL Proyecto: ')
        self.textlab1.pack(side=LEFT)
        self.edit_url=StringVar()
        self.text_edit = Entry(self.frencedit,textvariable=self.edit_url,width=60,bg='white',fg='black')
        #self.text_edit.bind('<Alt-KeyPress>',self.copyfromcomposer)
        self.text_edit.pack(side=LEFT)
        if self.urlproy!=None: self.edit_url.set(self.urlproy)
        self.butrefreshurl=Button(self.frencedit, text= 'Refescar',command=self.refresh)
        self.butrefreshurl.pack(side=LEFT, padx=4)
        self.butback= Button(self.frencedit, text= ' < ',command=self.backward)
        self.butback.pack(side=LEFT, padx=10)
        self.butforward= Button(self.frencedit, text= ' > ',command=self.forward)
        self.butforward.pack(side=LEFT, padx=10)
        self.colspro, colsize, colview =dictsit.findkeynamesize(dictsit.elem_sitio(self.sitio))            
        #colspro = ['Titulo','Fecha','Elemento','Fechas','Bids','Clientes','Paises','Rating','Presupuesto','Textos','url','Skills']
        self.listprel =ttk.Treeview(self.frgridprel, columns=self.colspro, displaycolumns=colview,height=12, padding=1, show="headings")
        self.listprel.pack(side=TOP)
        for col in self.colspro:
            self.listprel.column(col,width=colsize[self.colspro.index(col)],anchor=W)
            self.listprel.heading(col, text=col)
        self.lab_filtro =Label(self.frbusqedit,text='Filtrar por:')
        self.lab_filtro.pack(side=LEFT)
        self.var_filtro = StringVar()
        self.var_filtro.set(self.filtro)
        self.edit_filtro = Entry(self.frbusqedit,textvariable=self.var_filtro,width=60,bg='white',fg='black')
        self.edit_filtro.pack(side=LEFT,fill=Y)  
        self.butfiltrar= Button(self.frbusqedit, text= 'Filtrar',command=self.filtrar)
        self.butfiltrar.pack(side=LEFT, padx=5)
        self.butsitio= Button(self.frmenubut, text= 'Sitio',command=self.gositio)
        self.butsitio.pack(side=LEFT, padx=5)
        self.butmenos1= Button(self.frmenubut, text= ' <1 ',command=self.menos)
        self.butmenos1.pack(side=LEFT, padx=5)
        self.butmas1= Button(self.frmenubut, text= ' 1> ',command=self.mas)
        self.butmas1.pack(side=LEFT, padx=5)
        self.butcomponer= Button(self.frmenubut, text= 'Ver Listado',command=self.verlistado)
        self.butcomponer.pack(side=LEFT, padx=5)
        self.butverproyecto= Button(self.frmenubut, text= 'Ver Proyecto',command=self.verproyecto)
        self.butverproyecto.pack(side=LEFT, padx=5)
        self.butmarcarproyecto= Button(self.frmenubut, text= 'Marcar Proyecto',command=self.marcarproyecto)
        self.butmarcarproyecto.pack(side=LEFT, padx=5)
        self.butverproyecto.bind('<<Alt-Control-KeyPress>>', lambda event:self.controlkey(event))
        self.butofertar= Button(self.frmenubut, text= 'Ofertar',command=self.ofertar)
        self.butofertar.pack(side=LEFT, padx=5)        
        self.butsalvar= Button(self.frmenubut, text= 'Salvar',command=self.salvar)
        self.butsalvar.pack(side=LEFT, padx=5)
        self.butcomponer= Button(self.frmenubut, text= 'Cover Letter',command=self.defcover)
        self.butcomponer.pack(side=LEFT, padx=5)
        self.butsalvarofer= Button(self.frmenubut, text= 'Procesar Oferta',command=self.procesar)
        self.butsalvarofer.pack(side=LEFT, padx=5)
        self.butlistfilter= Button(self.frlistbut, text= 'Filtrar x Lista',command=self.filtrarXlistaRedu)
        self.butlistfilter.pack(side=BOTTOM, padx=10)
        listaproyectos=dictsit.findelements(dictsit.elem_sitio(self.sitio))
        #self.butshow=tk.Checkbutton(frameshow,text='Ocultar', variable=self.ocultar,command=self.ocultarlistprel).grid(row=3,column=5)
        self.listprel.bind('<<TreeviewSelect>>', lambda event: self.selectItem(event))
        self.listprel.tag_configure('mark', foreground='red')
        self.llenagrid(self.colspro, listaproyectos)

    def marcarproyecto(self):
        line=self.listprel.item(self.listprel.focus(),tags=('mark'))
        proymark.append(line)
        
    def refresh(self):
        self.edit_url.set(dictsit.driver.current_url)
        listaproyectos=dictsit.findelements(dictsit.elem_sitio(self.sitio))
        #self.butshow=tk.Checkbutton(frameshow,text='Ocultar', variable=self.ocultar,command=self.ocultarlistprel).grid(row=3,column=5)
        self.llenagrid(self.colspro, listaproyectos)

    def backward(self):
        self.edit_url.set(dictsit.driver.back)
        listaproyectos=dictsit.findelements(dictsit.elem_sitio(self.sitio))
        #self.butshow=tk.Checkbutton(frameshow,text='Ocultar', variable=self.ocultar,command=self.ocultarlistprel).grid(row=3,column=5)
        self.llenagrid(self.colspro, listaproyectos)

    def forward(self):
        self.edit_url.set(dictsit.driver.forward)
        listaproyectos=dictsit.findelements(dictsit.elem_sitio(self.sitio))
        #self.butshow=tk.Checkbutton(frameshow,text='Ocultar', variable=self.ocultar,command=self.ocultarlistprel).grid(row=3,column=5)
        self.llenagrid(self.colspro, listaproyectos)

    def selectfilter(self,sender):
        if self.filtered==sender:
            sender.configure(bg='white')
            self.filtered=None
        elif  sender =='Lista' and self.filtered!='Lista':
           self.butlistfilter.configure(bg='green')
           self.butfiltrar.configure(bg='white')

    def procesar(self):
        if self.oferta['idoferta'].get()==None : self.oferta['idoferta'].set(0)
        for key in self.widgofer:  # se pasan los campos escribibles
            if self.widgofer[key][3]!=None :
                self.oferta[key].set(self.widgofer[key][3].get())
        dictsit.makeoferta(dictsit.elem_sitio(self.sitio),self.oferta,'w') # escribir los campos en la web
        dictsit.makeoferta(dictsit.elem_sitio(self.sitio),self.oferta,"R") # leer los campos asociados a la escitura
        if messagebox.askquestion(' Adverterncia', 'Esta seguro de enviar la oferta'):
            dictsit.makeoferta(dictsit.elem_sitio(self.sitio),self.oferta,'P') # escribir los campos en la web     

    def controlkey(self,event):
        if event.char   =='p' : 
            self.verproyecto()
        elif event.char =='l' : 
            self.verlistado()
        elif event.char =='e' : 
            self.ofertar()    
    
    def defcover(self):
        try: 
            self.handle.findwindow('',"Analizador de ")
            self.handle.set_foreround()
        except:      
            os.startfile("StartDriveApi.exe")

        """
        llamandolo desde el codigo
        new_window=Tk()
        gd=ViewDrive(new_window,main(),1)
        gd.gui_butmenu()
        gd.gui_oferta_guardada()
        #gd.cambiartit()
        #raiz.mainloop()"""

    def gositio(self):
        try:
            self.handle.findwindow('',"tk")
            self.handle.set_foreround()
        except:        
            os.startfile("Sition.exe")        

    def selectItem(self,event):
        curitem = self.listprel.focus()
        for key in self.proyecto.keys():
            if key.capitalize() in self.colspro: 
                #print('colspro  ',self.listprel.item(curitem,'values'))
                #print (key,  self.colspro.index(key.capitalize()) , self.listprel.item(curitem)['values'][self.colspro.index(key.capitalize())])
                self.proyecto[key].set(self.listprel.item(curitem)['values'][self.colspro.index(key.capitalize())])
            else:
                if isinstance(self.proyecto[key],IntVar):
                    self.proyecto[key].set(0)
                else:
                    self.proyecto[key].set('')        
            print(key, self.proyecto[key].get(), sep=' ')
        self.muestra_proy(True,8,8)
        
    def oldmuestra_proy(self,event):
       i=0
       if isinstance(event,int):
           k=event
       else:
           k=20
       i+=1
       li.LabelInput(self.frediproy,'Nombre del Proyecto', height=2,input_var=self.proyecto['nomproyecto']).grid(row=i % k, column= (i//k)+1)
       i+=2
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
       i+=4
       descr=li.LabelInput(self.frediproy,'Descripcion', heigt=7,input_class=Text).grid(row=i % k, column= (i//k)+1)
       descr.insert('1,0',self.proyecto['descripcion'])
       #li.LabelInput(self.frediproy,'Numero Preguntas', input_var=self.proyecto['numpreguntas']).grid(row=19,column=1)
       #li.LabelInput(self.frediproy,'Cantidad Ofertas', input_var=self.proyecto['cantofertantes']).grid(row=20,column=1)

    def verproyecto(self):
        
        self.urllist=dictsit.driver.current_url
        #dictsit.driver.get(self.proyecto['referencia'].get())
        dictsit.switchtab(1,self.proyecto['referencia'].get())
        if dictsit.findextraproy(dictsit.elem_sitio('Workana'),self.proyecto)==False:
            messagebox.showinfo('','No se pudo abrir la web')
        self.edit_url.set(self.proyecto['referencia'].get())
        self.frlist.pack_forget()
        print('propagateprel',self.frgridprel.pack_propagate())
        self.frgridprel.pack_forget()
        print('propagatelistinside', self.frlistinside.pack_propagate())
        self.widgproy['descripcion']=[Text,20,50]
        print('muestraproy')
        #self.butverproyecto.configure(text='Ver Listado')
        #self.butverproyecto.configure(command=self.verlistado)
        self.butsalvar.configure(state='normal')
        self.butofertar.configure(state='normal')
        self.muestra_proy(False,6,16)

    def verlistado(self):
        self.textlab1.configure(text='URL General: ')
        dictsit.switchtab(0,'')
        self.edit_url.set(self.urllist)

        self.widgproy['descripcion']=[Text,10,50]
        #self.butverproyecto.configure(text='Ver Proyecto')
        #self.butverproyecto.configure(command=self.verproyecto)
        self.butsalvar.configure(state='disabled')
        self.butofertar.configure(state='disabled')
        #self.frgridprel.pack_propagate(True)
        #self.frlistinside.pack_propagate(True)
        self.frlist.pack(before=self.fredit,side=LEFT)
        self.frgridprel.pack(before=self.frediproy, side=TOP)
        self.froferta.pack_forget()
        self.muestra_proy(True,8,8)
        #dictsit.driver.back()        
        
    def filtrar(self):
        listaproyectos=dictsit.findelements(dictsit.elem_sitio(self.sitio),self.var_filtro.get(),'gen')
        self.edit_url.set(dictsit.driver.current_url)
        self.llenagrid(self.colspro,listaproyectos)
    def mas(self):
        self.click+=1
        listaproyectos=dictsit.findelements(dictsit.elem_sitio(self.sitio),self.click)
        self.edit_url.set(dictsit.driver.current_url)
        self.llenagrid(self.colspro,listaproyectos)

    def menos(self):
        self.click-=1
        listaproyectos=dictsit.findelements(dictsit.elem_sitio(self.sitio),self.click)
        self.edit_url.set(dictsit.driver.current_url)
        self.llenagrid(self.colspro,listaproyectos)

    def filtrarXlistaRedu(self):   # este es un uso aterno sin que usen los xdict u todo el problema de los filtros y la ISO
        idiosel=self.lbidio.curselection()
        idiomtrad=[]
        for idio in idiosel: 
            idiomtrad.append(self.lbidio.get(idio))
        habsel=self.lbtema.curselection()
        habtrab=[]
        for skill in habsel:
            strskill=self.lbtema.get(skill)
            habtrab.append(strskill)
        edifilter= ' '.join(idiomtrad) +' ' +' '.join(habtrab)
        print('Filtado x Lista ',edifilter)
        listaproyectos=dictsit.findelements(dictsit.elem_sitio(self.sitio),edifilter,'gen')
        self.edit_url.set(dictsit.driver.current_url)
        self.llenagrid(self.colspro,listaproyectos)

  
    def filtrarXlista(self):
        idiosel=self.lbidio.curselection()
        habsel=self.lbtema.curselection()
        #print('idio ',idiosel)
        #print('hab ',habsel)
        xdict=dictsit.elem_sitio(self.sitio)
        url=xdict['url']
        if idiosel!=():
            strini=xdict['filtroidio'][0]
            if xdict['filtroidio'][2]=='ISO': # se usa la ISO 659 para hacer a query de idiomas 
                idiomtrad=[]
                for idio in idiosel: 
                    idiomtrad.append(self.lbidio.get(idio))
                if len(idiomtrad)==1 :
                     idiomtrad.append('') # para tratar las tuplas de 1 element que dan una coma adicional
                idioISO=queryidiomasISO(enumeradores.Idiomas, idiomtrad) #retorna una[(lista de tupla)]      
                for idio in idioISO[0]:
                    strini=strini+idio+xdict['filtroidio'][1]
            else: # no hay que traducri al ISO 639 
               for idio in idiosel:                         
                   strini+=self.lbidio.get(idio)+xdict['filtroidio'][1]
            url=url+strini[:-len(xdict['filtroidio'][1])]+xdict['filtrounion'][0]
       
        if habsel!=():
            strini=xdict['filtroskills'][0]
            for skill in habsel:
                strini+=self.lbtema.get(skill)+xdict['filtroskills'][1]
            url=url+strini[:-len(xdict['filtroskills'][1])]+xdict['filtrounion'][0]
        url=url[:-len(xdict['filtrounion'][0])] # se le quita la utima union
        dictsit.gotourl(url)






    def salvar(self):
        # para salvar se debe borrar el id proyecyo a meneos que exista. Se pone el idsitio solo sirve para salvar
        if self.proyecto['idproyecto'].get()==0:
             del self.proyecto['idproyecto']
        self.proyecto['idsitio'].set(self.idsitio)
        # se repone el id proyecto
        try:
            valorid=(salvadict('proyecto',dictvartoval(self.proyecto)))
            
        except:
            messagebox.showerror('Error', 'No se pudo salvar el proyecto')
            valorid=0
        finally:
            self.proyecto['idproyecto']=IntVar()
            self.proyecto['idproyecto'].set(valorid)
        # salva la oferta si esta visible
        if self.froferta.winfo_manager()!='': # esta visible selfroferta
            if self.oferta['idoferta'].get()==0:
                del self.oferta['idoferta']
            self.oferta['idproyecto']=self.proyecto['idproyecto']
            try:
                valorid=(salvadict('oferta',dictvartoval(self.oferta)))
            except:
                messagebox.showerror('Error', 'No se pudo salvar el proyecto')
                valorid=0
            finally:
                self.oferta['idoferta']=IntVar()
                self.oferta['idoferta'].set(valorid)

            
    def copiar(self):
        clip = Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(self.text_edit.get('1.0',END) )  # Change INFO_TO_COPY to the name of your data source
        clip.destroy()

    def ofertar(self):
        #TODO se necesita creAR EL ECANISMO EN BASE DE DATOS DE TIPO DE LOGIN
        dictsit.switchtab(2,self.proyecto['.ofertar'].get())
        if not self.login:
            if dictsit.login(dictsit.elem_sitio(self.sitio),'Google',self.nombusq,self.clavebusq)!=None:
                self.login=True
            else: 
                messagebox.showerror('Error en el logeo', 'No puede ofertar, Favor revisar la llave de la base de datos')
                return
        #dictsit.switchtab(2,self.proyecto['.ofertar'].get())
        if not dictsit.assertoferta(dictsit.elem_sitio(self.sitio)):
                    #TODO esta mal parece qur yirnr que ponerse este o no logeado
                    messagebox.showerror('Error en la web', 'No puede encontrar la web de oferta, Favor revisar la llave del diccionario')
                    return
        errors = dictsit.makeoferta(dictsit.elem_sitio(self.sitio),self.oferta,'r') 
        if errors!=[] : messagebox.showwarning('Advertencia', 'no se puderon encontrar '+','.join(errors))  
        self.froferta.pack(side=LEFT)     
        self.muestra_ofer(dictsit.elem_sitio(self.sitio),True,False,4,16)
        
        """"click
        #app > div > div.container.main > div.access.access-floating > div > div > div.box-common.box-lg > div > div:nth-child(2) > div > div:nth-child(2) > p > a
        xpath //*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/p/a
       
        vd = Toplevel(bg='gray')
        #TODO pr que no reconoce las Control booleanas cdo de llama a una pagina inde[pendiente
        gd=ViewDrive(vd,main(),1)
        #gd=ViewDrive(raiz,None,1)
        gd.gui_butmenu()
        gd.gui_oferta_guardada()
        #gd.cambiartit()
        raiz2.mainloop()""" 
     
if __name__ == '__main__':
    #po = def __init__(self, idfreelancer, idsitio, sitio,idioma, tema, xdict, urlproy, tiplogin, nombusq,clavebusq,bd):
    import Freelancer20 as frl
    
    po=Busqproywin(1,2,'Workana',['English','Español','Português'],['Delphi','C++','Excel'],frl.xdict,'https://www.workana.com/jobs?ref=home_top_bar','Google','raulrfa@gmail.com','Karpov75%','freebd.db')
    #po = Preofertawin(None,None, None,None,None, 'freebd.db')
    

