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
driver = webdriver.Firefox(options=options, executable_path="C:/Users/dougl/Downloads/geckodriver-v0.29.1-win64/2/geckodriver.exe")#adiconando o caminho do controlador de navegador

link='https://www.google.com.br/maps/place/Esp%C3%ADrito+Santo/'
#nome = '0518251'
#senha = 'Weliton@123'

def acess(link):
  element=driver.get(link)
  return element

def authentication():
  elemento=driver.find_element_by_xpath(r'//*[@id="user_id"]').send_keys(nome)
  elemento=driver.find_element_by_xpath(r'//*[@id="password"]').send_keys(senha)
  elemento=driver.find_element_by_xpath(r'//*[@id="entry-login"]').click()
  return elemento
def exam():
  time.sleep(10)                           
  elemento=driver.find_element_by_css_selector(r'.submit').click()
  return elemento

acess(link)
authentication()
exam()
list_terms=[]
soup = BeautifulSoup(driver.page_source, 'html.parser')
for i in range(0,5):
  questions=soup.find_all('p')[i].get_text()
  list_terms.append(questions)
for term in list_terms:
  link='https://www.google.com/search?q=google&oq=google&aqs=chrome..69i57j35i39l2j69i60l3j69i65l2.3484j0j7&sourceid=chrome&ie=UTF-8'
  acess(link)                             
  elemento=driver.find_element_by_xpath(r'/html/body/div[4]/form/div[1]/div[1]/div[2]/div/div[2]/input').clear
  elemento=driver.find_element_by_xpath(r'/html/body/div[4]/form/div[1]/div[1]/div[2]/div/div[2]/input').send_key('branly.:'+term)
  elemento=driver.find_element_by_xpath(r'/html/body/div[4]/form/div[1]/div[1]/div[2]/div/div[2]/input').send_keys(Keys.ENTER)
  elemento=driver.find_element_by_xpath(r'/html/body/div[4]/form/div[1]/div[1]/div[2]/div/div[2]/input').click()
#def authentication():


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