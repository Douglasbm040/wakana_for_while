#!/usr/bin/env python
# coding: utf-8

# In[93]:


from selenium import webdriver #importe do selenium webdriver "controlador" de site
from selenium.webdriver.firefox.options import Options #import do controlador especifico do firefox
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time #biblioteca para adicionar um tempo de espera 


# In[94]:



#instacinado o bot 
options = Options()# instancinado 
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"#adicionando o caminho do navagado ao codigo
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options, executable_path="C:/Users/dougl/Desktop/estudar/projetos/bot/geckodriver.exe")#adiconando o caminho do controlador de navegador


# In[95]:


link='https://www.google.com.br/maps/place/'
local = 'paque pedra da cebola'
#link = link+local


# In[96]:


def acess(link):
  elemento=driver.get(link)
  return elemento

def local(link):
  time.sleep(30)
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]').send_keys('paque pedra da cebola')
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div/div[3]/div/input[1]').send_keys(Keys.ENTER)
  return elemento


def restaurantes(link):
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[5]/div/div/div/div[1]/div/div/div/div/div[1]/div/button/span[1]').click()
  elemento=driver.find_element_by_xpath(r'/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]')
  print(elemento)
  return elemento


# In[97]:


acess(link)
local(link)
print('acessando restaurantes#')
time.sleep(10) 
restaurantes(link)


# In[98]:


time.sleep(30)

#dados=driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]')
dados=driver.find_element_by_css_selector('div.siAUzd-neVct:nth-child(4)')


# In[99]:


html=dados.get_attribute("innerHTML")


# In[100]:


soup=BeautifulSoup(html,'html.parser')
#resposta=soup.find("div", {"jstcache":"933"})
texto=soup.get_text()
texto.strip()
texto=texto.replace("$$",'')
texto=texto.split('·')



# In[ ]:




