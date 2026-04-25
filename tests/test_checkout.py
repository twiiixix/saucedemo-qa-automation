from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def test_successful_checkout(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack_to_cart()
    inventory.open_cart()

    checkout.start_checkout()
    checkout.enter_customer_info("Terry", "Wesley", "89101")
    checkout.finish_checkout()

    assert checkout.get_confirmation_message() == "Thank you for your order!"