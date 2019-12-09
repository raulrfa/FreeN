import sqlite3
import enumeradores 


def editsitiosdb():
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    # En el filtro debiera ser distinct en el body todos
    query =" SELECT * FROM  sitios "
    # query = query + " and tema = "+ 
    curs.execute(query) 
    return curs.fetchall()

def editprelproyectosdb(id):
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    # En el filtro debiera ser distinct en el body todos
    if id==0:
        query =" SELECT * FROM  prelproyecto "
    else:
        query =" SELECT * FROM  prelproyecto WHERE idsitio={}".format(id)
    # query = query + " and tema = "+ 
    curs.execute(query) 
    return curs.fetchall()

def editproyectosdb(id):
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    # En el filtro debiera ser distinct en el body todos
    if id==0:
        query =" SELECT * FROM  proyecto "
    else:
        query =" SELECT * FROM  proyecto WHERE idsitio={}".format(id)
    # query = query + " and tema = "+ 
    curs.execute(query) 
    return curs.fetchall()


def nuevositiodb():     
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    # En el filtro debiera ser distinct en el body todos
    query =" INSERT INTO sitios DEFAULT VALUES"
    # query = query + " and tema = "+ 
    curs.execute(query) 
    db.commit()
    return curs.lastrowid

def deletesitiodb(id):     
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    # En el filtro debiera ser distinct en el body todos
    query ="DELETE FROM sitios WHERE idsitio={}".format(id)
    # query = query + " and tema = "+ 
    curs.execute(query) 
    db.commit()
    return curs.lastrowid

def updatesitio(lista):
    lista=tuple(lista)
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    # En el filtro debiera ser distinct en el body todos
    query ="""UPDATE sitios SET idsitio=?,nomsitio=?,url=?,pais=?,creacion=?,nivelesdemerito=?,nivelesmembresia=?, 
          urlproy=?, nombusq=?, clavebusq=?, notas=?, xdict=? WHERE IDSITIO={}""".format(lista[0])
    # query = query + " and tema = "+ 
    print(query,lista)
    curs.execute(query,lista) 
    db.commit()
    return lista[0]

def salvarprelproyectodb(lista):
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    if lista[0]==-1: # se inserta un nuevo elemento no se pasa el indice (No se puede usar None)
        query= "INSERT OR REPLACE INTO prelproyecto (idsitio, fechavisita, url, copy, copyofer,keywords) VALUES(?,?,?,?,?,?)"
        curs.execute(query,lista[1:])
    else:   # se reempaza algunos cmbios pero no e toca el indice
        query= "INSERT OR REPLACE INTO prelproyecto (idprelproyecto,idsitio, fechavisita, url, copy, copyofer,keywords) VALUES(?,?,?,?,?,?,?)"
        curs.execute(query,lista)
    db.commit()

def dictvartoval(dictvar):
    dictval={}
    for key in dictvar.keys():
        dictval[key]=dictvar[key].get()
    return dictval  

def salvadict(tabla,mydict):
    try:
        db = sqlite3.connect('freebd.db')
        curs = db.cursor()
        curs.execute('SELECT * FROM '+ tabla)
        names = [description[0] for description in curs.description]
        toerase=[]
        replace = False
        for key in mydict.keys():
            if key in names: 
                if key=='idproyecto' :  replace=True
            else: toerase.append(key)
        for key in toerase:
            del mydict[key]   
        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())

        if  not replace : # se inserta un nuevo elemento no se pasa el indice (No se puede usar None)
            query = "INSERT INTO %s ( %s ) VALUES ( %s );" % (tabla, columns, values)
            print(query)
            curs.execute(query)
        else:   # se reempaza algunos cmbios pero no e toca el indice
            query= "INSERT OR REPLACE INTO %s ( %s ) VALUES ( %s );" % (tabla, columns, values) 
            curs.execute(query)
        db.commit()
    except:
        print( 'Error en la base de datos')
    return curs.lastrowid

def queryidiomasISO(enum, listentr):
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    if enum==enumeradores.Idiomas:
        tablename ='idioma'
        campo1 = 'idioma'
        campo2 = 'ISO639'
    query="SELECT {} FROM {} WHERE {} IN {} ".format(campo2,tablename,campo1,tuple(listentr))
    curs.execute(query)
    return tuple(curs.fetchall())


def muchosUnsitio(id,enum,setenum, Escritura):
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    if enum==enumeradores.Idiomas: 
        tablename ='sitioidioma'
        campo = 'ididioma'
    elif enum==enumeradores.TipoProyecto:
        tablename='sitiostipo'
        campo= 'idTipo'
    elif enum==enumeradores.AreasTrab:
        tablename='sitioareatrabajo'
        campo= 'idareatrabajo'
    elif enum==enumeradores.Habilidades:
        tablename='sitiohabilidad'
        campo= 'idhabilidad'
    if Escritura==True:
        query='DELETE FROM {} WHERE idsitio={}'.format(tablename,id)
        print(query)
        curs.execute(query) 
        db.commit()
        curs =db.cursor()
        for muchos in list(setenum):
            query= 'INSERT INTO {} VALUES({},{}) '.format(tablename,id,muchos)
            print(query)
            curs.execute(query) 
        db.commit()
    else:
        query= 'SELECT {} FROM {} WHERE idsitio={}'.format(campo,tablename,id)
        print(query)
        curs.execute(query)
        lista=[]
        for rec in curs.fetchall():
            lista.append(rec[0])
        return lista
    
if __name__ == '__main__':
    #print(type())
    muchosUnsitio(2,enumeradores.Habilidades,{1,2,3},1)