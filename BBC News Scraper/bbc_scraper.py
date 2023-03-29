from csv import writer
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


class Initializer:
    def __init__(self,url):
        self.title_lst = []
        self.description_lst = []
        self.url_lst = []
        self.url = url

class Browser:
    def session(self):
        self.driver = webdriver.Chrome()

class Scraper(Browser, Initializer):
    def news_scraper(self):
        articles = self.driver.find_elements(By.CLASS_NAME, 'gs-c-promo-body')
        for article in articles:
            url = article.find_element(By.TAG_NAME, 'a')
            self.url_lst.append(url.get_attribute('href'))


        self.new_url_lst = []
        for i in self.url_lst:
            if i not in self.new_url_lst:
                if re.search("news",i, re.IGNORECASE):
                    self.new_url_lst.append(i)


    def get_description(self):
        self.link_lst = []
        for i in self.new_url_lst:
            if i.startswith('https'):
                self.link_lst.append(i)
            else:
                format_link = "https://www.bbc.com{}".format(i)
                self.link_lst.append(format_link)

        for i in self.link_lst:
            print(i)
            self.driver.get(i)
            time.sleep(10)
            try:
                ad_btn = self.driver.find_element(By.XPATH, '//button[@id="close1"]')
                ad_btn.click()
                time.sleep(5)
            except:
                pass

            flag = False

            try:
                title = self.driver.find_element(By.XPATH, '//h1[@id="main-heading"]')
                self.title_lst.append(title.text)
            except:
                self.title_lst.append("No title found!")

            time.sleep(2)
            try:
                description = self.driver.find_elements(By.XPATH, '//div[@data-component="text-block"]')
                flag = True
            except:
                description = self.driver.find_elements(By.XPATH, '//article//p')
                flag = True

            if flag == False:
                description = self.driver.find_elements(By.XPATH, '//p[@class="ssrcss-1q0x1qg-Paragraph eq5iqo00"]')
            else:
                pass

            desc_lst = []
            for i in description:
                desc_lst.append(i.text)
            self.description_lst.append(desc_lst)
        print(self.description_lst)

class CSV(Scraper):
    def make_csv(self, filename):
        with open(filename, "a", newline="", encoding="utf8") as f:
            csv = writer(f)
            columns = ['Title', 'URL', 'Description']
            csv.writerow(columns)

    def populate_csv(self,filename):
        with open(filename, "a", newline="", encoding="utf8") as f:
            csv = writer(f)
            for i in range(len(self.link_lst)):
                data = [self.title_lst[i], self.link_lst[i], self.description_lst[i]]
                csv.writerow(data)


class Scraper_Implementor(CSV):
    def get_news(self):
        super().session()
        self.driver.get(self.url)
        time.sleep(5)
        super().news_scraper()
        super().get_description()


url = 'https://www.bbc.com/news'
obj = Scraper_Implementor(url)
obj.get_news()
obj.make_csv('news.csv')
obj.populate_csv('news.csv')
