from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://www.imdb.com/")

driver.implicitly_wait(6) #seconds

campoBusca = driver.find_elements(By.NAME,"q")[0]

campoBusca.send_keys('Titanic')