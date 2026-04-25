from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_logout(driver):
    login = LoginPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "logout_sidebar_link").click()

    assert "saucedemo.com" in driver.current_url