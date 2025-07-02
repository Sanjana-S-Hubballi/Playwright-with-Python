# pages/cart_page.py

class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_table = '#cart_info_table'
        self.product_in_cart = lambda name: f'//a[contains(text(),"{name}")]'
        self.product_price = '#product-1 .cart_price p'
        self.product_quantity = '#product-1 .cart_quantity button'
        self.product_total = '#product-1 .cart_total p'

    def is_product_in_cart(self, product_name):
        return self.page.is_visible(self.product_in_cart(product_name))

    def get_product_price(self):
        return self.page.inner_text(self.product_price)

    def get_product_quantity(self):
        return self.page.inner_text(self.product_quantity)

    def get_product_total(self):
        return self.page.inner_text(self.product_total)