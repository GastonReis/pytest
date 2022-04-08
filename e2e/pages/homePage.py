import imp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.action_chains import ActionChains


class HomePage():

    BASE_URL = "http://automationpractice.com/"

    def __init__(self, driver) -> None:
        self.driver = driver
        self.driver.get(self.BASE_URL)


    def search(self, string):
        searchInput = self.driver.find_element(By.ID, "search_query_top")
        searchInput.send_keys(string)
        searchInput.send_keys(Keys.ENTER)

    def get_products_titles(self):
        titlesElements = self.driver.find_elements(By.XPATH, '//*[@class="product_list grid row"]//a[@class="product-name"]')
        return [title.text for title in titlesElements]

    def add_first_item_to_cart(self):
        products = "//span[text()='Add to cart']"
        #visibility_of_element_located(products)
        product = self.driver.find_element(By.XPATH, products)
        hover = ActionChains(self.driver).move_to_element(product)
        hover.perform()
        product.click()
        self.driver.find_element(By.XPATH, "//a[@title='Proceed to checkout']").click()

    def get_cart_products_quantity(self):
        self.driver.find_element(By.XPATH, "//div[@class='shopping_cart']//span[@class='ajax_cart_quantity']").text()
