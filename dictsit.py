from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from enum import Enum
from tkinter import messagebox
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TipValor(Enum):
    v = 1 #vacio
    t = 2 # texto
    tc= 3 # texto acumulado
    tt= 4 # busqueda en vusquedas 
    at= 5 # get atributrte title
    ah= 6 # get titlereference
    af= 7 #  atributo de nombre 5 con valor 5, 
    c = 8 #  click

va=Enum('TipValor','v t tc tt at ah af c') # va.v vacio va.t > texto, va.tc texto acumulativo va.tt busqueda en busquedas clsva.at .get_atrribute('title') va.ah hreference,af atributo de nombre 5 con valor 5, c click
driver=None
from selenium import webdriver
# Define the URL's we will open and a few other variables 
tab_lista = '' # URL A
tab_proy = '' # URL B
tab_ofer = ''

def init_driver():
    global driver,tab_lista,tab_proy,tab_ofer
    if driver==None: # si el driver no existe se crea, si existe se reusa
        driver =webdriver.Chrome(executable_path="F:\PyProj\FreeN\chromedriver.exe")
        print("Current Page Title is : %s" %driver.title)
        driver.get(tab_lista)
    #driver.execute_script("window.open('');")
    driver.execute_script('''window.open('{}');'''.format("about:blank"))
    # Switch to the new window and open URL B
    #driver.switch_to.window(driver.window_handles[1])
    #driver.get(tab_proy)
    #driver.execute_script("window.open('');")
    #driver.execute_script('''window.open('{}');'''.format("about:blank"))
    #driver.switch_to.window(driver.window_handles[2])
    #driver.get(tab_ofer)
    # …Do something here
    print("Current Page Title is : %s" %driver.title)
    # Close the tab with URL B
    # Switch back to the first tab with URL A
    #driver.switch_to.window(driver.window_handles[0])
       
def switchtab(i,url):
    global driver,tab_lista,tab_proy,tab_ofer
    try:
        if driver.current_window_handle!=driver.window_handles[i]:
            driver.switch_to_window(driver.window_handles[i])
        if url!='':    
            driver.get(url)
            if i==0 : tab_lista=url
            if i==1 : tab_proy= url
            if i==2 : tab_ofer= url
    except:
        messagebox.showerror('No se pudo encontrar la url')

xdict={}
tuplemax=('idProyecto','creacion', 'mensajes','coverletter','ganttoferta','answers','plazo','nomproponente','paisproponente','ratingproponente',
'ultimologin','proyectospagados','moneda','valoroferta','costooferta','devengado','ofertamin','mensajesenviado','fechaultmensaje','requisitosesp',
'referenciaofer')

#driver.get("https://www.workana.com/jobs?ref=home_top_bar")

def elem_sitio(sitio):
    global xdict
    if sitio == "Workana":
        xdict={'sitio' : "Workana"}
        xdict['url']="https://www.workana.com/jobs?"  
        # click hoy 20/ 10 //*[@id="projects"]/div[13]/div[2]/nav/ul     > li:nth-child(2)
        xdict['filtroskills']=('skills=','.')
        xdict['filtrogen']=('query=','+')
        xdict['filtroidio']=('language=',',','ISO')
        xdict['filtrounion']=('&')
        xdict['click']=(By.CSS_SELECTOR,'ul.pagination> li:nth-child(#) > a',va.ah)
        xdict['urlskills']="https://www.workana.com/jobs?ref=home_top_bar"
        #xdict['elems']= [By.XPATH,'//div[contains(@class,"project-item")]',va.v]
        xdict['nomproyecto']= [250,By.XPATH,'//div[contains(@class,"project-item")]/div/h2/a/span',va.at]
        xdict['creacion']=[100,By.XPATH,'//div[contains(@class,"project-item")]/div/h5',va.at]
        xdict['cantofertantes']=[60,By.XPATH,'//span[contains(@class,"bids")]',va.t]
        xdict['nomproponente']=[40,By.XPATH,'//div[contains(@class,"project-item")]/div[2]/div[4]/span[2]/a/span',va.t]
        # xdict['presupuestos2']='//div[contains(@class,"project-item")]/div[3]/span[@class="values"]' # text
        xdict['paisproponente']=[30,By.XPATH,'//span[@class="country-name"]',va.t,30] # text
        # xdict['ratings']=[By.XPATH,"//*[@id='projects']/div/div[2]/div[1]/h2/a/span" # text
        xdict['ratingproponente']=[10,By.XPATH,'//span[@class="stars-bg"]',va.at] # title
        xdict['presupuestos']=[50,By.XPATH,'//div[contains(@class,"project-item")]/div[3]/h4/span',va.t] # text
        xdict['descripcion']=[350,By.XPATH,'//div[contains(@class,"project-item")]/div[2]/div[2]/div',va.t] # text
        xdict['referencia'] = [0,By.XPATH,'//div[contains(@class,"project-item")]/div[1]/h2/a', va.ah] # referencia atributo
        xdict['skills'] = [25,By.XPATH,'//div[@class="skills"]/div',va.tt,By.XPATH,'./a',va.tc]
        xdict['assertproject']=(By.XPATH,'//*[@class="project-status"]')
        # eb la lista de proyectos los que comienzan con . no estan en la grid sino en los detalles del proyecto 
        xdict['.descripcion']=(0,By.CLASS_NAME,'specification',va.t) # la descripcoion puede tnener datos adicionales que van al camp descripcion sin .
        xdict['.deadline']=(0,By.CLASS_NAME,'deadline',va.t)
        xdict['.expdate']=(0,By.CLASS_NAME, 'date',va.t)
        xdict['.ofertar']=(0,By.XPATH,'//*[@id="bid_button"]',va.ah)
        xdict[':tiplogin']=(0,By.CLASS_NAME,'btn--google')
        xdict[':nombusq']=(0,By.XPATH,'//*[@id="identifierId"]',By.XPATH,'//*[@id="identifierNext"]/span/span')
        xdict[':clavebusq']=(0,By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input',By.XPATH, '//*[@id="passwordNext"]/span/span')
        xdict['#moneda']=('r',By.XPATH,'//span[comtains(@class,"input-group-addon")]',va.t)
        xdict['#coverletter']=('w',By.XPATH,'//*[@id="BidContent"]')
        xdict['#plazo']=('w',By.CSS_SELECTOR,'#BidDeliveryTime')
        xdict['#valoroferta']=('w',By.CSS_SELECTOR,'#Amount')
        xdict['#costooferta']=('R',By.ID,"bid_comission",va.t)
        xdict['#devengado']=('R',By.CSS_SELECTOR,'#workerNetAmount',va.t)
        xdict['#includedfile']=('R',By.XPATH,'//*[@class="block-appear"]/i/span',va.t)
        xdict['#referenciaofer']=('R',By.XPATH,'//*[@class="btn-primary"]',va.t)
        xdict['#enviarofer']=('P',By.XPATH,'//*[@class="btn-primary"]',va.t)

        return xdict
    elif sitio=='Twago':pass
    elif sitio=='Freelancer':pass
    elif sitio=='UpWork':pass
    elif sitio=='Freelancer':pass
    elif sitio=='Freelancer':pass

def login(xdict,tiplogin,nombusq,clavebusq):
    if tiplogin!='': # es un login en medios sociales
        wait=WebDriverWait(driver,12)
        key=':tiplogin'
        print(xdict[key][2])
        ele=wait.until(EC.element_to_be_clickable((xdict[key][1],xdict[key][2])))  
        ele.click()
        print(driver.current_url)
        key=':nombusq'
        print(driver.current_url)
        wait.until(EC.visibility_of_element_located((xdict[key][1],xdict[key][2]))).send_keys(nombusq)
        if xdict[key][3]!='':
            wait.until(EC.element_to_be_clickable((xdict[key][3],xdict[key][4]))).click()
        key=':clavebusq'
        wait.until(EC.visibility_of_element_located((xdict[key][1],xdict[key][2]))).send_keys(clavebusq)
        if xdict[key][3]!='':
            wait.until(EC.element_to_be_clickable((xdict[key][3],xdict[key][4]))).click()
    else:    
        key=':nombusq'
        driver.find_element(xdict[key][1],xdict[key][2]).send_keys(nombusq)
        key=key=':clavebusq'
        driver.find_element(xdict[key][1],xdict[key][2]).send_keys(clavebusq)
        key=':sendlogin'
        wait.until(EC.element_to_be_clickable((xdict[key][1],xdict[key][2]))).click()
    tab_ofer=driver.current_url
    return tab_ofer    

def assertoferta(xdict):
    key='#coverletter'
    try:
        ele=driver.find_element(xdict[key][1],xdict[key][2])
        return True      #encontro la coverletter
    except:  #estoy en una variante de proyecto
        key='.ofertar'   #insisto en la oferta
        try:
            ele=driver.find_element(xdict[key][1],xdict[key][2])  # debo haber encontrado el boton
            driver.get(ele.get_attribute('href')) # voy a la web de fertas
            return True # lo logre
        except:
           return False    # estoy perdido
    
    

def makeoferta(xdict,oferta,work):
    """ Esciruts y lectura anticipada y retarada 
    de las oferta """
    oferdict = {key:xdict[key] for key in xdict.keys() if key[0]=='#'}
    errors=[]
    for key in oferdict.keys():
        if oferdict[key][0]==work: #este elemento es de trabajo 
            try:
                ele= driver.find_element(oferdict[key][1],oferdict[key][2])
                if work.upper() == 'R':  # lectura inicial o final                
                    if oferdict[key][2]==va.t: result=ele.text
                    else: print ('no terminada')
                    oferta[key[1:]]=result
                elif work.upper()=='W':
                    ele.clear()
                    ele.click()
                    ele.send_keys(Keys.CONTROL + 'a' + Keys.NULL, oferta[key[1:]].get())
                else:
                    if isinstance(oferta[key[1:]],int): oferta[key[1:]]=-100000
                    else: oferta[key[1:]]='Error'
                    messagebox.showerror('Error', 'Letra no valida en el tratamiento de la llave '+ key)   
            except:
                errors.append(key)
                print(key)
    return errors
            
                
def genenum(chain,varen):
    if chain[0]=='<' and chain[len(chain)-1]=='>':
        print(char, varen)
        chain.lstrip('<')
        chain.rstrip('>')
        numpto=chain.find('.')
        numdosptos=chain.find(':')
        chainnew=varen + chain[numpto:numdosptos]
        return chainnew
    else: return None    

        
        




def findkeynamesize(xdict):
    xlist=[]
    colsize=[]
    colview=[]
    for key in xdict.keys():
        print(key, xdict[key], 'tipo ',type(xdict[key]))
        if isinstance(xdict[key],list):
            xlist.append(key.capitalize())
            colsize.append(xdict[key][0])
            if xdict[key][0]!=0:
                colview.append(key.capitalize())
    return xlist, colsize, colview

def find_next_page(xdict,var=''):
    global driver
    #driver.get(xdict['url']) # se paso al main
    if isinstance(var,int): 
        replaced=xdict['click'][1].replace('#',str(var),1)
    next=driver.find_element(xdict['click'][0],replaced)
    web=next.get_attribute('href')
    driver.get(web)


def filtrar_next_page(xdict,var="",type=""):
     global driver
     if isinstance(var,str):
        filtroind='filtro'+type
        filtrobase=xdict[filtroind][0]
        filtro=var.split()
        for word in filtro:
            tup=xdict[filtroind][1]
            filtrobase+=word+tup
        web=xdict['url']+filtrobase[:-1]
        driver.get(web)

def findextraproy(xdict,proyecto):
    """ Procesa los elementos del diccionario cuya llave comieza con . y que no estan en la grid
        y que aparecen en la wen especifica de cada proyecto y n en el general"""
    global driver
    if driver.find_element(xdict['assertproject'][0], xdict['assertproject'][1])==None: return False 
    for key in xdict.keys():
        print(key)
        if key[0]=='.':
            ele=driver.find_element(xdict[key][1],xdict[key][2])
            if xdict[key][3]==va.v: result=ele
            elif xdict[key][3]==va.t: result=ele.text
            elif xdict[key][3]==va.at: result=ele.get_attribute('title')
            elif xdict[key][3]==va.ah: result=ele.get_attribute('href')
            if key in proyecto.keys():
                proyecto[key].set(result)
                print ('extra ', key, result)
            elif key[1:] in proyecto.keys():  
                proyecto[key[1:]].set(result)
            else:
                messagebox.showwarning ('No hay variantes en proyectode la clave ',key)      
    return True

def findelements(xdict,var='',typevar=None):
    global driver
    try:        
        sdict={} # diccionarios de llaves que ban en las grids
        lenmin=200 # longitudes maximas de atributos en cada keyword
        lenmax=0
        if driver==None: # si el driver no existe se crea, si existe se reusa
            driver =webdriver.Chrome(executable_path="F:\PyProj\FreeN\chromedriver.exe")
            driver.get(xdict['url'])
        else: # se usa la variable var
            if driver.title=="Settings":
                driver.get(xdict['url'])
            if isinstance(var, int):
                find_next_page(xdict,var)
            elif var!='' : 
                filtrar_next_page(xdict,var,typevar)
            else: pass
                    
        keymax=keymin=''   
        for key in xdict.keys(): # se rellena el diccionario de sdict con los elementos que hay en la pagina seleccionada
            if isinstance(xdict[key],list): # en la grid solo van los elementos lista, no tuplas [çlick] o strings
                sdict[key]=driver.find_elements(xdict[key][1],xdict[key][2]) 
                k= len(sdict[key])  # vsntidad de elementos
                if k > lenmax:  
                    lenmax=k
                    keymax=key
                elif k <lenmin : 
                    lenmin=k
                    keymin=key
        tabla =[] # tabla que se retornara para llenar la grid
        for k in range(lenmax): # numero de elementos encontrados
            fila=[]
            for key in sdict.keys():
                try:
                    # va.v vacio va.t > texto, va.tc texto acumulativo va.tt busqueda en busquedas clsva.at .get_atrribute('title') va.ah hreference
                    if xdict[key][3]==va.v: fila.append(sdict[key][k])
                    elif xdict[key][3]==va.t: fila.append(sdict[key][k].text)
                    elif xdict[key][3]==va.at: fila.append(sdict[key][k].get_attribute('title'))
                    elif xdict[key][3]==va.ah: fila.append(sdict[key][k].get_attribute('href'))
                    
                    elif xdict[key][3]==va.tt and xdict[key][5]: # para listas
                        texto=''
                        subcoll=sdict[key][k].find_elements(xdict[key][4],xdict[key][5])
                        for sub in subcoll:
                            texto = texto+ sub.text+','
                        fila.append(texto[:-1])
                except:
                    fila.append('Error')
                    messagebox.showwarning('Se adiciono un campo vacio en la llave key: '+key+'. Existe una longitud diferente lenmin: '+str(lenmin), 'lenmax '+str(lenmax) )
            tabla.append(fila)
    except :
        messagebox.showerror('Error','Se produjo un error en el proceso')
    finally:
        pass
    return tabla        

def assertdict(xdict,tipo=None):
    global driver
    errfind=[]
    errfield=[]
    keymax=keymin=''  
            
    sdict={} # diccionarios de llaves que ban en las grids
    if driver==None: # si el driver no existe se crea, si existe se reusa
        driver =webdriver.Chrome(executable_path="F:\PyProj\FreeN\chromedriver.exe")
        
    else: # se usa la variable var
        if driver.title=="Settings":
            
            
            driver.get(xdict['url'])                  
    
    for key in xdict.keys(): # se rellena el diccionario de sdict con los elementos que hay en la pagina seleccionada
        
        try:
            if isinstance(xdict[key],list): # en la grid solo van los elementos lista, no tuplas [çlick] o strings
                assert driver.find_element(xdict[key][1],xdict[key][2]) != None,  "La lave "+ key + "no encontro nada"
                sdict[key]=driver.find_elements(xdict[key][1],xdict[key][2]) 
                assert len(sdict[key])>0 , "Para llave "+key + "no se encontraron elementos"
                k= len(sdict[key])//4  # vsntidad de elementos
            elif isinstance(xdict[key],tuple):
                assert driver.find_element(xdict[key][1],xdict[key][2]) != None,  "La lave "+ key + " de la tupla no encontro nada"
                k=1
            elif isinstance(xdict[key],str):
                if find('http',xdict[key])==0:
                   assert(driver.current_url==xdict[key]), 'La llave '+ key + 'escribe eb otra url'  
                continue   
            else:
                print('La llave '+key+ 'n es string, ni lista ni tuyp;a')
                continue
        except :
            print('Error en la busquedad de key ' + key, file=sys.stderr)
            errfind.append(key)
            continue                    
        for k in range(3): # numero de elementos encontrados
            try:
                # va.v vacio va.t > texto, va.tc texto acumulativo va.tt busqueda en busquedas clsva.at .get_atrribute('title') va.ah hreference
                if xdict[key][3]==va.v: assert len(sdict[key][k])>0 , 'No hay valor para la llave '+key + ' en el campo ' + str(k)
                elif xdict[key][3]==va.t: assert len(sdict[key][k].text)>0 , 'No hay texto para la llave '+key + ' en el campo ' + str(k)
                elif xdict[key][3]==va.at: assert len(sdict[key][k].get_attribute('title'))>0 , 'No hay title para la llave '+key + ' en el campo ' + str(k)
                elif xdict[key][3]==va.ah: assert len(sdict[key][k].get_attribute('href'))>0 , 'No hay href para la llave '+key + ' en el campo ' + str(k)
                elif xdict[key][3]==va.tt and xdict[key][5]: # para listas
                    texto=''
                    subcoll=sdict[key][k].find_elements(xdict[key][4],xdict[key][5])
                    for sub in subcoll:
                        texto = texto+ sub.text+','
                    assert len(texto[:-1])>0 , 'No hay texto de listas acumulado para la llave '+key + ' en el campo ' + str(k)
            except:
                print('Error campo ' + key + ' posicion ' + str(k), file=sys.stderr)
                errfield.append(key)                  
    
    return errfind,errfield        

def gotourl(url):
    global driver
    driver.get(url)
    print(driver.title)

def printsitio(sdict):
    for key in sdict.keys():
        print(key,': ', len(sdict[key]))
    for i in range(len(sdict['elems'])):
        print()
        print('PROYECTO NUMERO '+str(i))
        print()
        print('Titulo: ', sdict['titles'][i].get_attribute('title'))
        print('Fecha :', sdict['dates'][i].get_attribute('title'))
        print('Elemento ', sdict['elems'][i])

    # title[i]=elems[i].find_element_by_xpath("./div/h2/span").get_attribute('title')
    #print('Titulo: ', title[i].get_attribute('title')
    #.get_attribute('title')
    print('Fechas: ', sdict['dates'][i].get_attribute('title'))
    print('Bids: ',sdict['bids'][i].text)
    print('Clientes: ',sdict['clients'][i].text)
    print('Paises: ', sdict['paises'][i].text)
    # print('Rating: ',sdict['ratings'][i].text)
    print('Rating: ', sdict['ratings2'][i].get_attribute('title'))

    print("Presupuesto: ",  sdict['presupuestos'][i].text)
    # print("Presupuesto2: ", presupuestos2[i].text)
    print("Textos: ",  sdict['texts'][i].text)
    print("Referencia]: ", sdict['ref'][i].get_attribute('href'))
    skills=sdict['skills'][i].find_elements(By.XPATH,'./a')
    strskills=''
    for sk in skills:
        strskills=strskills+ sk.text +','
    strskills=strskills[:-1]
    print("Skills: ", strskills)

if __name__ == '__main__':
    #print (elem_sitio('Workana'))
    tab_lista=tab_proy=tab_ofer=elem_sitio('Workana')['url']
    init_driver()
    #input('Teclee enter')
    driver.get('https://www.workana.com/signup/w?r=%2Fjob%2Fwagelaseh')
    login(elem_sitio('Workana'),'Google','raulrfa@gmail.com','Karpov75%')

    #filtrar_next_page(xdict,'Delphi web','gen')
    #find_next_page(elem_sitio('Workana'),2)
    


    """
    llaves= findkeynamesize(elem_sitio('Workana'))
    findelements(elem_sitio('Workana'),'')
    a=input('valor de: ')
    print(findelements(elem_sitio('Workana'),a))"""