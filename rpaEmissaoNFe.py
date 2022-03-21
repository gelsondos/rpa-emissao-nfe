from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Redirect the path to locate my webdrive
driver= webdriver.Chrome(executable_path="/Users/gelson/Desktop/CODE/rpa-emissao-nfe/Drivers/chromedriver")

driver.get("https://receita.pr.gov.br/login")

#login in page
login=driver.find_element(By.ID,"cpfusuario")
login.send_keys("05750629910")

#password in page and click
passWord=driver.find_element(By.NAME,"senha")
passWord.send_keys("Gel0255762son", Keys.ENTER)

#wait and start fill first page "Emitente"

driver.get("https://nfae.fazenda.pr.gov.br/nfae/avulsa/emitir/emitente")
driver.implicitly_wait(1)
telefoneEmitente=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div/div[1]/div[1]/div[2]/div[5]/div[1]/input')
telefoneEmitente.send_keys("41984993475")
avancar=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div/div[2]/button')
print("finaly")





