"""
Construir os metodos:
get_email()
get_fone()
get_location()
main()
"""
from selenium import webdriver
import re

def get_site(host):
    chrome = webdriver.Chrome()
    pagina = chrome.get(host)
    fonte = chrome.page_source
    return fonte,chrome

def get_email(host):
    fonte,chrome = get_site(host)
    import re
    #print fonte    
    padrao1 = re.compile(r'\w+@\w+\.\w+')
    padrao2 = re.compile(r'\w+@\w+\.\w+\.\w+')
    lista_1 = padrao1.findall(fonte)
    lista_2 = padrao2.findall(fonte)

    chrome.close()
    return lista_1,lista_2  

lista_email = []
def organiza_lista(lista):
    lista1,lista2 = lista
    global lista_email
    for email in range(len(lista1)-1):
        lista_email.append(lista1[email])
    for email in range(len(lista2)-1):
        lista_email.append(lista2[email])
    return lista_email        

host = "http://www.listanossa.com.br/welcome/empresa/1/"
for i in range(190,999):
    
    lista = organiza_lista(get_email(host + str(i)))

    def armazena(lista):
        arquivo = open("arquivo1.txt","a")
        for item in range(len(lista)):
            arquivo.write(lista[item]+',')
        #arquivo.save()
        arquivo.close()

    armazena(lista)
