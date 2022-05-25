from pandas import options
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs",{
  "download.default_directory": r"C:\Users\marcos.da.silva.j\Downloads",
  "download.prompt_for_download":False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Chrome(chrome_options=options,executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://www.opera.com/pt-br/download")

try:
    # driver.find_element(By.ID,'onetrust-accept-btn-handler').click()
    driver.find_element(By.XPATH,'//*[@id="cookie-consent"]/div[1]/div/div/span[1]').click()
except:
    print('Não existe alerta!')

spanBotao = driver.find_element(By.XPATH,'/html/body/main/section[1]/div[2]/div[2]/span')
linkBotao = spanBotao.find_element(By.TAG_NAME,'a')
linkBotao.click()