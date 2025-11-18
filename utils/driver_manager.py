from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Classe para gerenciar a criação do WebDriver do Chrome
class DriverManager:
    # param headless: Se True, roda o navegador em modo headless (sem interface gráfica)
    def __init__(self, headless=False):
        self.headless = headless

    # Inicializa e retorna uma instância do Chrome WebDriver configurada
    def get_driver(self):
        options = Options()
        if self.headless:
            options.add_argument('--headless=new')
            
        # Configura o serviço do ChromeDriver usando webdriver_manager
        service = Service(ChromeDriverManager().install())

        # Cria a instância do WebDriver
        driver = webdriver.Chrome(service=service, options=options)

        # Define espera implícita de 5 segundos para encontrar elementos
        driver.implicitly_wait(5)
        
        return driver
