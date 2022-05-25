from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://www.infomoney.com.br/")

driver.implicitly_wait(3) #seconds

dados1 = driver.find_element(By.ID,"high").text
dados2 = driver.find_elements(By.ID,"high")[0].text


print(dados1)
print('------')
print(dados2)

driver.get("https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?chave")

driver.implicitly_wait(3)#seconds

dados3 = driver.find_element(By.ID,"product-name-default").text

print(dados3)