from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import urllib3
import urllib.request

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://www.imdb.com")

driver.implicitly_wait(3) #seconds

driver.find_elements(By.NAME,'q')[0].send_keys("Titanic" + Keys.RETURN)