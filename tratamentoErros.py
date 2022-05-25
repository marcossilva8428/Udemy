from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

#driver.get("https://www.magazineluiza.com.br/iphone-11-apple-128gb-preto-61-12mp-ios/p/155611100/te/ip11/")

driver.get("https://www.magazineluiza.com.br/copo-long-drink-330ml-translucido-25-unidades-rep/p/kf55ggeff0/ud/cpdk/")

driver.implicitly_wait(3) # seconds

#avaliacao = driver.find_element(By.CLASS_NAME,"js-rating-value").text

try:
    avaliacao = driver.find_element(By.CLASS_NAME,"js-rating-value").text
except:
    avaliacao = "Não avaliado"

print(avaliacao)