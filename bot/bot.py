from selenium import webdriver #importe do selenium webdriver "controlador" de site
from selenium.webdriver.firefox.options import Options #import do controlador especifico do firefox
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time #biblioteca para adicionar um tempo de espera 

#instacinado o bot 
options = Options()# instancinado 
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"#adicionando o caminho do navagado ao codigo
driver = webdriver.Firefox(options=options, executable_path="C:/Users/dougl/Desktop/estudar/projetos/bot/geckodriver.exe")#adiconando o caminho do controlador de navegador

link='https://www.google.com.br/maps/place/'
#nome = '0518251'
#senha = 'Weliton@123'
local = 'paque pedra da cebola'
#link = link+local

def acess(link):
  elemento=driver.get(link)
  return elemento

def local(link):
  time.sleep(30)
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]').send_keys('paque pedra da cebola')
  #elemento=driver.find_element_by_xpath(r'//*[@id="password"]').send_keys(senha)
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]').send_keys(Keys.ENTER)
  return elemento


def restaurantes(link):
  
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[5]/div/div/div/div[1]/div/div/div/div/div[1]/div/button/span[1]').click()
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]')
  print(elemento)
  return elemento






acess(link)
local(link)
print('acessando restaurantes#')
time.sleep(10) 
#click_open_close_time(link)
restaurantes(link)

soup=BeautifulSoup(elemento,'html.parser')
#resposta=soup.find("div", {"jstcache":"933"})
print(soup)


#     while True:
#         try :
#             elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span')
            
#             authentication=True
#         except:
#             authentication=False
            
#         if authentication==True:
#             print('autentificado')
#             break
#     return authentication 
# print('teste função de acesso')
# acess(link)
# print('função de autentificação') 
# authentication()
 
 
 
 
 
 
# def messenger(destino,message):
#     elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span').click()
#     time.sleep(20)
#     print('limpando')
#     elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]').clear() 
#     print('escrever')
#     time.sleep(20)
#     elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]').send_keys(destino)
#     print('acessando')
#     time.sleep(10)
#     elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/span').click()
#     print('limpando')
#     elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').clear() 
#     print('escrever')
#     time.sleep(20)
#     elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
#     print('acessando')
#     time.sleep(20)
#     elemento=driver.find_element_by_xpath(r'/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)



#     return elemento

# messenger('É eu msm','ola mundo')
#web scraping
#colta de dados
#mensagem = driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/div[3]/div/div/div[3]/div[17]/div/span')
#print(mensagem)