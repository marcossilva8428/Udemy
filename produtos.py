from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\marcos.da.silva.j\OneDrive - Accenture\Desktop\scripts-python\novo_curso_python\chromedriver.exe")

driver.get("https://br.gearbest.com/celulares-c_11293/")

driver.implicitly_wait(2) #seconds

listaLinks = []

existePagina = True
primeiraPagina = True

while (existePagina):
    if(primeiraPagina):
        primeiraPagina = False
    else:
        try:
            driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[1]/div/footer/div[2]/div/a[5]/i').click()
            driver.implicitly_wait(3) # seconds
        except:
            print("Acabaram as páginas")
            existePagina = False
            driver.close()

    for produtoAtual in driver.find_elements(By.CLASS_NAME,'gbGoodsItem_outBox'):
        link = produtoAtual.find_element(By.TAG_NAME,'a')
        listaLinks.append(link.get_attribute('href'))
    
    for linkAtual in listaLinks:
        driver.get(linkAtual)
        driver.implicitly_wait(3) #seconds
        nomeProduto = driver.find_element(By.CLASS_NAME,'goodsIntro_title').text
        preco = driver.find_element(By.ID,'js-panelIntroNormalPrice').find_element(By.TAG_NAME,'span').text
        try:
            avaliacao = driver.find_element(By.CLASS_NAME,'gbStartGrade_count').text
        except:
            avaliacao = 'Sem avaliação'
        
        print(nomeProduto)
        print(preco)
        print(avaliacao)