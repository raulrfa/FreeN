import sqlite3


def editsitiosdb():
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    # En el filtro debiera ser distinct en el body todos
    query =" SELECT * FROM  sitios "
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

def updatesitio(lista):
    db = sqlite3.connect('freebd.db')
    curs = db.cursor()
    # En el filtro debiera ser distinct en el body todos
    query =" UPDATE sitios WHERE IDSITIO={} VALUES({})". format(lista[0],lista)
    # query = query + " and tema = "+ 
    curs.execute(query) 
    db.commit()
    return curs.lastrowid