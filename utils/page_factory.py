class PageFactory:

    def __init__(self, driver,  testname):
        self.driver = driver
        self.testname = testname

    def get_login_page(self):
        from pages.login_page import LoginPage
        return LoginPage(self.driver, self.testname)

    def get_inventory_page(self):
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver, self.testname)

    def get_cart_page(self):
        from pages.cart_page import CartPage
        return CartPage(self.driver, self.testname)

    def get_checkout_page(self):
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver, self.testname)

    def get_payment_page(self):
        from pages.payment_page import PaymentPage
        return PaymentPage(self.driver, self.testname)

    def get_confirmation_page(self):
        from pages.confirmation_page import ConfirmationPage
        return ConfirmationPage(self.driver, self.testname)



