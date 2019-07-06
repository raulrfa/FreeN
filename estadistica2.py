from tkinter import *
from tkinter import ttk as tk
from tkinter import messagebox
#from tkintertable.Tables import TableCanvas
from tkintertable import TableCanvas, TableModel
import sqlite3 

class Estadisticas(Frame):
    def __init__(self, raiz, bd, tabimp):
        self.raiz=raiz
       
        self.tabimp=tabimp
        db = sqlite3.connect(bd)
        self.curs = db.cursor()
        self.fra = LabelFrame(self.raiz , bg='yellow', padx=5,pady =5, text ='Estadisticas Ofertas realizadas')
        self.fra.pack(side=LEFT, fill=Y,expand=1)
        self.guia= Frame(self.fra)
        self.guia.pack(side=TOP)
        self.var_query=StringVar()
        self.nombre = tk.Combobox(self.guia,width=30,height=4, textvariable=self.var_query)
        self.nombre['values']=self.curs.execute("Select name FROM querys").fetchall()
        self.nombre.bind("<<ComboboxSelected>>", self.TextBoxUpdate)
        #TODO:separate functionality

        if self.tabimp!='' : 
            self.var_query.set(self.tabimp)
        self.nombre.pack(side=LEFT)
        self.var_sql=StringVar()
        self.sql= Entry(self.guia, width=50, bg='cyan', textvariable=self.var_sql)
        self.sql.bind('<Return>',self.muestradatos)
        self.sql.pack(side=LEFT)
        self.butsalvar= Button(self.guia, text= ' Salvar',command=self.salvar)
        self.butsalvar.pack(side=LEFT, padx=10)
        self.frtab=Frame(self.fra)
        self.frtab.pack(side=TOP)
        self.var_query.set('querys')
        self.var_sql.set('SELECT * FROM querys')
        self.muestradatos(None) 
        #TODO: foo
        # todo: liat




        
    def TextBoxUpdate(self,event):
        try:
            sql = "SELECT sql FROM querys  WHERE name='{}'".format(self.var_query.get())
            sqlfilt= self.curs.execute(sql).fetchone()
            self.var_sql.set(sqlfilt[0])
            self.muestradatos(None)
        except  sqlite3.DatabaseError:
            messa=messagebox.showwarning( 'Error en la base de datos')


    def muestradatos(self,event):
       model = TableModel()
       self.curs.execute(self.var_sql.get())
       output = self.curs.fetchall() #output from query
       columns = [description[0] for description in self.curs.description]
       output_dict = {}
       for index in range(len(output)): #use an index to create new dictionary elements
            data = output[index] #use that index to find the next piece of data to insert into output dictionary
            dictrecord={}
            for  indcol  in range(len(columns)):
                dictrecord[columns[indcol]]=data[indcol]
            output_dict[index]=dictrecord    
            #create new dictionary element, using 
            #the index as the key and setup a nested dictionary as the value associated with the key
       table = TableCanvas(self.frtab,data=output_dict,width=600,height=300)
       table.show()

    def salvar(self):
       try:             
            update = "INSERT INTO querys SET name= '{}', sql= '{}' ".format(self.var_query.get(),self.var_query.get())#,self.id)
            self.curs.execute(update)
            #db.commit()
       except  sqlite3.DatabaseError:
            messa=messagebox.showwarning( 'Error en la base de datos')


if __name__ == '__main__':
     raiz = Tk()
     b=Estadisticas(raiz,'freebd.db','ofertasrealizadas')
     #b.muestradatos()
     raiz.mainloop()

     