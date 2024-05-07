
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

#pesquisador
class Pesquisador:
  def __init__(self):
    self.options = Options()
    self.options.add_argument('--headless')
    self.options.add_argument('--no-sandbox')
    self.options.add_argument('--disable-dev-shm-usage')
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
    self.driver.get("https://www.google.com/")

  #faz pesquisa
  def pesquisar(self, input):
    #Inicializando navegador
    
    searchInput = self.driver.find_element(By.NAME, "q")
    searchInput.click()
    searchInput.send_keys(input)
    searchInput.send_keys(Keys.ENTER)
    
    #clica em ferramentas
    ferramentasButton = self.driver.find_element(By.ID, "hdtb-tls")
    ferramentasButton.click()
    
    #texto de resultados
    results = self.driver.find_element(By.ID, "result-stats").get_attribute("textContent")
    results = ((results.split(" ")[1]))
    results_num = float(results.replace(".",""))
    return results_num

pesquisador = Pesquisador()

print(pesquisador.pesquisar("romulo calado pantaleão camara"))
print(pesquisador.pesquisar("vasco"))
