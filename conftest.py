import pytest
from utils.driver_manager import DriverManager

@pytest.fixture
def driver():
    dm = DriverManager(headless=True)
    d = dm.get_driver()
    yield d
    d.quit()
