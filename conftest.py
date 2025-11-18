import pytest
from utils.driver_manager import DriverManager

@pytest.fixture
def driver():
    # cria o manager em modo headless
    dm = DriverManager(headless=True)

    # inicializa o Chrome
    d = dm.get_driver()

    # entrega o driver ao teste
    yield d

    # fecha o navegador após o teste
    d.quit()
