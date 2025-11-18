from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class DriverManager:
    def __init__(self, headless=False):
        self.headless = headless

    def get_driver(self):
        options = Options()
        if self.headless:
            options.add_argument('--headless=new')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(5)
        return driver
