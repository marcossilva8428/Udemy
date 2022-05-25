from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

elementoAImagem = driver.find_elements(By.CLASS_NAME,"navbar-brand")[0]
elementoImg = elementoAImagem.find_element(By.TAG_NAME,"img")
atributoSrc = elementoImg.get_attribute("src")
print(atributoSrc)

driver.get("https://www.melhorcambio.com/dolar-hoje")

elementoCotacao = driver.find_element(By.ID,"comercial")
valorCotacao = elementoCotacao.get_attribute("value")
classeElemento = elementoCotacao.get_attribute("class")
tipoElemento = elementoCotacao.get_attribute("type")

print(valorCotacao)
print(classeElemento)
print(tipoElemento)

driver.close()