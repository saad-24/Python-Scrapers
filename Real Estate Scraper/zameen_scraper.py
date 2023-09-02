from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from csv import writer
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pandas as pd



class ListInitializer:
    def __init__(self):
        self.property_link_lst = []
        self.area_list = ['https://www.zameen.com/{}/Karachi-2-1.html']

class Browser:
    def session(self):
        self.driver = webdriver.Chrome()

class CSV:
    def make_csv(self, filename):
        if os.path.exists(filename):
            print("File exists")
            return
        else:
            print("File does not exist")
            with open(filename, "w", encoding="utf8", newline="") as csvfile:
                csv = writer(csvfile)
                columns = ['Link','Source', 'Property_id', 'Title', 'Type', 'Purpose', 'Area', 'Address', 'Location', 'Number', 'Price', 'Beds', 'Baths', 'Amenties', 'Description', 'Images']
                csv.writerow(columns)

    def populate_csv(self, filename, data):
        with open(filename, "a", encoding="utf8", newline="") as csvfile:
            csv = writer(csvfile)
            csv.writerow(data)

class Scraper(Browser, ListInitializer, CSV):
    def collect_links(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            self.driver.switch_to.frame('google_ads_iframe_/31946216/Splash_660x500_0')
            self.driver.find_element(By.XPATH, '/html/body/div[2]/img').click()
            self.driver.switch_to.default_content()
        except:
            pass

        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, '//*[@id="body-wrapper"]/div[2]/div/div/div[2]/button[2]').click()
            self.driver.switch_to.frame('google_ads_iframe_/31946216/HStrip_NS_0')
            self.driver.find_element(By.CLASS_NAME, 'hotstrip_cross').click()
            self.driver.switch_to.default_content()
        except:
            pass
        try:
            self.next_page = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@title='Next']")))
            # self.driver.find_element(By.XPATH, "//a[@title='Next']")
        except:
            articles = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='_7ac32433']")))
            # articles = self.driver.find_elements(By.XPATH, "//a[@class='_7ac32433']")
            for article in articles:
                all_articles = article.get_attribute('href')
                self.property_link_lst.append(all_articles)
                print(article.get_attribute('href'))

        while self.next_page:
            articles = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='_7ac32433']")))
            for article in articles:
                all_articles = article.get_attribute('href')
                self.property_link_lst.append(all_articles)
                print(article.get_attribute('href'))
            
            try:
                self.next_page.click()
                time.sleep(10)
                self.next_page = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@title='Next']")))

            except:
                break


    def get_property_info(self, filename):
        link_lst = []
        link_lst.append(self.driver.current_url)

        source_lst = []
        source_lst.append('Zameen.com')

        #images
        main_img_lst = []
        try:
            loop_range = self.driver.find_element(By.XPATH, '//div[@aria-label="View gallery"]')
            a = loop_range.text

            open_images = self.driver.find_element(By.XPATH, '//div[@class="_2c38e06c _750a3d83"]')
            open_images.click()
            time.sleep(5)

            for i in range(int(a) - 1):
                self.driver.find_element(By.XPATH, '//div[@class="_2c38e06c _54481376"]').click()
                time.sleep(1)

            image_lst = []
            image = self.driver.find_elements(By.XPATH, '//img[@class="_90d35881"]')
            for j in image:
                all_images = j.get_attribute('src')
                image_lst.append(all_images)
            main_img_lst.append(image_lst)
            close_btn = self.driver.find_element(By.XPATH, '//button[@class="eae3ed68 c1c2e5c8"]')
            close_btn.click()
        except:
            main_img_lst.append("Not Found")

        #title
        title_lst = []
        try:
            title = self.driver.find_element(By.XPATH, "//h1[@class='_64bb5b3b']")
            title_lst.append(title.text)
        except:
            title_lst.append("Not Found")
        time.sleep(2)

        #price
        price_lst = []
        try:
            price = self.driver.find_elements(By.XPATH, '//span[@class="_8eee1bdd"]')
            property_price = price[1]
            price_lst.append(property_price.text)
        except:
            price_lst.append("Not Found")
        time.sleep(2)

        #address
        address_lst = []
        try:
            address = self.driver.find_element(By.XPATH, '//div[@aria-label="Property header"]')
            address_lst.append(address.text)
        except:
            address_lst.append("Not Found")

        time.sleep(2)

        #location
        location_lst = []
        try:
            location = self.driver.find_element(By.XPATH, '//span[@aria-label="Location"]')
            location_lst.append(location.text)
        except:
            location_lst.append("Not Found")
        time.sleep(2)

        #beds
        beds_lst = []
        try:
            beds = self.driver.find_element(By.XPATH, '//span[@aria-label="Beds"]')
            index = beds.text.find("Beds")
            if index != -1:
                new_string = beds.text[:index]
                beds_lst.append(new_string)
        except:
            beds_lst.append("Not Found")
        time.sleep(2)

        # baths
        baths_lst = []
        try:
            baths = self.driver.find_element(By.XPATH, '//span[@aria-label="Baths"]')
            index = baths.text.find("Baths")
            if index != -1:
                new_string = baths.text[:index]
                baths_lst.append(new_string)

        except:
            baths_lst.append("Not Found")
        time.sleep(2)

        #area
        area_lst = []
        try:
            area = self.driver.find_element(By.XPATH, '//span[@aria-label="Area"]')
            area_lst.append(area.text)
        except:
            area_lst.append("Not Found")
        time.sleep(2)

        #type
        type_lst = []
        try:
            type = self.driver.find_element(By.XPATH, '//span[@aria-label="Type"]')
            type_lst.append(type.text)
        except:
            type_lst.append("Not Found")
        time.sleep(2)

        #purpose
        purpose_lst = []
        try:
            purpose = self.driver.find_element(By.XPATH, '//span[@aria-label="Purpose"]')
            if purpose.text == "For Rent":
                index = purpose.text.find("Rent")
                if index != -1:
                    new_string = purpose.text[index:]
                    purpose_lst.append(new_string)
                    print(new_string)
            elif purpose.text == "For Sale":
                index = purpose.text.find("Sale")
                if index != -1:
                    new_string = purpose.text[index:]
                    purpose_lst.append(new_string)
                    print(new_string)

        except:
            purpose_lst.append("Not Found")

        #description
        description_lst = []
        try:
            description = self.driver.find_element(By.XPATH, '//span[@class="_2a806e1e"]')
            description_lst.append(description.text)
        except:
            description_lst.append("Not Found")
        time.sleep(2)

        #amenties
        amenties_lst = []
        try:
            amenties = self.driver.find_elements(By.XPATH, '//ul[@class="_6e283b70"]')
            for i in amenties:
                amenties_lst.append(i.text)
        except:
            amenties_lst.append("Not Found")
        time.sleep(2)

        #number
        number_lst = []
        property_id_lst = []
        try:
            self.driver.find_element(By.XPATH, "//button[@class='_5b77d672 da62f2ae _8a1d083b']").click()
            time.sleep(3)
            property_id = self.driver.find_element(By.XPATH, '//div[@class="a90d2509"]')
            property_id_lst.append(property_id.text)

            number = self.driver.find_element(By.XPATH, "//span[@dir='ltr']")
            number_lst.append(number.text)
        except:
            number_lst.append("Not Found")
            property_id_lst.append("Not Found")
        
        data = []
        data.extend([link_lst, source_lst, property_id_lst, title_lst, type_lst, purpose_lst, area_lst, address_lst, location_lst, number_lst, price_lst, beds_lst, baths_lst, amenties_lst, description_lst, main_img_lst])
        print(data)
        super().populate_csv(filename, data)

    def property_info_implementor(self, filename):
        df = pd.read_csv(filename)
        property_urls=df['link'].tolist()
        super().session()
        for link in self.property_link_lst:
            if link not in property_urls:
                self.driver.get(link)
                time.sleep(5)
                self.get_property_info(filename)
        


class Scraper_Implementor(Scraper):
    def rent_residential(self):
        super().session()
        for i in self.area_list:
            url = i.format('Rentals')
            self.driver.get(url)
            super().collect_links()

    def rent_commercial(self):
        super().session()
        for i in self.area_list:
            url = i.format('Rentals_Commercial')
            self.driver.get(url)
            super().collect_links()

    def rent_plot(self):
        super().session()
        for i in self.area_list:
            url = i.format('Rentals_Plots')
            self.driver.get(url)
            super().collect_links()

    def sale_residential(self):
        super().session()
        for i in self.area_list:
            url = i.format('Homes')
            self.driver.get(url)
            super().collect_links()

    def sale_commercial(self):
        super().session()
        for i in self.area_list:
            url = i.format('Commercial')
            self.driver.get(url)
            super().collect_links()

    def sale_plot(self):
        super().session()
        for i in self.area_list:
            url = i.format('Plots')
            self.driver.get(url)
            super().collect_links()


# driver code

obj = Scraper_Implementor()
# obj.rent_residential()
# obj.rent_commercial()
# obj.rent_plot()
# obj.sale_residential()
# obj.sale_commercial()
obj.sale_plot()
obj.make_csv('property_scraper_v11.csv')
obj.property_info_implementor('property_scraper_v11.csv')