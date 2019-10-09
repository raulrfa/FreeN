from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from enum import Enum

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


va=Enum('TipValor','v t tc tt at ah') # va.v vacio va.t > texto, va.tc texto acumulativo va.tt busqueda en busquedas clsva.at .get_atrribute('title') va.ah hreference


#driver.get("https://www.workana.com/jobs?ref=home_top_bar")

def elem_sitio():

    xdict={'sitio' : "Workana"}
    xdict['url']="https://www.workana.com/jobs?ref=home_top_bar"
    xdict['urlskills']="https://www.workana.com/jobs?ref=home_top_bar"
    xdict['elems']= [By.XPATH,'//div[contains(@class,"project-item")]',va.v]
    xdict['titles']= [By.XPATH,'//div[contains(@class,"project-item")]/div/h2/a/span',va.at]
    xdict['dates']=[By.XPATH,'//div[contains(@class,"project-item")]/div/h5',va.at]
    xdict['bids']=[By.XPATH,'//span[contains(@class,"bids")]',va.t]
    xdict['clients']=[By.XPATH,'//div[contains(@class,"project-item")]/div[2]/div[4]/span[2]/a/span',va.t]
    xdict['presupuestos']=[By.XPATH,'//div[contains(@class,"project-item")]/div[3]/h4/span',va.t] # text
    # xdict['presupuestos2']='//div[contains(@class,"project-item")]/div[3]/span[@class="values"]' # text
    xdict['paises']=[By.XPATH,'//span[@class="country-name"]',va.t] # text
    # xdict['ratings']=[By.XPATH,"//*[@id='projects']/div/div[2]/div[1]/h2/a/span" # text
    xdict['ratings']=[By.XPATH,'//span[@class="stars-bg"]',va.at] # title
    xdict['texts']=[By.XPATH,'//div[contains(@class,"project-item")]/div[2]/div[2]/div',va.t] # text
    xdict['ref'] = [By.XPATH,'//div[contains(@class,"project-item")]/div[1]/h2/a', va.ah] # referencia atributo
    xdict['skills'] = [By.XPATH,'//div[@class="skills"]/div',va.tt,By.XPATH,'./a',va.tc]
    return xdict

def findkeynames(xdict):
    xlist=[]
    for key in xdict.keys():
        print(key, xdict[key], 'tipo ',type(xdict[key]))
        if isinstance(xdict[key],list):
            xlist.append(key)
    return xlist




def findelements(xdict):
    sdict={}
    lenmin=200
    lenmax=0
    keymax=keymin=''
    driver =webdriver.Chrome(executable_path="F:\PyProj\FreeN\chromedriver.exe")
    driver.get(xdict['url'])
    for key in xdict.keys():
        if isinstance(xdict[key],str):
            pass # sdict[key]=xdict[key]
        else:
            sdict[key]=driver.find_elements(xdict[key][0],xdict[key][1])
            k= len(sdict[key])
            if k > lenmax:
                lenmax=k
                keymax=key
            elif k <lenmin : 
                lenmin=k
                keymin=key
    tabla =[]
    for k in range(lenmax):
        fila=[]
        for key in sdict.keys():
            # va.v vacio va.t > texto, va.tc texto acumulativo va.tt busqueda en busquedas clsva.at .get_atrribute('title') va.ah hreference
            if xdict[key][2]==va.v: fila.append(sdict[key][k])
            elif xdict[key][2]==va.t: fila.append(sdict[key][k].text)
            elif xdict[key][2]==va.at: fila.append(sdict[key][k].get_attribute('title'))
            elif xdict[key][2]==va.ah: fila.append(sdict[key][k].get_attribute('href'))
            elif xdict[key][2]==va.tt and xdict[key][5]:
                texto=''
                subcoll=sdict[key][k].find_elements(xdict[key][3],xdict[key][4])
                for sub in subcoll:
                    texto = texto+ sub.text+','
                fila.append(texto[:-1]) 
        tabla.append(fila)
    return tabla        


    

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
    print (elem_sitio())
    llaves= findkeynames(elem_sitio())
    print(llaves)
    print(findelements(elem_sitio()))