import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Initializer:
    def __init__(self):
        self.category_link_lst = []
        self.product_link_lst = ['https://www.kickscrew.com/products/jordan-legacy-thinker-bq0296-423', 'https://www.kickscrew.com/products/air-jordan-essential-jacket-dv7617-274', 'https://www.kickscrew.com/products/air-jordan-x-travis-scott-do4103-256', 'https://www.kickscrew.com/products/air-jordan-jacket-x-solefly-light-smoke-grey-dv7515-077', 'https://www.kickscrew.com/products/air-jordan-x-travis-scott-jacket-do4104-256', 'https://www.kickscrew.com/products/air-jordan-x-travis-scott-woven-jacket-do4096-010', 'https://www.kickscrew.com/products/air-jordan-x-travis-scott-woven-jacket-do4095-010', 'https://www.kickscrew.com/products/air-jordan-x-solefly-jacket-dv7516-077', 'https://www.kickscrew.com/products/air-jordan-23-engineered-jacket-dq8057-712', 'https://www.kickscrew.com/products/air-jordan-essentials-statement-jacket-dq7345-680', 'https://www.kickscrew.com/products/air-jordan-logo-dv1283-206', 'https://www.kickscrew.com/products/air-jordan-x-dj9771-203', 'https://www.kickscrew.com/products/air-jordan-logo-dx6596-010', 'https://www.kickscrew.com/products/air-jordan-logo-dq8105-612', 'https://www.kickscrew.com/products/air-jordan-logo-dv5634-010', 'https://www.kickscrew.com/products/air-jordan-logo-dv5634-244', 'https://www.kickscrew.com/products/air-jordan-logo-dx6596-781', 'https://www.kickscrew.com/products/air-jordan-logo-885874-010', 'https://www.kickscrew.com/products/air-jordan-logo-716847-021', 'https://www.kickscrew.com/products/air-jordan-logo-dz4554-256', 'https://www.kickscrew.com/products/air-jordan-logo-931835-011', 'https://www.kickscrew.com/products/air-jordan-fw22-logo-dq8060-010', 'https://www.kickscrew.com/products/air-jordan-logo-ah3932-063', 'https://www.kickscrew.com/products/jordan-x-maison-chateau-rouge-do4092-226', 'https://www.kickscrew.com/products/air-jordan-x-maison-chateau-rouge-do4162-226', 'https://www.kickscrew.com/products/jordan-dc9655-010', 'https://www.kickscrew.com/products/jordan-dm1868-579', 'https://www.kickscrew.com/products/jordan-dm1864-010', 'https://www.kickscrew.com/products/nike-jordan-ss22-dj0243-241', 'https://www.kickscrew.com/products/nike-jordan-ss22-dj0253-010', 'https://www.kickscrew.com/products/nike-jordan-dh9038-010', 'https://www.kickscrew.com/products/nike-jordan-ss22-dj0253-455', 'https://www.kickscrew.com/products/nike-jordan-x-mitchell-ness-mj-dunk-champ-cw0884-100', 'https://www.kickscrew.com/products/nike-jordan-da9855-010', 'https://www.kickscrew.com/products/air-jordan-sportswear-flight-tech-887777-010', 'https://www.kickscrew.com/products/nike-jordan-wings-diamond-ci7916-355', 'https://www.kickscrew.com/products/air-jordan-ck1353-091', 'https://www.kickscrew.com/products/nike-jordan-av1303-854', 'https://www.kickscrew.com/products/nike-jordan-cd8734-010', 'https://www.kickscrew.com/products/nike-jordan-822659-010', 'https://www.kickscrew.com/products/nike-jordan-jumpman-classic-logo-ck2223-011', 'https://www.kickscrew.com/products/nike-jordan-sport-dna-cd5748-010', 'https://www.kickscrew.com/products/jordan-x-mitchell-ness-1988-all-star-warm-up-jacket-cw0884-657', 'https://www.kickscrew.com/products/air-jordan-flight-ao0556-272', 'https://www.kickscrew.com/products/nike-jordan-logo-ck1343-010', 'https://www.kickscrew.com/products/air-jordan-jumpman-classics-dh9507-010', 'https://www.kickscrew.com/products/nike-jordan-wings-bq4171-347', 'https://www.kickscrew.com/products/nike-jordan-bq5650-010', 'https://www.kickscrew.com/products/nike-jordan-ma-1-db3693-010', 'https://www.kickscrew.com/products/air-jordan-ao0423-011', 'https://www.kickscrew.com/products/nike-jordan-924676-010', 'https://www.kickscrew.com/products/jordan-jumpman-men-s-jacket-grey-ar2249-091', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-dc9657-387', 'https://www.kickscrew.com/products/nike-jordan-ct9369-011', 'https://www.kickscrew.com/products/nike-jordan-wings-diamond-ci7916-010', 'https://www.kickscrew.com/products/air-jordan-x-travis-scott-track-logo-ck4035-260', 'https://www.kickscrew.com/products/nike-jordan-ci0254-657', 'https://www.kickscrew.com/products/nike-jordan-ck9566-010', 'https://www.kickscrew.com/products/nike-jordan-wings-bq4171-059', 'https://www.kickscrew.com/products/jordan-jacket-men-s-red-av2291-687', 'https://www.kickscrew.com/products/nike-jordan-flight-fleece-cv6145-010', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-cv2787-010', 'https://www.kickscrew.com/products/nike-jordan-wings-ma-1-logo-av2599-010', 'https://www.kickscrew.com/products/air-jordan-sports-hooded-jacket-men-black-cu2775-010', 'https://www.kickscrew.com/products/nike-jordan-777500-010', 'https://www.kickscrew.com/products/air-jordan-ck2218-072', 'https://www.kickscrew.com/products/nike-jordan-nba-aj8954-010', 'https://www.kickscrew.com/products/nike-jordan-wings-ma-1-cd5458-100', 'https://www.kickscrew.com/products/nike-jordan-ct3555-010', 'https://www.kickscrew.com/products/nike-jordan-ck6448-010', 'https://www.kickscrew.com/products/nike-jordan-x-union-la-logo-db8260-072', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-printed-parka-cu8624-100', 'https://www.kickscrew.com/products/nike-air-air-jordan-29-637492-063', 'https://www.kickscrew.com/products/air-jordan-city-of-flight-ma-1-jacket-white-911314-100', 'https://www.kickscrew.com/products/nike-jordan-why-not-dc3242-230', 'https://www.kickscrew.com/products/air-jordan-ck2218-710', 'https://www.kickscrew.com/products/nike-jordan-x-union-la-logo-db8260-041', 'https://www.kickscrew.com/products/nike-jordan-ar4736-010', 'https://www.kickscrew.com/products/nike-jordan-cu2775-687', 'https://www.kickscrew.com/products/nike-jordan-dd0388-010', 'https://www.kickscrew.com/products/nike-jordan-jumpman-wave-ck6867-100', 'https://www.kickscrew.com/products/air-jordan-ck2218-100', 'https://www.kickscrew.com/products/nike-jordan-cv2356-091', 'https://www.kickscrew.com/products/nike-jordan-cv2356-010', 'https://www.kickscrew.com/products/nike-jordan-wings-ma-1-logo-av2599-100', 'https://www.kickscrew.com/products/nike-jordan-ao0423-108', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-da5623-010', 'https://www.kickscrew.com/products/air-jordan-sport-dna-ck9351-011', 'https://www.kickscrew.com/products/nike-jordan-ah6164-010', 'https://www.kickscrew.com/products/nike-jordan-wings-do6298-265', 'https://www.kickscrew.com/products/nike-jordan-ct3338-010', 'https://www.kickscrew.com/products/nike-jordan-jumpman-wave-ck6867-631', 'https://www.kickscrew.com/products/nike-jordan-ah6256-687', 'https://www.kickscrew.com/products/air-jordan-5-sportswear-ar3131-010', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-quilted-aj1055-010', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-ct3555-612', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-bq5766-347', 'https://www.kickscrew.com/products/jordan-x-union-la-coaches-jacket-men-beige-white-db8261-072', 'https://www.kickscrew.com/products/nike-jordan-diamond-cement-jacket-ar3243-010', 'https://www.kickscrew.com/products/air-jordan-sport-dna-ck9351-432', 'https://www.kickscrew.com/products/air-jordan-3-x-a-ma-maniere-cv3429-099', 'https://www.kickscrew.com/products/nike-jordan-ma-1-av5999-395', 'https://www.kickscrew.com/products/air-jordan-ah6162-010', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-cn4579-446', 'https://www.kickscrew.com/products/nike-jordan-x-union-la-logo-db8261-454', 'https://www.kickscrew.com/products/air-jordan-sport-dna-logo-dn3404-010', 'https://www.kickscrew.com/products/nike-jordan-aa1952-010', 'https://www.kickscrew.com/products/nike-jordan-dc9680-333', 'https://www.kickscrew.com/products/nike-jordan-bq5772-010', 'https://www.kickscrew.com/products/nike-jordan-legacy-aj11-cw0864-100', 'https://www.kickscrew.com/products/nike-jordan-logo-dh3289-220', 'https://www.kickscrew.com/products/air-jordan-jumpman-ao0445-100', 'https://www.kickscrew.com/products/nike-jordan-chinese-new-year-cv3488-219', 'https://www.kickscrew.com/products/nike-jordan-cv3289-010', 'https://www.kickscrew.com/products/nike-jordan-x-psg-bq8369-010', 'https://www.kickscrew.com/products/nike-jordan-939941-010', 'https://www.kickscrew.com/products/nike-jordan-cz2495-010', 'https://www.kickscrew.com/products/nike-jordan-logo-cu9123-010', 'https://www.kickscrew.com/products/nike-jordan-cj9097-010', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-ck8936-313', 'https://www.kickscrew.com/products/air-jordan-ah6162-121', 'https://www.kickscrew.com/products/nike-jordan-jumpman-da7173-010', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-cv2867-875', 'https://www.kickscrew.com/products/nike-jordan-av1303-011', 'https://www.kickscrew.com/products/nike-jordan-city-of-flight-at9006-010', 'https://www.kickscrew.com/products/nike-jordan-da9807-781', 'https://www.kickscrew.com/products/nike-jordan-wings-suit-jacket-logo-av1302-451', 'https://www.kickscrew.com/products/nike-jordan-x-union-la-logo-db8260-454', 'https://www.kickscrew.com/products/air-jordan-ah6256-010', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-dc9657-010', 'https://www.kickscrew.com/products/nike-jordan-bq5772-557', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-cv2787-875', 'https://www.kickscrew.com/products/jordan-wings-bq4171-010', 'https://www.kickscrew.com/products/air-jordan-logo-dh7727-687', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-ma-1-cq2465-010', 'https://www.kickscrew.com/products/nike-jordan-winter-utility-ct3380-100', 'https://www.kickscrew.com/products/nike-jordan-sportdna-da7166-010', 'https://www.kickscrew.com/products/air-jordan-x-clot-mesh-shorts-ar8401-010', 'https://www.kickscrew.com/products/nike-jordan-jumpman-windbreaker-cn3824-010', 'https://www.kickscrew.com/products/nike-jordan-924676-072', 'https://www.kickscrew.com/products/nike-jordan-sport-dna-logo-cv2774-412', 'https://www.kickscrew.com/products/nike-jordan-dj0239-010', 'https://www.kickscrew.com/products/air-jordan-jsw-j-3b-flight-parka-black-aa1952-011', 'https://www.kickscrew.com/products/air-jordan-logo-dh7727-010', 'https://www.kickscrew.com/products/nike-jordan-cd8734-606', 'https://www.kickscrew.com/products/air-jordan-5-legacy-sports-jacket-for-men-white-cu1667-100', 'https://www.kickscrew.com/products/nike-jordan-winter-utility-ct3380-010', 'https://www.kickscrew.com/products/air-jordan-jumpman-bq8476-010', 'https://www.kickscrew.com/products/air-jordan-x-travis-scott-track-logo-ck4036-260', 'https://www.kickscrew.com/products/nike-jordan-wings-ma-1v-cd5458-010', 'https://www.kickscrew.com/products/nike-jordan-dq0385-010', 'https://www.kickscrew.com/products/jordan-sportswear-jacket-men-black-ck1353-011', 'https://www.kickscrew.com/products/air-jordan-6-srt-lgc-nylon-jacket-bv5406-010', 'https://www.kickscrew.com/products/nike-jordan-jumpman-coaches-aj6796-010', 'https://www.kickscrew.com/products/nike-jordan-823065-091', 'https://www.kickscrew.com/products/nike-jordan-23-engineered-ct3555-110', 'https://www.kickscrew.com/products/nike-aq2684-010', 'https://www.kickscrew.com/products/nike-jordan-ma-1-ck1358-010', 'https://www.kickscrew.com/products/air-jordan-av2291-010', 'https://www.kickscrew.com/products/air-jordan-939969-100', 'https://www.kickscrew.com/products/air-jordan-23-engineered-flight-tech-aj1053-010', 'https://www.kickscrew.com/products/air-jordan-city-of-flight-911314-010', 'https://www.kickscrew.com/products/air-jordan-cny-chinese-new-year-ma-1-jacket-cd9046-010', 'https://www.kickscrew.com/products/air-jordan-cny-chinese-new-year-wings-fz-hoodie-ao1922-010', 'https://www.kickscrew.com/products/air-jordan-mens-jumpman-multicolor-tat-sports-jacket-white-cv2241-100', 'https://www.kickscrew.com/products/nike-as-m-men-s-j-sprt-dna-wvn-jkt-thermal-green-cd5729-370', 'https://www.kickscrew.com/products/as-m-j-jmc-jkt-smoke-grey-black-cz4825-084', 'https://www.kickscrew.com/products/air-jordan-flight-warmup-jacket-ao0556-687', 'https://www.kickscrew.com/products/nike-jordan-x-clot-tricot-jacket-black-ar8402-010', 'https://www.kickscrew.com/products/nike-jordan-performance-hybrid-black-807948-010', 'https://www.kickscrew.com/products/nike-jordan-icon-fleece-full-zip-black-809473-010', 'https://www.kickscrew.com/products/nike-wmns-air-jordan-as-j-sp-collective-dv1382-250', 'https://www.kickscrew.com/products/as-w-j-next-utility-jacket-black-iron-grey-dd7096-010', 'https://www.kickscrew.com/products/jordan-wmns-bomber-jacket-black-cz7500-010', 'https://www.kickscrew.com/products/nike-jordan-moto-lightweight-cu4156-891', 'https://www.kickscrew.com/products/as-w-j-lt-wt-jkt-future-white-white-da1521-100']

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


    def collect_product_info(self, filename):
            wait = WebDriverWait(self.driver, 20)
            for i in self.product_link_lst:
                self.driver.get(i)

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
                product_cat.append("SNEAKERS|SNEAKERS")
                # try:
                #     product_category = category
                #     sub_category = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="vendor product-detail__gap-sm"]/span')))
                #     category_string = "{}|{}>{}".format(product_category, product_category, sub_category.text)
                #     product_cat.append(category_string)
                # except:
                #     product_cat.append("Not Found")


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
                if i == 'https://www.kickscrew.com/collections/nike?product_type=Sneakers':
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
                            try:
                                oosbadge = self.driver.find_element(By.XPATH, "//span[contains(text(),'Out of Stock')]")
                            except:
                                product_link_lst.append(product.get_attribute('href'))
                                print(product.get_attribute('href'))

                    while next_btn:
                        products = self.driver.find_elements(By.XPATH, '//li[@class="ais-Hits-item"]/article/a')
                        for product in products:
                            try:
                                oosbadge = self.driver.find_element(By.XPATH, "//span[contains(text(),'Out of Stock')]")
                            except:
                                product_link_lst.append(product.get_attribute('href'))
                                print(product.get_attribute('href'))
                        
                        try:
                            next_link = self.driver.find_element(By.XPATH, '//a[@aria-label="Next"]')
                            a = next_link.get_attribute('href')
                        except:
                            break

                        self.driver.get(a)
                
                    print(len(product_link_lst))
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
        # self.driver.get(url)
        # super().collect_categories()
        # super().collect_products(filename)
        super().collect_product_info(filename)
        

        

filename = 'product_sample38.csv'
obj = Scraper_Implementor()
obj.implementor('https://www.kickscrew.com/', filename)