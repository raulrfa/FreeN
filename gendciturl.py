from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox
from tkinter import filedialog                
from enum import Enum
from sqlite3 import *
from sitio_backend import *
from proyecto import Proyecto
import dictsit
from StartDriveApi import *
import LabelInput as li
from busqproy import Busqproywin as bp
import dictsit as di
from datetime import date
import importlib
import io
from contextlib import redirect_stderr, redirect_stdout
from os import path



tipstruct= Enum('tipstruct', 'rec dicto dictgen')
class dictofindsel:
    def __init__(self,sitio,url,dictini,xdictedit,tipstruct,marked=[]):
        self.raiz=Tk()
        self.sitio = StringVar()
        self.sitio.set(sitio)
        self.url= StringVar()
        self.url.set(url)
        self.dictini=dictini
        self.dictbase= StringVar()
        self.dictbase.set(dictini['sitio'])
        self.tipstruct = StringVar()
        self.tipstruct.set(tipstruct)
        self.newattr=None
        self.modifiedkey=marked
        self.basechanged= False
        #self.nomstruct= StringVar()
        #self.nomstruct= nomstruct.set(nomstuct)

        self.raiz.configure(bg='gray')
        self.raiz.title('Generador de diccionario de  busquedas: ' + str(self.sitio) )       
        w = self.raiz.winfo_screenwidth()/1.8
        h = self.raiz.winfo_screenheight()
        self.raiz.geometry("%dx%d+0+0" % (w, h))
        if isinstance(xdictedit,dict):
            self.xdictedit=xdictedit
            self.baseedit=True
        else:
            self.baseedit=False
        self.creaframes()
        self.muestraenc()       
        self.lastpos=self.muestra_proy(True,2,18)
        self.raiz.mainloop()

    def creaframes(self):        
        self.frlistenc=Frame(self.raiz, bg='gray') # internal frame to fothet
        self.frlistenc.pack(side=LEFT, fill=Y)
        self.fredit = Frame(self.raiz, bg='lightblue', padx=5,pady =5)
        self.fredit.pack(side=LEFT, fill=Y)
        self.frlistbut=Frame(self.raiz,bg='gray')
        self.frlistbut.pack(side=LEFT)
    
    def ponnum(self,event):
        if event.char in {'1','2','3','4','5','6','7','8','9'}: 
            self.numcoma.set(event.char)
        elif event.keysym=='Up': 
            print('up')
            up=self.numcoma.get()+1
            self.numcoma.set(up)
        elif event.keysym=='Down': self.numcoma.set(self.numcoma.get()-1)

    def muestraenc(self):
        li.LabelInput(self.frlistenc,'Sitio', width=30,input_var=self.sitio).grid(row=1,column=1,columnspan=2)
        li.LabelInput(self.frlistenc,"URL de Analisis", input_var=self.url).grid(row=2,column=1,columnspan=2)
        
        #li.LabelInput(self.frlistenc,'Nombrestruct', input_var=self.nomstruct).grid(row=4,column=1)
        li.LabelInput(self.frlistenc,'Diccionario Base', input_var=self.dictbase).grid(row=3,column=1,columnspan=2)
        li.LabelInput(self.frlistenc,'Tipo de Estructura', input_var=self.tipstruct).grid(row=4,column=1,columnspan=2)

        self.text_edit = Text(self.frlistenc,width=30,bg='white',fg='black')
        #self.text_edit.bind('<Alt-KeyPress>',self.copyfromcomposer)
        self.text_edit.grid(row=20,column= 1,columnspan=2)
        self.text_edit.insert((END),str(self.dictini))
        self.btnchangebase= Button(self.frlistenc,text='Change Base',command=self.changebase)
        self.btnchangebase.grid(row=5,column=1)
        self.btnchangeatr= Button(self.frlistenc,text='Change Attr',command=self.changeatr)
        self.btnchangeatr.grid(row=5,column=2)

        self.btngenerate= Button(self.frlistenc,text='Generate',command=self.generate)
        self.btngenerate.grid(row=6,column=1)
        self.btnclean= Button(self.frlistenc,text='Clean',command=self.cleanall)
        self.btnclean.grid(row=6,column=2)
        self.btncopy= Button(self.frlistenc,text='Copy',command=self.copy)
        self.btncopy.grid(row=7,column=1)
        self.numcoma=IntVar()
        self.numcoma.set(3)
        self.labelnum=Entry(self.frlistenc,textvar=self.numcoma,width=8)
        self.labelnum.grid(row=7,column=2)
        #self.labelnum.bind_all('<Alt-KeyPress-uparrow>',lambda e: self.numcoma.set(self.numcoma.get()+1))
        #self.labelnum.bind_all('<Alt-KeyPress-downarrow>',lambda e: self.numcoma.set(self.numcoma.get()-1))
        self.labelnum.bind_all('<Alt-KeyPress>', self.ponnum)
        #self.labelnum.bind_all('<Alt-KeyPress>',lambda e : if e.char in {'1','2','3','4','5','6','7','8','9'}: self.numcoma.set(e.char))
        # if e.char in {'1','2','3','4','5','6','7','8','9'})
        self.btncopyuntil= Button(self.frlistenc,text='CopyUntil',command=self.copyuntil)
        self.btncopyuntil.grid(row=8,column=1)
        self.btnlast= Button(self.frlistenc,text='CopyLast',command=self.copylast)
        self.btnlast.grid(row=8,column=2)
        self.btnone= Button(self.frlistenc,text='CopyOne',command=self.generate)
        self.btnone.grid(row=9,column=1)
        self.btnmark= Button(self.frlistenc,text='Mark',command=self.mark)
        self.btnmark.grid(row=9,column=2)
        self.btnunmark= Button(self.frlistenc,text='UnMark',command=self.unmark)
        self.btnunmark.grid(row=11,column=1)
        self.btnunmarkall= Button(self.frlistenc,text='UnMark All',command=self.unmarkall)
        self.btnunmarkall.grid(row=11,column=2)
        self.btnnewatr= Button(self.frlistenc,text='New Attribute',command=self.newattribute)
        self.btnnewatr.grid(row=12,column=1)
        self.btnsaveatr= Button(self.frlistenc,text='Save New',command=self.savenew)
        self.btnsaveatr.grid(row=12,column=2)
        
        self.btnpartial= Button(self.frlistenc,text='Load Partial',command=self.editparcial)
        self.btnpartial.grid(row=13,column=1)
        self.btnproof= Button(self.frlistenc,text='Proof',command=self.proof)
        self.btnproof.grid(row=13,column=2)


    def changebase(self):
        filepath=filedialog.askopenfilename(defaultextension='py',title='Abrir fichero base')
        pathfile=path.dirname(filepath)
        files=path.basename(filepath)
        filename=path.splitext(files)[0]
        fp=importlib.import_module(filename)
        self.dictini=fp.xdict
        self.raiz.title = "Fichero base "+ filename
        self.basechanged=True
        self.muestra_proy(True,2,16)

        

    def mark(self):
        if self.key not in self.modifiedkey:
            self.dictout[self.key].mark('cyan')
            self.modifiedkey.append(self.key)
            self.widget['background']='cyan'            
        else:        
            exit


    def unmark(self):
        if self.key not in self.modifiedkey:
            exit
        else:        
            self.dictout[self.key].mark('white')
            self.modifiedkey.remove(self.key)

    def unmarkall(self):
        for key in self.modifiedkey:       
            self.dictout[key].mark('white')
            self.modifiedkey.remove(key)


    def editparcial(self):
        file=filedialog.askopenfilename(defaultextension='txt',title='Abrir fichero a editar')
        self.raiz.title = "Edicion de fichero parcial "+ file
        with open (file, mode='r') as f:
            numprocesadas=numnoprocesadas=0
            st=f.readline()
            while st!='':
                val1=st.find('[',0)
                val2=st.find(']',0)
                val3=st.find('=',0)
                print(st,val1,val2,val3,st[val1+2:val2-1],st[val3+2:],sep=' :  ')
                if (val1<val2) and (val2<val3): # es una linea con diccionario key y resultado
                   self.strout[st[val1+2:val2-1]].set(st[val3+1:])
                   numprocesadas+=1
                else:
                    numnoprocesadas+=1
                st=f.readline()
        messagebox.showinfo('Info', 'Se procesaron '+str(numprocesadas)+' çlaves\n'+' No se procesaron '+str(numnoprocesadas))        

    def newattribute(self):
        if self.newattr==None:
            self.newattr=li.LabelInput(self.frlistenc,'Nombre Nuevo atributo',bg='green')
            self.newattr.grid(row=10,column=1,columnspan=2)
        else: self.newattr.grid(row=10,column=1,columnspan=2)   
        print(self.newattr.get())

    def savenew(self):
        if self.newattr.get() in self.strout.keys():
            messagebox.showwarning('Advertencia', 'Esta llave ya existe: '+self.newattr.get())
        elif self.newattr.get()=="":
            messagebox.showwarning('Advertencia', 'Esta campo no puede esatar vacio : '+self.newattr.get())
        else:
            self.strout[self.newattr.get()]=StringVar()
            self.dictout[self.newattr.get()] = li.LabelInput(self.fredit,self.newattr.get() +'= Nuevo',width=30,input_var=self.strout[self.newattr.get()],bg='green')
            self.dictout[self.newattr.get()].grid(row=self.lastpos[0],column=self.lastpos[1])
            self.newattr.pack_forget()
        

    def proofold(self):
        xdictout={}  # It is neccesary to form a xdict  dor find elements 
        for key in self.strout.keys():
            try:
                expr=self.strout[key].get().strip( )
                if expr[0] == '[' and expr[-1]==']':
                    expr1 = expr.strip('][')
                    expr2 = expe1.split(',')
                    expr0 = expr2
                elif expr[0] == '(' and expr[-1]==')':   
                    expr1 = expr.strip('()')
                    expr2 = expr1.split(',')
                    expr3 = tuple(expr)
                    expr0 = expr 
                else:
                    expr0 = expr    
                xdictout[key]=expr0
            except:
                xdictout[key]=self.strout[key].get().strip( )
        dictsit.init_driver
        table = dictsit.findelements(xdictout)
        print(table)

    def proof(self):
        filepy=self.sitio.get()+ str(datetime.today().date().strftime('%d-%m-%Y'))
        fp=importlib.import_module(filepy)
        # import filepy as gen        
        with open('filename.log', 'w') as f , redirect_stderr(f): #replace filepath & filename
            print("print this to file")   #will be written to filename & -
            dictsit.tab_lista=fp.xdict['url']
            dictsit.init_driver()
            errfind,errfield = dictsit.assertdict(fp.xdict)
        self.text_edit.delete('1.0',END)
        self.text_edit.insert(END, 'Errores en encntrar elementos ', str(len(errfind)) )
        self.text_edit.insert(END, 'Errores en encntrar atributos ', str(len(errfield)) )
        for key in errfind:
            self.dictout[key].mark('red')
            self.modifiedkey.append(key)
        for key in errfield:
            self.dictout[key].mark('orange')
            self.modifiedkey.append(key)
        with open('filename.log', 'r') as f:
            self.text_edit.insert(END, f.readlines())
            

    def generate(self):
        #print(os.curdir)
        with open(self.sitio.get()+ str(datetime.today().date().strftime('%d-%m-%Y'))+'.py', mode='w',encoding='utf-8') as f:
            print ('from dictsit import va', file=f)
            print('xdict = {}', file=f)
            for key in self.dictout.keys():
                expr = self.dictout[key].get().strip()
                if expr=='': # no pone este campo
                    continue
                elif expr[0] in ['(','['] :
                    print('xdict["'+key+'"] = '+ expr,file=f)
                else:
                    if expr[0]!="'" and expr[len(expr)-1]!="'":
                        expr="'"+expr+"'" # hay que poner comillas
                    print('xdict["'+key+'"] = '+ expr ,file=f)
            return f.name
            f.close()
        
    def get_key(self,val): 
            for key, value in self.dictout.items(): 
                print(val,value)
                if val == str(value): 
                    return key 
            return None     

    def focus(self,event): 
        
        self.widget = self.raiz.focus_get() 
        busqwidget=str(self.widget)[0:-7]# se le quita el .!entrt. Hay un problema cdo se da el click el focus lo da como entry
        self.key= self.get_key(busqwidget)
        print(self.widget, "has focus") 

    def cleanall(self):
        for key in self.dictout.keys():
            self.strout[key].set('')

    def copy(self):
        print('copy')
        self.dictout[self.key].set(str(self.dictini[self.key]))

    def changeatr(self):
        numfind=self.strout[self.key].get().find('#')
        self.newattribute()
        if self.newattr!=None:
            if numfind>0:
                self.newattr.set(strout[self.key][numfind:])
        amswer = input (' tecle')
        dictini[self.key]=self.newattr.get()
 
            
    def copyuntil(self):
        init_str=str(self.dictini[self.key])
        val = -1
        for i in range(0, self.numcoma.get()): 
            val = init_str.find(',', val + 1)
        self.dictout[self.key].set(str(self.dictini[self.key])[:val])

    def copylast(self):
        init_str=str(self.dictini[self.key])
        val = -1
        for i in range(0, self.numcoma.get()): 
            val = init_str.find(',', val + 1)
        self.dictout[self.key].set(str(self.dictini[self.key])[val:])


    def muestra_proy(self,printvacio,columnas,heightmax):
       for widg in self.fredit.winfo_children():
            widg.destroy()
       cols=[]
       if not self.basechanged: # si no es base changed se incializa el strout
            self.strout={}
       self.dictout={}
       for col in range(columnas): cols.append(0)
       for key in self.dictini.keys():
          print(key,cols) 
          if printvacio or (isinstance(self.dictini[key],IntVar) and self.dictini[key].get()!=0) or (isinstance(self.dictini[key],StringVar) and self.dictini[key].get()!=''):         
                if not self.basechanged:  # si no es una base cambiada se crea la str var y se mantiene con el valor 
                    self.strout[key]=StringVar()
                    if self.baseedit:
                        if key in self.xdictedit.keys():
                            self.strout[key].set(str(self.xdictedit[key]))
                        else:
                            self.strout[key].set('')
                    else:
                        self.strout[key].set(str(self.dictini[key]))
                self.dictout[key]=li.LabelInput(self.fredit,key +'= '+str(self.dictini[key]),width=30,input_var=self.strout[key])
                for col in range(len(cols)):
                    if cols[col]<heightmax:
                        self.dictout[key].grid(row=cols[col], column=col)
                        self.dictout[key].bind("<Button-1>", self.focus)
                        print('posic wid',key, cols[col], col)
                        cols[col]+=1
                        break
                    else:
                        continue                           
       self.fredit.bind_all("<Button-1>",self.focus)
       return (cols[col],col)
        
if __name__ == '__main__':
    import Freelancer20 as frl
    #po=Busqproywin(1,2,'Workana',['English','Español','Português'],['Delphi','C++'],'https://www.workana.com/jobs?ref=home_top_bar','Google','raulrfa@gmail.com','Karpov75%','freebd.db')
    
    ds=dictofindsel('Freelancer','https://www.freelancer.com/jobs/1/',di.elem_sitio('Workana'),frl.xdict,tipstruct.dictgen)
    ds.muestra_proy(True,2,16)
    #ds.clean()
    #print (elem_sitio('Workana'))

    