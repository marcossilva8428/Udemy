from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://www.imdb.com/title/tt0120338/videogallery/")

elementoSelect = Select(driver.find_element(By.NAME,"sort"))

elementoSelect.select_by_value('expiration')

driver.implicitly_wait(3) #seconds

elementoSelect = Select(driver.find_element(By.NAME,"sort"))

elementoSelect.select_by_visible_text('Date')

Select(driver.find_element(By.NAME,"sort")).select_by_index(1)
