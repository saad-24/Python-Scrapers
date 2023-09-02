from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from csv import writer
import os
import pandas as pd


class ListInitializer:
    def __init__(self):
        self.property_link_lst = []
        self.area_list = ['https://www.graana.com/{}karachi-169/']


class Browser:
    #initializing browser session
    def session(self):
        self.driver = webdriver.Chrome()

class CSV:
    def make_csv(self, filename):
        if os.path.exists(filename):
            print("File exists")
            return
        else:
            print("File does not exist")
            with open(filename, "w", encoding="utf8" ,newline="") as csvfile:
            # Create a CSV writer object
                csv = writer(csvfile)
                csv.writerow(['Link','Source', 'Property ID', 'Title', 'Type', 'Purpose', 'Area', 'Address', 'Location', 'Number', 'Price', 'Bed', 'Bath', 'Amenties', 'Description', 'Images'])

    def populate_csv(self, filename, data):
        with open(filename, "a", encoding="utf8", newline="") as csvfile:
            csv = writer(csvfile)
            csv.writerow(data)


class Scraper(Browser, ListInitializer, CSV):
    #this function collect links on each page
    def collect_links(self):
        global total_pages
        try:
            self.driver.find_element(By.XPATH, '//div[@class="MuiBox-root mui-style-1osduea"]')
            pass
        except:
            print('No property found')
            return

        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0,3100)")

        try:
            next_btn = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
            pass
        except:
            all_property = self.driver.find_elements(By.XPATH, '//div[@class="MuiBox-root mui-style-79elbk"]//a')
            for k in all_property:
                property_links = k.get_attribute('href')
                self.property_link_lst.append(property_links)
            return

        while next_btn.is_enabled():
            self.driver.execute_script("window.scrollTo(0,500)")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,900)")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,1200)")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,2000)")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,2300)")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,3000)")
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,3100)")
            time.sleep(5)
            all_property = self.driver.find_elements(By.XPATH, '//div[@class="MuiBox-root mui-style-79elbk"]//a')
            for k in all_property:
                property_links = k.get_attribute('href')
                self.property_link_lst.append(property_links)
            try:
                next_btn.click()
                time.sleep(20)
                next_btn = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
            except:
                break


    #this fucntion visits each link, gets the information and save in csv
    def get_property_info(self, filename):
            
        link_lst = []
        link_lst.append(self.driver.current_url)

        purpose_lst = []
        if "rent" in self.driver.current_url:
            purpose_lst.append("Rent")
        elif "sale" in self.driver.current_url:
            purpose_lst.append("Sale")
        time.sleep(20)

        source_lst = []
        source_lst.append('Graana.com')

        # number
        number_lst = []
        try:
            self.driver.find_element(By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium mui-style-xyl7ut"]').click()
            time.sleep(5)
            number = self.driver.find_element(By.XPATH, '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedSecondary MuiButton-sizeMedium MuiButton-containedSizeMedium mui-style-t3j9vb"]')
            number_lst.append(number.text)
            self.driver.find_element(By.XPATH, '//div[@class="MuiBox-root mui-style-1c3dwoe"]').click()
        except:
            number_lst.append('Not found')
        time.sleep(1)

        #property id
        property_id_lst = []
        try:
            property_id = self.driver.find_element(By.XPATH, '//h4[@class="MuiTypography-root MuiTypography-h4 mui-style-1w6o2c9"]')
            index = property_id.text.find("#")
            if index != -1:
                new_string = property_id.text[index + 1:]
                property_id_lst.append(new_string)
        except:
            property_id_lst.append("Not Found")

        #bed,bath,area
        bed_lst = []
        bath_lst = []
        area_lst = []
        try:
            lst = self.driver.find_elements(By.XPATH, '//div[@class="MuiTypography-root MuiTypography-subtitle2New mui-style-1b47bkd"]')
            bed_lst.append(lst[0].text)
            bath_lst.append(lst[1].text)
            area_lst.append(lst[2].text)
        except:
            bed_lst.append("Not Found")
            bath_lst.append("Not Found")
            area_lst.append("Not Found")

        #images
        main_img_lst = []
        try:
            self.driver.find_element(By.XPATH, '//div[@class="MuiBox-root mui-style-16biat6"]').click()
            img = self.driver.find_elements(By.XPATH, '//li[@class="slide"]//img')
            img_lst = []
            for image in img:
                images = image.get_attribute('src')
                img_lst.append(images)
            main_img_lst.append(img_lst)
            self.driver.find_element(By.XPATH, '//div[@class="MuiBox-root mui-style-l8uiwr"]').click()

        except:
            main_img_lst.append('Not Found')
        time.sleep(1)

        #title
        title_lst = []
        address_lst = []
        location = []
        try:
            title = self.driver.find_element(By.XPATH, '//h3[@class="MuiTypography-root MuiTypography-h3New mui-style-s6x0cd"]')
            title_lst.append(title.text)
            index = title.text.find("In")
            if index != -1:
                new_string = title.text[index + 2:]
                address_lst.append(new_string)
                location.append(new_string)
        except:
            title_lst.append("Not Found")
            address_lst.append("Not Found")
            location.append("Not Found")
        # time.sleep(1)

        #type
        type_lst = []
        try:
            type = self.driver.find_element(By.XPATH, '//div[@class="MuiTypography-root MuiTypography-subtitle2New mui-style-1d3e9wz"]')
            type_lst.append(type.text)
        except:
            type_lst.append("Not Found")


        #price
        price_lst = []
        try:
            price = self.driver.find_element(By.XPATH, '//span[@class="MuiTypography-root MuiTypography-h2New mui-style-1k6ms13"]')
            price_lst.append(price.text)
        except:
            price_lst.append('Not Found')
        # time.sleep(1)

        #description
        description_lst = []
        try:
            description = self.driver.find_element(By.XPATH,
                                                    '//div[@class="MuiTypography-root MuiTypography-subtitle2New mui-style-13sqdw6"]')
            read = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Read more')]")

            if description:
                if read:
                    read.click()
                    description_lst.append(description.text)
                else:
                    description_lst.append(description.text)
        except:
            description_lst.append("Not Found")
        time.sleep(1)

        #amenties
        amenties_lst = []
        try:
            amenties = self.driver.find_element(By.XPATH, '//div[@class="MuiBox-root mui-style-s98bge"]')
            amenties_lst.append(amenties.text)
        except:
            amenties_lst.append('Not found')
        time.sleep(1)

        data = []
        data.extend([link_lst, source_lst, property_id_lst, title_lst, type_lst, purpose_lst, area_lst, address_lst, location, number_lst, price_lst, bed_lst, bath_lst, amenties_lst, description_lst, main_img_lst])
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

#implementor class
class Scraper_Implementor(Scraper):
    def rent_residential(self):
        super().session()
        for i in self.area_list:
            url = i.format('rent/residential-properties-rent-')
            self.driver.get(url)
            super().collect_links()

    def rent_commercial(self):
        super().session()
        for i in self.area_list:
            url = i.format('rent/commercial-properties-rent-')
            self.driver.get(url)
            super().collect_links()


    def rent_plot(self):
        super().session()
        for i in self.area_list:
            url = i.format('rent/plot-properties-rent-')
            self.driver.get(url)
            super().collect_links()

    def sale_residential(self):
        super().session()
        for i in self.area_list:
            url = i.format('sale/residential-properties-sale-')
            self.driver.get(url)
            super().collect_links()

    def sale_commercial(self):
        super().session()
        for i in self.area_list:
            url = i.format('sale/commercial-properties-sale-')
            self.driver.get(url)
            super().collect_links()


    def sale_plot(self):
        super().session()
        for i in self.area_list:
            url = i.format('sale/plot-properties-sale-')
            self.driver.get(url)
            super().collect_links()




# driver code
obj = Scraper()
scraper_obj = Scraper_Implementor()
scraper_obj.rent_residential()
scraper_obj.rent_commercial()
scraper_obj.rent_plot()
scraper_obj.sale_residential()
scraper_obj.sale_commercial()
scraper_obj.sale_plot()
scraper_obj.make_csv('property_scraper_v3.csv')
scraper_obj.property_info_implementor('property_scraper_v3.csv')
