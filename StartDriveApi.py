from __future__ import print_function
import pickle
import os.path
from io import StringIO, BytesIO
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import messagebox
# Carga ttk (para widgets nuevos 8.5+)
#from tkinter.filedialog import *
from tkinter import ttk as tk
from datetime import date
import pickle
from enumeradores import Idiomas
from preoferta import *
from estadistica2 import *
from datetime import datetime
import urllib.parse
import sqlite3 

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
# ['https://www.googleapis.com/auth/drive.metadata.readonly']


class ViewDrive(Frame):
    """Clase para visualizar la interfaz de Drive correspndiente al inicio de la vista"""
    def __init__(self,raiz,servicio,idiomadefecto):
        self.choice = IntVar()
        self.choice.set(idiomadefecto)
        self.search = StringVar()
        self.search.set('')
        self.titu = StringVar()
        self.titu.set('ESP')
        self.listfiles = StringVar()
        self.raiz= raiz
        self.servicio =servicio

        # Define las dimensiones de la ventana, que se ubicará en 
        # el centro de la pantalla. Si se omite esta línea la
        # ventana se adaptará a los widgets que se coloquen en
        # ella. 

        self.raiz.geometry('1600x600') # anchura x altura

        # Asigna un color de fondo a la ventana. Si se omite
        # esta línea el fondo será gris

        self.raiz.configure(bg = 'green')

        # Asigna un título a la ventana

        self.raiz.title('Analizador de ofertas')
        self.estadistica= None  #;a c;ase #stadisitica es none al principio
        
      
        # Frames asociadas a la raiz del documento

        self.frbutm = LabelFrame(self.raiz, bg='black', padx=2,pady =2, text ='Menu')
        self.frbutm.pack(side=LEFT, fill=Y)
        self.frlist = LabelFrame(self.raiz, bg='gray', padx=5,pady =5, text ='Selección de Ofertas Almacenadas')
        self.frlist.pack(side=LEFT, fill=Y)
        self.fredit = LabelFrame(self.raiz, bg='lightblue', padx=5,pady =5, text ='Edición del Documento')
        self.fredit.pack(side=LEFT, fill=Y)
        self.frcompose = LabelFrame(self.raiz, bg='yellow', padx=5,pady =5, text ='Composición del Docuento')
        self.frcompose.pack(side=LEFT, fill=Y)
        self.frcomposeredit=LabelFrame(self.raiz,name='' , bg='lightblue',padx=5,pady =5, text ='Preofertas en Base Datos')
        self.frcomposeredit.pack(side=LEFT,fill=Y)

        # frames para poner la fucionalidad del proyecto 

    def gui_butmenu(self):
        self.sbutmenu=tk.Style()
        self.sbutmenu.theme_use('clam')
        self.sbutmenu.configure('.',font='Times 12', foreground='yellow',background='blue',state=True)
        self.var_dash=IntVar()
        self.var_dash.set(1)
        self.cb_dashboard =tk.Checkbutton(self.frbutm, name='dash' ,text='Dash', variable=self.var_dash, state='disabled', command=self.cbclickp)
        self.cb_dashboard.grid(row=0,column=0)
        self.var_estad=IntVar()
        self.var_estad.set(0)
        self.cb_estad =tk.Checkbutton(self.frbutm,name='estad',text='Grid ', variable=self.var_estad,state='normal',command=self.cbclickp)
        self.cb_estad.grid(row=1, column=0, sticky=(W + E))
        self.var_sitios=IntVar()
        self.var_sitios.set(1)
        self.cb_sitios =tk.Checkbutton(self.frbutm, name='sitios' ,text='Esit', variable=self.var_sitios, state='disabled',command=self.cbclickp)
        self.cb_sitios.grid(row=2, column=0, sticky=(W + E))
        self.var_busq=IntVar()
        self.var_busq.set(1)
        self.cb_busq =tk.Checkbutton(self.frbutm, name='buscarsitios' ,text='Bsit', variable=self.var_busq,state='disabled', command=self.cbclickp)
        self.cb_busq.grid(row=3, column=0, sticky=(W + E))
        self.var_busqofer=IntVar()
        self.var_busqofer.set(1)
        self.cb_busqofer =tk.Checkbutton(self.frbutm, name='buscaroferta' ,text='Bofe', variable=self.var_busqofer,
        command= self.cbclickp)
        self.cb_busqofer.grid(row=4, column=0, sticky=(W + E))
        self.var_ediofer=IntVar()
        self.var_ediofer.set(1)
        self.cb_ediofer =tk.Checkbutton(self.frbutm, name='editarofer' ,text='Eofe',variable=self.var_ediofer, command=self.cbclickp)
        self.cb_ediofer.grid(row=5, column=0, sticky=(W + E))
        self.var_composer=IntVar()
        self.var_composer.set(1)
        self.cb_composer =tk.Checkbutton(self.frbutm, name='composer' ,text='Compo',variable=self.var_composer, command=self.cbclickp)
        self.cb_composer.grid(row=6, column=0, sticky=(W + E))
        self.var_config=IntVar()
        self.var_config.set(1)
        self.cb_config =tk.Checkbutton(self.frbutm, name='config' ,text='Conf', variable=self.var_config, command=self.cbclickp)
        self.cb_config.grid(row=9, column=0, sticky=(W + E))    
        
     

    def cbclickp(self): 
        list_frraiz_selec=[]

        #no se incuye en la lista ni el frmbutm ni ls disableds

        if self.cb_estad.instate(['selected','!disabled']):
            if self.estadistica==None:
                self.estadistica=Estadisticas(self.raiz,'freebd.db','ofertasrealizadas')          
            list_frraiz_selec.append(self.estadistica.fra)
        if self.estadistica!= None: self.estadistica.fra.pack_forget()
        if self.cb_busqofer.instate(['selected','!disabled']):
            list_frraiz_selec.append(self.frlist)
        self.frlist.pack_forget()
        if self.cb_ediofer.instate(['selected','!disabled']):
            list_frraiz_selec.append(self.fredit)
            self.fredit.pack(side=LEFT, fill=Y)
        self.fredit.pack_forget()
        if self.cb_composer.instate(['selected','!disabled']):
            list_frraiz_selec.extend([self.frcompose,self.frcomposeredit])  
        self.frcompose.pack_forget()
        self.frcomposeredit.pack_forget()

        for wfr in list_frraiz_selec:
            wfr.pack(side=LEFT, fill=Y)
       
        

        

    def gui_oferta_guardada(self):
        # Define la ventana izquierda de la aplicación
        self.frlistchoice0 = Frame(self.frbutm, bg='gray')
        self.frlistchoice0.grid(row=10,column=0,sticky=(W+E))
        self.frlistchoice1 = Frame(self.frlistchoice0, bg='gray') 
        self.frlistchoice1.pack(side=TOP, fill=Y)
        self.frlistchoice2 = Frame(self.frlistchoice1, bg='gray')
        self.frlistchoice2.pack(side=TOP, fill=Y)
        self.frlistchoice3 = Frame(self.frlistchoice2, bg='gray')
        self.frlistchoice3.pack(side=TOP, fill=Y)    
        self.rb_esp =Radiobutton(self.frlistchoice0, text='Esp', variable=self.choice, value=1,command=self.rbclick)
        self.rb_esp.pack(side=TOP)
        self.rb_eng =Radiobutton(self.frlistchoice0, text='Eng', variable=self.choice, value=2,command=self.rbclick)
        self.rb_eng.pack(side=TOP)
        self.rb_fra =Radiobutton(self.frlistchoice0, text='Fra', variable=self.choice, value=3,command=self.rbclick)
        self.rb_fra.pack(side=TOP)
        self.rb_por =Radiobutton(self.frlistchoice0, text='Por', variable=self.choice, value=4,command=self.rbclick)
        self.rb_por.pack(side=TOP)
        self.rb_ale =Radiobutton(self.frlistchoice0, text='Ale', variable=self.choice, value=5,command=self.rbclick)
        self.rb_ale.pack(side=TOP)
        self.rb_ita =Radiobutton(self.frlistchoice0, text='Ita', variable=self.choice, value=6,command=self.rbclick)
        self.rb_ita.pack(side=TOP)
        self.rb_rus =Radiobutton(self.frlistchoice0, text='Rus', variable=self.choice, value=7,command=self.rbclick)
        self.rb_rus.pack(side=TOP)
        self.rb_otr =Radiobutton(self.frlistchoice0, text='Otr', variable=self.choice, value=8,command=self.rbclick)
        self.rb_otr.pack(side=TOP)
        self.frsearchbox = Frame(self.frlist,bg='blue')
        self.frsearchbox.pack(side=TOP, fill=Y)
        self.texttit = Entry(self.frsearchbox , width=30, textvariable=self.titu)
        self.texttit.pack(side=TOP,fill=X,expand=1)
        self.textbody = Entry(self.frsearchbox , width=30, textvariable=self.search)
        self.textbody.pack(side=TOP,fill=X,expand=1)
        self.butcamb= Button(self.frsearchbox, text= ' CambiarTitulo',command=self.cambiartit)
        self.butcamb.pack(side=TOP)
        self.frlistfile=Frame(self.frlist,bg='blue')
        self.frlistfile.pack(side=TOP, fill=Y)
        self.lbfile = Listbox(self.frlistfile,exportselection=False,selectmode=SINGLE,listvariable=self.listfiles,width=30, height=100)
        self.lbfile.pack(side=LEFT,expand=1,fill=Y)
        if self.choice.get()!=0 :
            self.cambiartit()
        self.gui_editar_oferta()
        self.gui_componer_oferta()

        #for items in self.listfiles.get():
        #    self.lbfile.insert(END,items)
        #self.raiz.mainloop()
        #self.raiz.quit() 
        #
    def gui_editar_oferta(self):
        # Define la ventana izquierda de la aplicación
        #self.fredit.pack(side=LEFT, fill=Y)
        self.fredittext=Frame(self.fredit,bg='gray')
        self.fredittext.pack(side=TOP,fill=Y, expand=1)  
        self.freditfile=Frame(self.fredit,bg='gray')
        self.freditfile.pack(side=TOP)
        self.frbutedit=Frame(self.fredit,bg='gray')
        self.frbutedit.pack(side=TOP)
        self.text_edit = Text(self.fredittext,width=50,height=20,bg='white',fg='black')
        self.text_edit.bind('<Alt-Shift-KeyPress>',self.copyfromcomposer)
        self.text_edit.bind('<Alt-Control-KeyPress>',self.copytocomposer) 
        self.text_edit.bind('<ButtonRelease-3>',self.copiarselnew )       
        self.text_edit.pack(side=TOP,fill=Y,expand=1)
        self.text_filename=StringVar()
        self.text_name = Entry(self.freditfile,width=60,bg='white',fg='black',textvariable=self.text_filename)
        self.text_name.pack(side=TOP,fill=Y)    
        self.butcargar= Button(self.frbutedit, text= ' Cargar',command=self.cargar)
        self.butcargar.pack(side=LEFT, padx=10)
        self.butsalvar= Button(self.frbutedit, text= ' Salvar',command=self.salvar)
        self.butsalvar.pack(side=LEFT, padx=10)
        self.butcopiar= Button(self.frbutedit, text= ' Copiar',command=self.copiar)
        self.butcopiar.pack(side=LEFT, padx=10)
        self.butlimpiar= Button(self.frbutedit, text= ' Limpiar',command=self.limpiar)
        self.butlimpiar.pack(side=LEFT, padx=10)        
        self.butcomponer= Button(self.frbutedit, text= ' Componer',command=self.componer)
        self.butcomponer.pack(side=LEFT, padx=10)

    def copyfromcomposer(self, event):
        """"Copia desde (Alt-Left) y hacia el composer (Alt=Right)
            dependiendo de la tecla pasada va hacia ua edicion del composer dedicado"""
           
        if event.char   =='s' : 
            w=self.text_salu
        elif event.char =='p' : 
            w=self.text_pres
        elif event.char =='e' : w=self.text_expe
        elif event.char =='c' : w=self.text_cert   
        elif event.char =='d' : w=self.text_desp
        elif event.char =='x' : w=self.text_extra
        elif event.char =='r' : w=self.text_refe
        elif event.char =='p' : w=self.text_pres
        elif event.char =='t' : w=self.text_todo
        else:
            return

        self.text_edit.insert(CURRENT,w.get('1.0',END),w._name)
        self.text_edit.tag_configure(w._name,background=w['background'])

        

    def copytocomposer(self, event):
        """"Copia desde (Alt) y hacia el composer (Ctrl-Alt)
            dependiendo de la tecla pasada va hacia ua edicion del cmposer dedicado"""
        
        if event.char   =='s' : 
            w=self.text_salu
        elif event.char =='p' : 
            w=self.text_pres
        elif event.char =='e' : w=self.text_expe    
        elif event.char =='d' : w=self.text_desp
        elif event.char =='c' : w=self.text_cert            
        elif event.char =='x' : w=self.text_extra
        elif event.char =='r' : w=self.text_refe
        elif event.char =='p' : w=self.text_pres
        elif event.char =='t' : w=self.text_todo
        else:
            return
        copy = self.text_edit.selection_get()
        if copy!='':
            w.insert('1.0',copy)
        else:
            messa=messagebox.showwarning("Advertencia","No tiene texto seleccionado")                
       


    def cargar(self):
        # using Drive API v3; if using v2, change 'pageSize' to 'maxResults',
        # 'name=' to 'title=', and ".get('files')" to ".get('items')"   
        filename=self.lbfile.curselection()
        MIME = 'text/plain'
        if self.lbfile.get(filename)!= "":
            if self.text_filename.get()=='':
                self.text_filename.set(self.lbfile.get(filename)+' *') 
            else:
                self.text_filename.set(self.text_filename.get()+ ' + '+self.lbfile.get(filename)) 
            ind = self.lbfile.curselection()
            id = self.indices[ind[0]]
            res = self.servicio.files().export(fileId=id, mimeType=MIME).execute()
            if res:
                self.text_edit.insert(END,(res.decode('utf-8')))
                # decode bytes for Py3; NOP for Py2

    def salvarpru(self):
        """
        file_metadata = {'name': 'Esp Delphi, RMA qq.txt',
                         'mimeType': 'application/vnd.google-apps.document',}
        media = MediaFileUpload('Esp Delphi, RMA qq.txt',
                          mimetype='text/plain',
                          resumable=True)
        file = self.servicio.files().create(body=file_metadata,
                                    media_body=media,
                                    ).execute()"""
        #self.text_filename.set('File ID: %s' % file.get('id'))     
        #response = urllib2.urlopen(url)
                 

    def salvar(self):
        staux=self.text_filename.get()
        if "+" in staux or "*" in staux:
           #mess=Message(self.fredittext,bg='gray',text="Revise en el nombre de fichero con caracteres no permitidos")
           #mess.place(relx=0.5,rely=0.5)
           messagebox.answer = messagebox.askyesnocancel("Revise en el nombre de fichero con caracteres * al final","¿Cambio automatico por la fecha de hoy o procede manuamente?")
           if messagebox.answer==True:
               self.text_filename.set(staux[0:-1] +' ' + str(datetime.today().date().strftime('%d/%m/%Y')))
           else:   
               return    
        fh = BytesIO(bytearray(self.text_edit.get("1.0",END),'utf-8'))
        media_body = MediaIoBaseUpload(fh, mimetype='text/plain',
                    chunksize=1024*1024, resumable=True)
        body = {
                'name': self.text_filename.get(),
                'mimeType': 'application/vnd.google-apps.document'
            }
        self.servicio.files().create(body=body, media_body=media_body).execute()  
        #mess=Message(text='File ID: %s' % file.get('id'))
    def copiar(self):
        clip = Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(self.text_edit.get('1.0',END) )  # Change INFO_TO_COPY to the name of your data source
        clip.destroy()

    def limpiar(self):
        self.text_edit.delete('1.0',END)
        self.text_filename.set('')

    def componer(self):pass
    
    def gui_componer_oferta(self):
        self.frcomposesalu=Frame(self.frcompose,name='salu' , bg='gray')
        self.frcomposesalu.pack(side=TOP,fill=Y, expand=1)  
        self.frcomposepresenta=Frame(self.frcompose,name='pres' , bg='gray')
        self.frcomposepresenta.pack(side=TOP,fill=Y, expand=1)
        self.frcomposecerti=Frame(self.frcompose,name='cert' , bg='gray')
        self.frcomposecerti.pack(side=TOP,fill=Y, expand=1)  
        self.frcomposeexpe=Frame(self.frcompose,name='expe' , bg='gray')
        self.frcomposeexpe.pack(side=TOP,fill=Y, expand=1)
        self.frcomposerefe=Frame(self.frcompose,name='refe' , bg='gray')
        self.frcomposerefe.pack(side=TOP,fill=Y, expand=1)  
        self.frcomposextras=Frame(self.frcompose,name='extr' , bg='gray')
        self.frcomposextras.pack(side=TOP,fill=Y, expand=1)
        self.frcomposedesp=Frame(self.frcompose,name='desp' , bg='gray')
        self.frcomposedesp.pack(side=TOP,fill=Y, expand=1)
        self.frcomposertodo=Frame(self.frcompose,name='todo' , bg='gray')
        self.frcomposertodo.pack(side=TOP,fill=Y, expand=1)
        self.frbutcomp=Frame(self.frcompose,name='' , bg='gray')
        self.frbutcomp.pack(side=BOTTOM)

        #ListBox editor se edita en frcomoseredit

       
        self.frbutcomp2=Frame(self.frcomposeredit,name='' , bg='gray')
        self.frbutcomp2.pack(side=TOP)
        self.choicefil=StringVar()
        self.rb_filtro =Radiobutton(self.frbutcomp2, text='Filtro', variable=self.choicefil, value='filtro')
        self.rb_filtro.pack(side=LEFT)
        self.rb_filtro.bind('<Button-1>',self.cambiarquery)
        self.rb_body =Radiobutton(self.frbutcomp2, text='Cuerpo', variable=self.choicefil, value='body')
        self.rb_body.pack(side=LEFT)
        self.rb_filtro.bind('<Button-1>',self.cambiarquery)
        self.choicefil.set('body')
        self.text_filtercomp=StringVar()
        self.filtercomp = Entry(self.frbutcomp2,width=50,bg='white',fg='black',textvariable=self.text_filtercomp)
        self.filtercomp.pack(side=LEFT,fill=X, expand=1)
        self.butfiltrar=IntVar(0)
        self.butt_filtrar=tk.Checkbutton(self.frbutcomp2, text= 'Filtrar',variable=self.butfiltrar)
        self.butt_filtrar.bind('<ButtonRelease-1>',self.cambiarquery)
        self.butt_filtrar.pack(side=LEFT)
        self.var_lbfiltro=StringVar()
        self.lbfiltro =Listbox(self.frcomposeredit,exportselection=False,selectmode=SINGLE,listvariable=self.var_lbfiltro,width=250, height=10)
        self.lbfiltro.pack(side=TOP,expand=1,fill=Y)
        
        self.editactual= Text(self.frcomposeredit,width=250,height=8,bg='white',fg='black')
        self.editactual.pack(side=TOP,expand=1,fill=Y)
        self.var_lbcomposer=StringVar()
        self.lbcomposer = Listbox(self.frcomposeredit,exportselection=False,selectmode=SINGLE,listvariable=self.var_lbcomposer,width=250, height=40)
        self.lbcomposer.pack(side=TOP,expand=1,fill=Y)
        self.lbcomposer.bind('<Double-Button-1>', self.copiarbody)
        self.lbcomposer.bind('<ButtonRelease-1>', self.muestraactual)
        self.lbcomposer.bind('<ButtonRelease-3>', self.copiarbodynew)
        

    
        # multiline text para cada uno de los textos
        self.widgeact=None
        self.text_salu = Text(self.frcomposesalu,width=40,height=3,bg='white',fg='black')

        self.text_salu.pack(side=LEFT,fill=Y,expand=1)
        self.butt_salu= Button(self.frcomposesalu, text= 'salu',bg='white')
        self.butt_salu.bind('<Button-1>',self.cambiarquery)
        self.butt_salu.pack(side=LEFT)
        self.text_pres = Text(self.frcomposepresenta,width=40,height=3,bg='light yellow',fg='black')
        self.text_pres.pack(side=LEFT,fill=Y,expand=1)
        self.butt_pres= Button(self.frcomposepresenta, text= 'pres',bg='light yellow')
        self.butt_pres.bind('<Button-1>',self.cambiarquery)
        self.butt_pres.pack(side=LEFT)
        self.text_cert = Text(self.frcomposecerti,width=40,height=3,bg='light green',fg='black')
        self.text_cert.pack(side=LEFT,fill=Y,expand=1)
        self.butt_cert= Button(self.frcomposecerti, text= 'cert',bg='light green')
        self.butt_cert.bind('<Button-1>',self.cambiarquery)
        self.butt_cert.pack(side=LEFT)
        self.text_expe = Text(self.frcomposeexpe,width=40,height=3,bg='light yellow',fg='black')
        self.text_expe.pack(side=LEFT,fill=Y,expand=1)
        self.butt_expe= Button(self.frcomposeexpe, text= 'expe',bg='light yellow')
        self.butt_expe.bind('<Button-1>',self.cambiarquery)
        self.butt_expe.pack(side=LEFT)
        self.text_refe = Text(self.frcomposerefe,width=40,height=3,bg='light salmon',fg='black')
        self.text_refe.pack(side=LEFT,fill=Y,expand=1)
        self.butt_refe= Button(self.frcomposerefe, text= 'refe')
        self.butt_refe.bind('<Button-1>',self.cambiarquery)
        self.butt_refe.pack(side=LEFT)
        self.text_extra = Text(self.frcomposextras,width=40,height=3,bg='light pink',fg='black')
        self.text_extra.pack(side=LEFT,fill=Y,expand=1)
        self.butt_extra= Button(self.frcomposextras, text= 'extra',bg='light pink')
        self.butt_extra.bind('<Button-1>',self.cambiarquery)
        self.butt_extra.pack(side=LEFT)
        self.text_desp = Text(self.frcomposedesp,width=40,height=3,bg='light cyan',fg='black')
        self.text_desp.pack(side=LEFT,fill=Y,expand=1)
        self.butt_desp= Button(self.frcomposedesp, text= 'desp',bg='light cyan')
        self.butt_desp.bind('<Button-1>',self.cambiarquery)        
        self.butt_desp.pack(side=LEFT)
        self.text_todo = Text(self.frcomposertodo,width=40,height=3,bg='light coral',fg='black')
        self.text_todo.pack(side=LEFT,fill=Y,expand=1)        
        self.butt_todo = Button(self.frcomposertodo, text= 'todo',bg='light coral')
        self.butt_todo.bind('<Button-1>',self.cambiarquery)
        self.butt_todo.pack(side=LEFT)        

 
        # checkbuttons que controla el compsitor

        self.var_saludo=IntVar()
        self.var_saludo.set(1)

        self.cb_saludo =tk.Checkbutton(self.frbutcomp, name='salu' ,text='Saludo   ', variable=self.var_saludo, command=self.cbclick)
        self.cb_saludo.grid(row=0,column=0)
        self.var_present=IntVar()
        self.var_present.set(1)
        self.cb_present =tk.Checkbutton(self.frbutcomp,name='pres',text='Presentación ', variable=self.var_present, command=self.cbclick)
        self.cb_present.grid(row=0, column=1, sticky=(W + E))
        self.var_certi=IntVar()
        self.var_certi.set(1)
        self.cb_certi =tk.Checkbutton(self.frbutcomp, name='cert' ,text='Certificaciones ', variable=self.var_certi,  command=self.cbclick)
        self.cb_certi.grid(row=0, column=2, sticky=(W + E))
        self.var_expe=IntVar()
        self.var_expe.set(1)
        self.cb_expe =tk.Checkbutton(self.frbutcomp, name='expe' ,text='Experiencia', variable=self.var_expe, command=self.cbclick)
        self.cb_expe.grid(row=0, column=3, sticky=(W + E))
        self.var_refe=IntVar()
        self.var_refe.set(1)
        self.cb_refe =tk.Checkbutton(self.frbutcomp, name='refe' ,text='Referencia ', variable=self.var_refe,command=self.cbclick)
        self.cb_refe.grid(row=1, column=0, sticky=(W + E))
        self.var_extras=IntVar()
        self.var_extras.set(1)
        self.cb_extras =tk.Checkbutton(self.frbutcomp, name='extr' ,text='Extras', variable=self.var_extras, command=self.cbclick)
        self.cb_extras.grid(row=1, column=1, sticky=(W + E))
        self.var_despe=IntVar()
        self.var_despe.set(1)
        self.cb_despe =tk.Checkbutton(self.frbutcomp, name='desp' ,text='Despedida', variable=self.var_despe, command=self.cbclick)
        self.cb_despe.grid(row=1, column=2, sticky=(W + E))
        self.var_todo=IntVar()
        self.var_todo.set(1)
        self.cb_todo =tk.Checkbutton(self.frbutcomp, name='todo' ,text='Todas', variable=self.var_todo, command=self.cbclick)
        self.cb_todo.grid(row=1, column=3, sticky=(W + E))

    def muestraactual(self,event):
        self.editactual.delete(END)
        val= self.lbcomposer.get(ACTIVE)
        self.editactual.insert(END,val)


        
    def cbclick(self):
        countpacked=0
        childrens = 0
        listwfrsel=[]
        
        for w in self.frbutcomp.children.values():
            #self.lbcomposer.insert(END,w._name) 
            childrens+=1
            for wfr in self.frcompose.children.values():
                if wfr._name==w._name:
                    wfr.pack_forget()
                    if w.instate(['selected']): 
                        countpacked+=1
                        listwfrsel.append(wfr)                                      
        if countpacked==0:
            return
        else:    
            nuevaaltura=32//countpacked
        for wfr in listwfrsel:              
            wfr['height']=nuevaaltura
            wfr.pack(side=TOP,fill=Y, expand=1)
            
                            
    def copiarbodynew(self,event):        
        body=self.lbcomposer.get(self.lbcomposer.curselection()[0])
        id=self.listrec[self.lbcomposer.curselection()[0]][0]
        tema=self.listrec[self.lbcomposer.curselection()[0]][2]
        filtro=self.listrec[self.lbcomposer.curselection()[0]][3]
        lenguaje=self.listrec[self.lbcomposer.curselection()[0]][1]
        po = Preofertawin(id,lenguaje, tema,filtro,body, 'freebd.db') 
        self.cambiarquery(event)  

    def copiarselnew(self,event):
        if event.widget == self.text_edit and self.text_edit.selection_get()!='':
            po = Preofertawin(None,None, None,self.text_filename.get(),self.text_edit.selection_get(), 'freebd.db')
            po.butsalvar.config(state = DISABLED)




    def copiarbody(self,event):
        val=self.lbcomposer.get(self.lbcomposer.curselection()[0])
        for w in self.widgeact.master.children.values():
            if type(w) is Text:
                w.insert(END,val)
                break



    def cambiarquery(self,event): 
        """" Cambia la query funcional. Puede ser llamado por los btoes del composer o por el radio
        buttoon del filtro de busqueda en este caso no puede ser cambiado el widgeatualct. Tampco si es e  buton de fitrar"""
        if type(event.widget) is Button and event.widget!=self.butt_filtrar:
            event.widget.master['height']=8
            event.widget['height']=4
            if self.widgeact!=None:
                self.widgeact.master['height']=4
                self.widgeact['height']=2
            self.widgeact=event.widget
        elif self.widgeact is None :
            return # si se da primero al RadioButton daba un error!
        db = sqlite3.connect('freebd.db')
        curs = db.cursor()
        # En el filtro debiera ser distinct en el body todos
        query =" SELECT DISTINCT filtro FROM composer WHERE lenguaje = '{}' and tema= '{}'".format(Idiomas(self.choice.get()).name[0:3].upper(), self.widgeact['text'],)
        # query = query + " and tema = "+ 
        if self.choicefil.get()=='filtro' and self.butfiltrar.get()==1 and self.text_filtercomp.get() !='':
            query = query + " and filtro = '{}'".format(self.text_filtercomp.get())
        curs.execute(query)
        listres=curs.fetchall()
        self.lbfiltro['height']=len(listres)
        self.var_lbfiltro.set(listres)
        query =" SELECT  id, lenguaje, tema,filtro, body  FROM composer WHERE lenguaje = '{}' and tema= '{}'".format(Idiomas(self.choice.get()).name[0:3].upper(), self.widgeact['text'],)
        # query = query + " and tema = "+ 
        if self.choicefil.get()=='body' and self.butfiltrar.get()==1 and self.text_filtercomp.get() !='':
            query = query + " and '{}' in body".format(self.text_filtercomp.get())
        curs.execute(query)
        listres=curs.fetchall()
        curs.close
        self.listrec = listres
        self.var_lbcomposer.set([item[4] for item in listres])
        return query
        
          
        

    def cambiartit(self):
        #self.search.set(self.titu.get())
        self.topic=self.titu.get().split()
        query=''
        for items in self.topic:
            query=query + "name contains "+chr(39)+ items +chr(39)+ " and "
        quitaand = len(query)
        query=query[0:quitaand-5]
        self.topic=self.search.get().split()
        querycont=''
        for items in self.topic:
            querycont=querycont + "fullText contains "+chr(39)+ items +chr(39)+ " and "
        quitaand = len(querycont)
        querycont=querycont[0:quitaand-5]
        #querycont= chr(34)+ querycont + chr(34)
        if query!="" and querycont!="":
            query=query+' and '+ querycont
        elif query=="": query = querycont
        # si el titulo esta vacio se hace la query con el contenido,di ningun con la suma, si el contenido
        # esta vacio se queda la query solo con el titulo
        #query="name contains 'ESP' and fullText contains 'Python'"
        #self.search.set(query)
        #query =urllib.parse.quote_plus(query)
        results = self.servicio.files().list(q=query,
            pageSize=80, fields="nextPageToken, files(name, id)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            self.listfiles.set([elem['name'] for elem in items])
            self.indices =[elem['id'] for elem in items]
        
    def rbclick(self):
       if self.choice.get() in range(1,8):# rango termina de 1 a 7
          self.titu.set((Idiomas(self.choice.get()).name)[0:3].upper()) 
       else:
          self.titu.set('')
       varP =self.titu.get()


def query_api_items(service,query):
    # return service
    # Decklaracion de variables para Tkinter 
    # Call the Drive v3 API
    
    results = service.files().list(q=query,
            pageSize=8, fields="nextPageToken, files(name, id)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        #listfiles.set(items)
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    return items 

   
def main():
    """Shows basic usage of the Drive v3 API.Prints the names and ids of the first 10 files 
    the user has access to."""
 
    
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
    service = build('drive', 'v3', credentials=creds)
    #query="name contains 'ESP'"
    #query_api_items(service,query)
    return service    

if __name__ == '__main__':
    
    raiz = Tk()
    #main()
    gd=ViewDrive(raiz,main(),1)
    gd.gui_butmenu()
    gd.gui_oferta_guardada()
    #gd.cambiartit()
    raiz.mainloop()