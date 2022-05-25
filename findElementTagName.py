from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

driver.implicitly_wait(6) #seconds

nomeFii = driver.find_elements(By.TAG_NAME,'h1')[0].text

valorAtual = driver.find_elements(By.TAG_NAME,'strong')[0].text

tabelaRendimentos = driver.find_elements(By.TAG_NAME,'table')[0].text

tabelaResultados = driver.find_elements(By.TAG_NAME,'table')[1].text

print(nomeFii)
print(valorAtual)
print('-------')
print(tabelaRendimentos)
print('-------')
print(tabelaResultados)