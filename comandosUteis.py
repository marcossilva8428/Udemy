from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://gshow.globo.com/realities/bbb/")

driver.implicitly_wait(2) #seconds

driver.minimize_window()

driver.implicitly_wait(2) #seconds

driver.maximize_window()

driver.implicitly_wait(2) #seconds

driver.get("https://www.mercadolivre.com.br/apple-iphone-11-128-gb-branco/p/MLB15149568?pdp_filters=category:MLB1055#searchVariation=MLB15149568&position=1&search_layout=stack&type=product&tracking_id=b4df068f-0756-40fb-baa1-1e8a9a5d0729")

driver.back()

driver.implicitly_wait(2) #seconds

driver.forward()

driver.refresh()

driver.implicitly_wait(2) #seconds

driver.close


