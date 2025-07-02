# pages/products_page.py

class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.all_products_header = 'h2.title.text-center'
        self.products_list = '.features_items'
        self.first_product_view_product = '(//a[contains(text(),"View Product")])[1]'

    def is_all_products_visible(self):
        return self.page.is_visible(self.all_products_header)

    def is_products_list_visible(self):
        return self.page.is_visible(self.products_list)

    def view_first_product(self):
        # Wait for element to be visible and clickable
        self.page.wait_for_selector(self.first_product_view_product, state='visible')
        # Scroll into view automatically handled by Playwright’s click()
        self.page.click(self.first_product_view_product)