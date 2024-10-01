from selene import browser
from selenium import webdriver
import pytest
@pytest.fixture(scope='function', autouse=True)
def test_1():
    browser.config.base_url = "https://demoqa.com/automation-practice-form"
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')  # вместо этой строки можно добавить другие опции
    browser.config.driver_options = driver_options
    browser.config.timeout = 3.0
    yield
    browser.quit()
