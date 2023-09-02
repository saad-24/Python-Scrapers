import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import pandas as pd


class Intializer:
    def __init__(self):
        self.property_link_lst = []        

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
            with open(filename, 'w', encoding='utf8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(['Link','Source', 'Property ID', 'Title', 'Type', 'Purpose', 'Area', 'Address', 'Location', 'Number', 'Price', 'Bed', 'Bath', 'Amenties', 'Description', 'Images'])

    def populate_csv(self, filename, data):
        with open(filename, 'a', encoding='utf8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(data)
            
class Scraper(Intializer, Browser, CSV):
    def view_all_property(self):
        wait = WebDriverWait(self.driver, 10)
        time.sleep(5)
        purpose = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-2-input"]')))
        purpose.click()
        purpose.send_keys('All Purposes')
        time.sleep(1)
        purpose.send_keys(Keys.ENTER)
        time.sleep(2)
        city_label = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-3-input"]')))
        city_label.click()
        city_label.send_keys('Karachi')
        time.sleep(1)
        city_label.send_keys(Keys.ENTER)
        time.sleep(2)
        categories = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="react-select-5-input"]')))
        categories.click()
        categories.send_keys('All Categories')
        time.sleep(1)
        categories.send_keys(Keys.ENTER)
        time.sleep(2)
        search_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-search btn-primary d-flex align-items-center"]')))
        search_btn.click()
        time.sleep(10)

    def get_property(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            next_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="Go to next page"]')))
        except:
            properties = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="property-item-listing property-item"]/a')))
            for property in properties:
                self.property_link_lst.append(property.get_attribute('href'))

        while next_btn.is_enabled():
            properties = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="property-item-listing property-item"]/a')))
            for property in properties:
                self.property_link_lst.append(property.get_attribute('href'))
                print(property.get_attribute('href'))
            time.sleep(5)
            try:
                next_btn.click()
                time.sleep(10)
                next_btn = self.driver.find_element(By.XPATH, '//a[@aria-label="Go to next page"]')
            except:
                break

    
    def get_property_info(self, filename):
        wait = WebDriverWait(self.driver, 10)
        data = []
        link_lst = []
        link_lst.append(self.driver.current_url)
        time.sleep(5)


        link = self.driver.current_url
        data.append(link)

        data.append('Jagah Online')

        try:
            property_id =  wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@class="property-list list-unstyled"]/li[1]')))
            new_id = []
            for i in property_id.text:
                if i not in 'Property ID:':
                    new_id.append(i)
                    
            data.append(''.join(new_id))
        except:
            data.append("Not Found")

        try:
            title = wait.until(EC.presence_of_element_located((By.XPATH, '//section//h1')))
            if 'House' in title:
                data.append('House')
            elif 'Apartment' in title.text:
                data.append('Appartment')
            elif 'Flat' in title.text:
                data.append('Flat')
        except:
            data.append("Not Found")


        try:
            title = wait.until(EC.presence_of_element_located((By.XPATH, '//section//h1')))
            data.append(title.text)
        except:
            data.append("Not Found")


        try:
            title = wait.until(EC.presence_of_element_located((By.XPATH, '//section//h1')))
            if 'Rent' in title.text:
                data.append('Rent')
            elif 'Sale' in title.text:
                data.append('Sale')
        except:
            data.append("Not Found")

        try:
            area = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@class="property-list list-unstyled"]/li[2]')))
            data.append(area.text)
        except:
            data.append("Not Found")

        try:
            address = wait.until(EC.presence_of_element_located((By.XPATH, '//section//div[@class="row"]/div/span')))
            data.append(address.text)
        except:
            data.append("Not Found")

        try:
            location = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="property-address"]//div[@class="col-sm-6"][1]/ul/li[2]')))
            data.append(location.text)
        except:
            data.append("Not Found")

        data.append('Not Found')

        try:
            price = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="price font-xll text-primary"]')))
            data.append(price.text)
        except:
            data.append("Not Found")

        try:
            amenties = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="amenity-group d-flex"]/div')))
            for amenty in amenties:
                if 'Bed Room' in amenty.text:
                    bed_number = ''.join(filter(str.isdigit, amenty.text))
                elif 'Bath Room' in amenty.text:
                    bath_number = ''.join(filter(str.isdigit, amenty.text))

            data.append(bed_number)
            data.append(bath_number)
        except:
            data.append('Not Found')
            data.append('Not Found')

        amenties_lst = []
        try:
            amenties = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="amenity-group d-flex"]/div')))
            for amenty in amenties:
                amenties_lst.append(amenty.text)
            data.append(amenties_lst)
        except:
            data.append("Not Found")



        try:
            description = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="property-description"]/div//div[2]/div')))
            data.append(description.text)
        except:
            data.append("Not Found")

        

        image_lst = []
        try:
            image_tab = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="frontImg-ctas-counters"]/a[1]')))
            image_tab.click()
            images = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="detail-big-car-gallery"]/img[@class="img-fluid"]')))
            for image in images:
                image_lst.append(image.get_attribute('src'))
            data.append(image_lst)
        except:
            data.append("Not Found")

        
        print(data)
        super().populate_csv(filename, data)

    def property_info_implementor(self, filename):
        df = pd.read_csv(filename)
        property_urls=df['link'].tolist()
        for link in self.property_link_lst:
            if link not in property_urls:
                self.driver.get(link)
                time.sleep(5)
                self.get_property_info(filename)

                

class Scraper_Implementor(Scraper):
    def implementor(self, url, filename):
        super().session()
        self.driver.get(url)
        super().view_all_property()
        super().get_property()
        super().make_csv(filename)
        super().property_info_implementor(filename)



filename = 'jagah_online_property.csv'
obj = Scraper_Implementor()
obj.implementor('https://www.jagahonline.com/', filename)




