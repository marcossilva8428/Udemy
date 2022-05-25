from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import urllib3
import urllib.request

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://www.imdb.com/title/tt0120338/mediaindex?ref_=tt_pv_mi_sm")

driver.implicitly_wait(3) #seconds

divImagens = driver.find_element(By.ID, 'media_index_thumbnail_grid')
primeiraImagem = divImagens.find_elements(By.TAG_NAME,'img')[0]
atributoSrc = primeiraImagem.get_attribute('src')
print(atributoSrc)

try:
    urllib.request.urlretrieve(atributoSrc,r'C:\Users\marcos.da.silva.j\Downloads\teste.jpg')
    print('Imagem Baixada')
except:
    print('Ocorreu um erro')