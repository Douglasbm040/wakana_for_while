


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
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options, executable_path="C:/Users/dougl/Desktop/estudar/projetos/bot/geckodriver.exe")#adiconando o caminho do controlador de navegador


link='https://www.google.com.br/maps/place/'
#local = routes.buscar()
#link = link+local


def acess(link):
  elemento=driver.get(link)
  return elemento

def local(link,local):
  time.sleep(30)
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]').send_keys(local)
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]').send_keys(Keys.ENTER)
  return elemento


def restaurantes(link):
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[5]/div/div/div/div[1]/div/div/div/div/div[1]/div/button/span[1]').click()
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]')
  print(elemento)
  return elemento


def web(ponto):
  acess(link)
  local(link,ponto)
  print('acessando restaurantes#')
  time.sleep(10) 
  restaurantes(link)
  time.sleep(30)
  #dados=driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]')
  dados=driver.find_element_by_css_selector('div.siAUzd-neVct:nth-child(4)')
  html=dados.get_attribute("innerHTML")
  soup=BeautifulSoup(html,'html.parser')
  #resposta=soup.find("div", {"jstcache":"933"})
  texto=soup.get_text()
  texto.strip()
  texto=texto.replace("$$",'')
  texto=texto.split('·')
  rest=[]
  horario=[]

  for i in range(0,len(texto)):
      v=texto[i].find('(') 
      if v != -1 :
         rest.append(texto[i])
      v=texto[i].find(':')
      if v != -1:
          horario.append(texto[i])
  rest = tuple(rest)
        
  return rest
  





