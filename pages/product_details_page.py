# pages/product_details_page.py

class ProductDetailsPage:
    def __init__(self, page):
        self.page = page
        self.product_info = '.product-information'
        self.add_to_cart_button = 'button.btn.btn-default.cart'
        self.modal_view_cart_button = '#cartModal a[href="/view_cart"]'

    def is_product_details_visible(self):
        return self.page.is_visible(self.product_info)

    def add_to_cart(self):
        self.page.click(self.add_to_cart_button)
        self.page.wait_for_selector(self.modal_view_cart_button, state='visible')

    def view_cart(self):
        self.page.click(self.modal_view_cart_button)