class HomePage:
    def __init__(self, page):
        self.page = page
        self.logo_selector = 'img[alt="Website for automation practice"]'
        self.products_link = 'a[href="/products"]'

    def goto(self):
        self.page.goto("https://automationexercise.com/")

    def is_home_page_visible(self):
        return self.page.is_visible(self.logo_selector)

    def goto_products(self):
        self.page.click(self.products_link)