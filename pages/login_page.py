from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://example.com/login"

    def __init__(self, driver):
        self.driver = driver

    def acessar(self):
        self.driver.get(self.URL)

    def login(self, user, pwd):
        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "password").send_keys(pwd)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def sucesso(self):
        return "profile" in self.driver.page_source
