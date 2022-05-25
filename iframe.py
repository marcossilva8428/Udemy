from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/derivativos/ajustes-do-pregao/")

driver.switch_to.frame('bvmf_iframe')

tabela = driver.find_element(By.ID,'tblDadosAjustes')

m = []

for linha in tabela.find_elements(By.TAG_NAME,'tr'):
    linhaDados = []
    for coluna in linha.find_elements(By.TAG_NAME,'td'):
        linhaDados.append(coluna.text)
    m.append(linhaDados)

df = pd.DataFrame(m)
print(df)