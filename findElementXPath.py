from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

driver.implicitly_wait(6) #seconds

valorTabela = driver.find_elements(By.XPATH,'/html/body/main/div[2]/div[8]/div/div[6]/div/div[2]/table/tbody/tr[3]/td[3]')[0].text

proventos = driver.find_elements(By.XPATH,'//*[@id="earning-section"]/div[6]/div/div[1]/div[4]/div/div/strong')[0].text

volumeAluguel = driver.find_elements(By.XPATH,'/html/body/main/div[2]/div[11]/div[2]/div[4]/div/div/strong')[0].text

nomeAdministrador = driver.find_elements(By.XPATH,'/html/body/main/div[3]/div/div/div[3]/div/div[2]/div[1]/div/strong')[0].text

print(valorTabela)
print('-------')
print(proventos)
print('-------')
print(volumeAluguel)
print('-------')
print(nomeAdministrador)