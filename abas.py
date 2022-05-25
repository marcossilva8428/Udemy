from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://www.infomoney.com.br/")

driver.implicitly_wait(2) #seconds

#https://www.uol.com.br
driver.execute_script('window.open()')

# Switch to the newly opened tab
driver.switch_to.window(driver.window_handles[1])

driver.get('http://www.uol.com.br')

driver.implicitly_wait(2) # seconds

driver.switch_to.window(driver.window_handles[0])

driver.close()