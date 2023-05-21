import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Initializer:
    def __init__(self):
        self.category_link_lst = []
        self.product_link_lst = []

class Browser:
    def session(self):
        self.driver = webdriver.Chrome()

class Scraper(Initializer, Browser):
    def collect_categories(self):
        # jordan = self.driver.find_element(By.XPATH, '//div[@class="tier-1"]/ul/li[1]/a')
        nike = self.driver.find_element(By.XPATH, '//div[@class="tier-1"]/ul/li[2]/a')
        # yeezy = self.driver.find_element(By.XPATH, '//div[@class="tier-1"]/ul/li[3]/a')
        # addidas = self.driver.find_element(By.XPATH, '//div[@class="tier-1"]/ul/li[4]/a')
        self.category_link_lst.extend([nike.get_attribute('href')])
        print(self.category_link_lst)


    def collect_product_info(self, filename, category):
            wait = WebDriverWait(self.driver, 20)

            # time.sleep(1)
            product_link = []
            product_link.append(self.driver.current_url)
            print(self.driver.current_url)

            # time.sleep(1)
            # product id
            product_id = []

            # time.sleep(1)
            # Model
            model_lst = []
            try:
                model = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="pdp-product-info-col"]/span[@class="pdp-body-text"]')))
                model_lst.append(model.text)
                print(model.text)
            except:
                model_lst.append("Not Found")
            
            # time.sleep(1)
            # Images
            image_lst = []
            try:
                image = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="product-media product-media--image"]/div/img')))
                image_lst.append(image.get_attribute('src'))
                print(image.get_attribute('src'))
            except:
                image_lst.append("Not Found")
            
            # time.sleep(1)
            # price
            price_lst = []
            try:
                price = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="product-detail__form"]/div[@class="price-area product-detail__gap-sm"]/span')))
                price_lst.append(price.text)
                print(price.text)
            except:
                price_lst.append("Not Found")

            # time.sleep(1)
            # name
            title_lst = []
            brand_lst = []
            try:
                title = wait.until(EC.presence_of_element_located((By.XPATH, '//h1[@class="product-area__details__title product-detail__gap-sm h2"]')))
                title_lst.append(title.text)
                print(title.text)
                air = 'Jordan'
                nike = 'Nike'
                adidas = 'Adidas'
                yeezy = 'Yeezy'
                if air.lower() in title.text.lower():
                    brand_lst.append("Air Jordan")
                elif nike.lower() in title.text.lower():
                    brand_lst.append("Nike")
                elif adidas.lower() in title.text.lower():
                    if yeezy.lower() in title.text.lower():
                        brand_lst.append('Yeezy')
                    else:
                        brand_lst.append('Adidas')
            except:
                title_lst.append("Not Found")

            # Description
            # time.sleep(1)
            description_lst = []
            try:
                description_tab = self.driver.find_element(By.XPATH, '//div[@class="cc-tabs__tab"][4]')
                description_tab.click()
                time.sleep(1)
                description = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="cc-tabs__tab"][4]/div/p[@hidden]')))
                self.driver.execute_script("arguments[0].setAttribute('style', 'display: block;');", description)
                description_lst.append(description.text)
                print(description.text)
            except:
                description_lst.append("Not Found")

            # time.sleep(1)
            # meta_title
            meta_title_lst = []
            try:
                meta_title = wait.until(EC.presence_of_element_located((By.XPATH,'//meta[@name="title"]')))
                meta_title_lst.append(meta_title.get_attribute('content'))
            except:
                meta_title_lst.append("Not Found")

            
            # time.sleep(1)
            # meta description
            meta_desc_lst = []
            try:
                meta_desc = wait.until(EC.presence_of_element_located((By.XPATH, '//meta[@property="og:description"]')))
                meta_desc_lst.append(meta_desc.get_attribute('content'))
            except:
                meta_desc_lst.append("Not Found")

            time.sleep(1)
            # additional images
            additional_image_lst = []
            add_image = []
            try:
                images = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="product-media product-media--image"]/div/img')))
                for i in images:
                    add_image.append(i.get_attribute('src'))
                    print(i.get_attribute('src'))
                my_string = '|'.join(add_image)
                additional_image_lst.append(my_string)
                    
            except:
                additional_image_lst.append("Not Found")

            # time.sleep(2)
            # product_attributes
            attributes_lst = []
            product_attribute_lst = []
            try:
                labels = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="pdp-product-info-col"]//h3')))
                values = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="pdp-product-info-col"]//span')))
                try:
                    heading = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="cc-tabs__tab"][1]/div/h3')))
                except:
                    heading = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="cc-tabs__tab"][1]/h2')))
                time.sleep(2)
                for label, value in zip(labels, values):
                    attribute = "{}:{}:{}".format(heading.text, label.text, value.text)
                    attributes_lst.append(attribute)

                my_string = '|'.join(attributes_lst)
                product_attribute_lst.append(my_string)

            except:
                product_attribute_lst.append("Not Found")


            # time.sleep(1)
            # product category
            product_cat = []
            try:
                product_category = category
                sub_category = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="vendor product-detail__gap-sm"]/span')))
                category_string = "{}|{}>{}".format(product_category, product_category, sub_category.text)
                product_cat.append(category_string)
            except:
                product_cat.append("Not Found")


            # time.sleep(2)
            product_options_lst = []
            options_lst = []
            try:
                sizes = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-option-name="Size"]//div[@class="clickyboxes clickyboxes-sq-picker-grid cc-init"]/div/a[@data-qty="qty"]/label/span[1]')))
                size_prices = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-option-name="Size"]//div[@class="clickyboxes clickyboxes-sq-picker-grid cc-init"]/div/a[@data-qty="qty"]/label/span[2]')))
                for shoe_size, size_price in zip(sizes, size_prices):
                    product_option = "select:Sizes:{}:+{}.0000.100:1:+0.00000000:1:".format(shoe_size.text, size_price.text)
                    options_lst.append(product_option)

                my_string = '|'.join(options_lst)
                product_options_lst.append(my_string)

            except:
                product_options_lst.append("Not Found")

            
            data = []
            data.extend([product_id, model_lst, 100, image_lst, price_lst, product_link, title_lst, description_lst, meta_title_lst, meta_desc_lst, additional_image_lst, product_attribute_lst, brand_lst, product_cat, product_options_lst])

            with open(filename, 'a', encoding='utf8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(data)




    def collect_products(self,filename):
        global next_btn
        wait = WebDriverWait(self.driver, 5)
        for i in self.category_link_lst:
            self.driver.get(i)
            time.sleep(2)
            categories = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@data-widget="product-types"]//ul//li//a')))
            category_lst = []
            for category in categories:
                category_lst.append(category.get_attribute('href'))
                
            
            for i in category_lst:
                product_link_lst = []
                self.driver.get(i)
                print(i)
                print('yes')
                category_name = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@class="ais-Menu-item ais-Menu-item--selected"]/div/a/span[1]')))
                b = category_name.text
                try:
                    next_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="Next"]')))
                except:
                    products = self.driver.find_elements(By.XPATH, '//li[@class="ais-Hits-item"]/article/a')
                    for product in products:
                        product_link_lst.append(product.get_attribute('href'))
                        print(product.get_attribute('href'))

                while next_btn:
                    products = self.driver.find_elements(By.XPATH, '//li[@class="ais-Hits-item"]/article/a')
                    for product in products:
                        product_link_lst.append(product.get_attribute('href'))
                        print(product.get_attribute('href'))
                    try:
                        next_link = self.driver.find_element(By.XPATH, '//a[@aria-label="Next"]')
                        a = next_link.get_attribute('href')
                    except:
                        break

                    self.driver.get(a)
                

                for j in product_link_lst:
                    self.driver.get(j)

                    self.collect_product_info(filename, category=b)


            
class CSV():
    def make_csv(self, filename):
        with open(filename, 'w', encoding='utf8', newline='') as f:
            csv_writer = csv.writer(f)
            columns = ['Product ID','Model','Quantity','Image','Price','Link','Name_en','Description_en','Meta_title_en','Meta_description_en','Additional_Image','Product_Attributes','Brand','Product_Category','Product_Option']
            csv_writer.writerow(columns)

class Scraper_Implementor(Scraper,CSV):
    def implementor(self, url, filename):
        super().session()
        super().make_csv(filename)
        self.driver.get(url)
        super().collect_categories()
        super().collect_products(filename)
        

        

filename = 'product_sample7.csv'
obj = Scraper_Implementor()
obj.implementor('https://www.kickscrew.com/', filename)