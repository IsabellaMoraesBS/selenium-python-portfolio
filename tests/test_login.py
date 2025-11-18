from pages.login_page import LoginPage

def test_login(driver):
    page = LoginPage(driver)
    page.acessar()
    page.login("user", "pass")
    assert page.sucesso()
