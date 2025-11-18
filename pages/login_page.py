# Importa o módulo para localizar elementos na página
from selenium.webdriver.common.by import By

class LoginPage:
    # URL da página de login
    URL = "https://example.com/login"

    # Recebe a instância do WebDriver (Chrome, Firefox, etc.) e armazena na variável self.driver para uso nos métodos.
    def __init__(self, driver):
        self.driver = driver

    # Abre a página de login no navegador. Chama o driver.get() com a URL definida na classe.
    def acessar(self):
        self.driver.get(self.URL)

    # Realiza o login
    def login(self, user, pwd):
        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(pwd)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Verifica se o login foi bem-sucedido
    def sucesso(self):
        return "profile" in self.driver.page_source
