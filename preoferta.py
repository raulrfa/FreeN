from tkinter import *
from tkinter import messagebox
from enumeradores import Idiomas
from sqlite3 import *

class Preofertawin:

    def __init__(self, id, idioma, tema, filtro, body,bd):
        """ Ventana flotante para editar coverofertas y poder rectificarla t y salvarla a
        la base de datos."""
        self.id = id
        self.lenguaje = idioma
        self.tema = tema
        self.body = body       
        self.raiz = Tk()
        self.filtro = filtro
        self.var_filtro = StringVar()
        self.var_filtro.set(filtro)
        # Define las dimensiones de la ventana, que se ubicará en 
        # el centro de la pantalla. Si se omite esta línea la
        # ventana se adaptará a los widgets que se coloquen en
        # ella. 
        # todo: gewwn 
        #  esta feo

        self.raiz.geometry('900x400') # anchura x altura

        # Asigna un color de fondo a la ventana. Si se omite
        # esta línea el fondo será gris

        self.raiz.configure(bg = 'cyan')

        # Asigna un título a la ventana

        self.raiz.title('Editor de preofertas: ' + str(self.id) )
        
        # Define un botón en la parte inferior de la ventana
        # que cuando sea presionado hará que termine el programa.
        # El primer parámetro indica el nombre de la ventana 'raiz'
        # donde se ubicará el botón
        self.muestraforma()
        self.raiz.mainloop()

    def muestraforma(self):

        self.frmenubut = LabelFrame(self.raiz, bg='black', padx=2,pady =2, text ='Menu')
        self.frmenubut.pack(side=BOTTOM, fill=Y)
        self.frcompose = LabelFrame(self.raiz, bg='yellow', padx=5,pady =5, text ='Edición del Documento')
        self.frcompose.pack(side=BOTTOM, fill=Y,expand=1)
        self.frlist = LabelFrame(self.frcompose, bg='gray', padx=5,pady =5, text ='Idioma/Tema')
        self.frlist.pack(side=LEFT, fill=Y)
        self.fredit = LabelFrame(self.frcompose, bg='lightblue', padx=5,pady =5, text ='Edición del Documento')
        self.fredit.pack(side=LEFT, fill=Y)
        self.text_edit = Text(self.fredit,width=100,height=20,bg='white',fg='black')
        #self.text_edit.bind('<Alt-KeyPress>',self.copyfromcomposer)
        self.text_edit.pack(side=TOP,fill=Y,expand=1)
        if self.body!=None:
            self.text_edit.insert(END,self.body)
        self.lbidio = Listbox(self.frlist,exportselection=False,selectmode=SINGLE,width=8, height=100)
        self.lbidio.pack(side=LEFT,expand=1,fill=Y)
        for i in range (1,8): self.lbidio.insert(END,Idiomas(i).name[0:3].upper())
        if self.lenguaje!=None:
            self.lbidio.selection_set(self.lbidio.get(0,END).index(self.lenguaje))    
        self.var_tema=StringVar()
        listatema=['salu','pres', 'expe', 'cert', 'refe', 'extras', 'desp','todo']
        #self.var_tema.set(listatema)
        self.lbtema = Listbox(self.frlist,exportselection=False,selectmode=SINGLE,listvariable=self.var_tema,width=8, height=100)
        for item in listatema:
             self.lbtema.insert(END,item)
        self.lbtema.pack(side=LEFT,expand=1,fill=Y)
        #self.var_tema.set(['salu','pres', 'expe', 'cert', 'refe', 'extras', 'desp','todo'])
        if self.tema!=None:
            self.lbtema.selection_set(self.lbtema.get(0,END).index(self.tema))
        self.lab_filtro =Label(self.frmenubut,text='Filtrar por:')
        self.lab_filtro.pack(side=LEFT)
        self.edit_filtro = Entry(self.frmenubut,textvariable=self.var_filtro,width=60,bg='white',fg='black')
        if self.filtro!=None:
            self.edit_filtro.insert(0,self.filtro)
        self.edit_filtro.pack(side=LEFT,fill=Y)  
        self.butcargar= Button(self.frmenubut, text= ' Crear Nuevo',command=self.salvarcomo)
        self.butcargar.pack(side=LEFT, padx=10)
        self.butsalvar= Button(self.frmenubut, text= ' Salvar',command=self.salvar)
        self.butsalvar.pack(side=LEFT, padx=10)
        self.butcopiar= Button(self.frmenubut, text= ' Copiar',command=self.copiar)
        self.butcopiar.pack(side=LEFT, padx=10)
        self.butlimpiar= Button(self.frmenubut, text= ' Limpiar',command=self.limpiar)
        self.butlimpiar.pack(side=LEFT, padx=10)        
        self.butcomponer= Button(self.frmenubut, text= ' Componer',command=self.componer)
        self.butcomponer.pack(side=LEFT, padx=10)

    def salvarcomo(self):
        try:
            db = connect('freebd.db')
            curs = db.cursor()
            lan= self.lbidio.get(self.lbidio.curselection()[0])
            tem=self.lbtema.get(self.lbtema.curselection()[0])
            fil=self.var_filtro.get()
            update = "INSERT INTO composer values('{}', '{}', '{}', '{}',{}) ".format(lan,tem,fil,self.text_edit.get('1.0',END),'NULL')
            print(update)
            self.id=curs.execute(update).lastrowid
            self.butsalvar.state=NORMAL
            curs.close
            db.commit()
        except  DatabaseError:
           messa=messagebox.showwarning( 'Error en la base de datos')


    def salvar(self):
       try: 
            db = connect('freebd.db')
            curs = db.cursor()
            lan= self.lbidio.get(self.lbidio.curselection()[0])
            tem=self.lbtema.get(self.lbtema.curselection()[0])
            fil=self.var_filtro.get()
            update = "UPDATE composer SET lenguaje= '{}', tema= '{}', filtro= '{}', body = '{}' WHERE id={} ".format(lan,tem,fil,self.text_edit.get('1.0',END),self.id)
            curs.execute(update)
            curs.close
            db.commit()
       except  DatabaseError:
            messa=messagebox.showwarning( 'Error en la base de datos')



    def componer(self):
        pass
    def copiar(self):
        clip = Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(self.text_edit.get('1.0',END) )  # Change INFO_TO_COPY to the name of your data source
        clip.destroy()

    def limpiar(self):
        self.text_edit.delete('1.0',END)
     
if __name__ == '__main__':
    #po = Preofertawin(19,'ENG', 'salu','general','Hello, Hope you are doing well!', 'freebd.db')
    po = Preofertawin(None,None, None,None,None, 'freebd.db')

