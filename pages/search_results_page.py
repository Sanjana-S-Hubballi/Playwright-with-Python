# pages/search_results_page.py

class SearchResultsPage:
    def __init__(self, page):
        self.page = page
        self.first_product_link = 'a[href="/product_details/1"]'

    def view_first_product(self):
        self.page.click(self.first_product_link)