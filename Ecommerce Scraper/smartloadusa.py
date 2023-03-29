import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class Initializer:
    def __init__(self):
        self.category_link_lst = []
        self.product_link_lst = []

class Browser:
    def session(self):
        self.driver = webdriver.Chrome()

class Scraper(Initializer, Browser):
    def login(self, filename):
        with open(filename) as f:
            email = f.readline().strip()
            password = f.readline().strip()

        time.sleep(5)
        login = self.driver.find_element(By.XPATH, '//a[@class="nav-top-link nav-top-not-logged-in is-small"]')
        login.click()
        time.sleep(5)

        email_input = self.driver.find_element(By.XPATH, '//input[@name="username"]')
        email_input.send_keys(email)
        time.sleep(3)

        password_input = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        password_input.send_keys(password)
        time.sleep(3)

        login_btn = self.driver.find_element(By.XPATH, '//button[@name="login"]')
        login_btn.click()
        time.sleep(10)

    def collect_categories(self):
        category_btn = self.driver.find_element(By.XPATH, '//li[@class="html header-button-1"]')
        category_btn.click()

        categories = self.driver.find_elements(By.XPATH, '//ul[@class="product-categories"]/li/a')
        for category in categories:
            self.category_link_lst.append(category.get_attribute('href'))

    def collect_products(self):
        flag = False
        for i in self.category_link_lst:
            self.driver.get(i)
            time.sleep(2)
            while flag == False:
                products = self.driver.find_elements(By.XPATH, '//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]')

                for product in products:
                    self.product_link_lst.append(product.get_attribute('href'))

                body = self.driver.find_element(By.TAG_NAME, "body")
                body.send_keys(Keys.PAGE_DOWN)
                time.sleep(10)
                last_height = self.driver.execute_script("return document.body.scrollHeight")
                if self.driver.execute_script("return window.pageYOffset + window.innerHeight") >= last_height:
                    time.sleep(5)
                    break

        self.product_lst = list(set(self.product_link_lst))

    def collect_product_info(self):
        self.product_title_lst = []
        self.product_sku_lst = []
        self.product_price_lst = []
        self.product_barcode_lst = []

        for i in self.product_lst:
            self.driver.get(i)
            time.sleep(5)

            try:
                product_title = self.driver.find_element(By.XPATH, '//h1[@class="product-title product_title entry-title"]')
                self.product_title_lst.append(product_title.text)
                time.sleep(1)
            except:
                self.product_title_lst.append("Not Found")

            try:
                product_sku = self.driver.find_element(By.XPATH, '//span[@class="sku"]')
                self.product_sku_lst.append(product_sku.text)
                time.sleep(1)
            except:
                self.product_sku_lst.append("Not Found")

            try:
                product_price = self.driver.find_element(By.XPATH, '//p[@class="price product-page-price "]')
                self.product_price_lst.append(product_price.text)
                time.sleep(1)
            except:
                self.product_price_lst.append("Not Found")

            try:
                product_barcode = self.driver.find_element(By.XPATH, '//tr[@class="woocommerce-product-attributes-item woocommerce-product-attributes-item--attribute_bar-code"]/td/p')
                self.product_barcode_lst.append(product_barcode.text)
                time.sleep(1)
            except:
                self.product_barcode_lst.append("Not Found")


class CSV(Scraper):
    def make_csv(self, csv_filename):
        with open(csv_filename, 'a', newline="", encoding="utf8") as f:
            csv_writer = csv.writer(f)
            columns = ['Title', 'SKU', 'Price', 'Barcode']
            csv_writer.writerow(columns)

    def populate_csv(self, csv_filename):
        with open(csv_filename, 'a', newline="", encoding="utf8") as f:
            csv_writer = csv.writer(f)
            for i,j,k,l in zip(self.product_title_lst,self.product_sku_lst,self.product_price_lst,self.product_barcode_lst):
                data = [i,j,k,l]
                csv_writer.writerow(data)


class Scraper_Implementor(CSV):
    def implementor(self, filename, url, csv_filename):
        super().session()
        self.driver.get(url)
        super().login(filename)
        super().collect_categories()
        super().collect_products()
        super().collect_product_info()
        super().make_csv(csv_filename)
        super().populate_csv(csv_filename)


obj = Scraper_Implementor()
obj.implementor('credentials.txt', 'https://smartloadusa.com/', 'smartloadusa.csv')