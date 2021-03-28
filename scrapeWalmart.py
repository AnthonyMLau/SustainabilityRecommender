from urllib.request import urlopen

class ScrapeWalmart:
    def __init__(self):
        self.home = "https://www.walmart.ca/"
        # dictionary of arrays containing product name and sku info and quantities
        self.data = {}

    def __call__(self, cart_url):
        page = self.get_cart_page(cart_url)
        self.get_food_items(page)

    def get_cart_page(self, cart_link):
        page = urlopen(cart_link)
        decoded_page = page.read().decode("utf-8")
        return decoded_page

    def get_food_items(self, page):
        print(page.find("product-item-title"))

if __name__ == "__main__":
    scraper = ScrapeWalmart()
    scraper("")
