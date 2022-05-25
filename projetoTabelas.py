from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://br.investing.com/commodities/crude-oil-historical-data")

try:
    driver.find_element(By.ID,'onetrust-accept-btn-handler').click()
    driver.find_element(By.XPATH,'//*[@id="PromoteSignUpPopUp"]/div[2]/i').click()
except:
    print('Não existe alerta!')

driver.implicitly_wait(6) #seconds

try:
    driver.find_element(By.CSS_SELECTOR,'#PromoteSignUpPopUp > div.right > i').click()
except:
    print('Não eciste alerta!')

driver.find_element(By.ID,'widgetFieldDateRange').click()

dataInicial = driver.find_element(By.ID,'startDate')
dataFim = driver.find_element(By.ID,'endDate')

dataInicial.clear()
dataFim.clear()

dataInicial.send_keys('10/01/2019')
dataFim.send_keys('01/01/2021')

driver.find_element(By.ID,'applyBtn').click()

dados = []
dadosTabela = driver.find_element(By.ID,'curr_table')

for linha in dadosTabela.find_elements(By.TAG_NAME,'tr'):
    linhaDados = []
    for coluna in linha.find_elements(By.TAG_NAME,'td'):
        linhaDados.append(coluna.text)
        dados.append(linhaDados)

df = pd.DataFrame(dados)
df = df.iloc[1: , :]

df.columns = ['Data', 'Ultimo', 'Abertura', 'Maxima', 'Minima', 'Vol', 'Var%']

print(df)

# saving the dataframe

df.to_csv('dadosOil.csv')

