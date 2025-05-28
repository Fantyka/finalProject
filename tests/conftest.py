from selenium import webdriver
import pytest

@pytest.fixture
def setup():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get('https://katalon-demo-cura.herokuapp.com/profile.php#login')

    yield driver

    driver.close()