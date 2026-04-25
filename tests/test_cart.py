from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_item_to_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack_to_cart()
    inventory.open_cart()

    assert "cart" in driver.current_url


def test_remove_item_from_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack_to_cart()
    inventory.remove_backpack_from_cart()

    assert "Remove" not in driver.page_source