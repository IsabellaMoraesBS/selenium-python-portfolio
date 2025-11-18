# Importa a página de login
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Teste de login usando pytest.
def test_login(driver):
    
    # Cria a instância da página, fornecendo o driver do navegador
    page = LoginPage(driver)

    # Abre a página de login
    page.acessar()

    # Realiza login com usuário e senha
    page.login("user", "pass")

    # Verifica se o login foi bem-sucedido
    assert page.sucesso()

    # Role a tela para baixo (200 pixels)
    driver.execute_script("window.scrollBy(0, 200);")
    
    # Aguarda até que o botão esteja clicável
    botao = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "meu-botao"))
    )
    
    # Clica no botão
    botao.click()
