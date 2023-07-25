from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from csv import writer
import pandas as pd
from selenium.webdriver.common.keys import Keys


class Initializer:
    def __init__(self):
        self.keywords_lst = []

# A browser class which initializes browser
class Browser:
    def session(self):
        self.driver = webdriver.Chrome()

# CSV class which performs all operations
# related to CSV. (read the keywords csv,
# make the output csv and populate each playlist
# detail in the CSV.
class CSV(Initializer):
    def read_csv(self, filename):
        df = pd.read_csv(filename)
        for i in df['Keywords']:
            self.keywords_lst.append(i)

    def make_csv(self, filename):
        with open(filename, "a", encoding="utf8", newline="") as f:
            write_csv = writer(f)
            columns = ['Keyword','Playlist Title', 'No.of Videos', 'Playlist Link']
            write_csv.writerow(columns)

    def populate_csv(self,filename, data):
        with open(filename, "a", encoding="utf8", newline="") as f:
            write_csv = writer(f)
            write_csv.writerow(data)


# a scraper class which performs search
# and scrapes the playlist details
class Scraper(Browser, CSV):
    def search(self, keyword):
        search_field = self.driver.find_element(By.XPATH, "//input[@id='search']")
        search_field.click()
        time.sleep(2)
        search_field.send_keys(keyword)
        self.driver.find_element(By.XPATH, '//button[@class="style-scope ytd-searchbox"]').click()
        time.sleep(10)
        try:
            filters = self.driver.find_element(By.XPATH, '//ytd-toggle-button-renderer[@class="style-scope ytd-search-sub-menu-renderer"]')
            filters.click()
        except:
            filters = self.driver.find_element(By.XPATH, '//button[@aria-label="Search filters"]')
            filters.click()
        time.sleep(2)
        set_filter = self.driver.find_element(By.XPATH, '//div[@title="Search for Playlist"]')
        self.driver.execute_script("arguments[0].click()",set_filter)
        time.sleep(5)

    def playlist_scraper(self, filename, keyword):
        playlist_title = []
        playlist_link = []
        playlist_videos = []
        flag = False

        while not flag:
            body = self.driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)  # wait for the page to load new content
            playlist_title = self.driver.find_elements(By.XPATH, '//span[@id="video-title"]')
            playlist_link = self.driver.find_elements(By.XPATH, '//a[@class="yt-simple-endpoint style-scope ytd-playlist-thumbnail"]')
            playlist_videos = self.driver.find_elements(By.XPATH, '//yt-formatted-string[@class="style-scope ytd-thumbnail-overlay-bottom-panel-renderer"]')
            # check if there are no more results
            no_more_results = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'No more results')]")
            if len(no_more_results) > 0:
                flag = True

        title_lst = []
        for title in playlist_title:
            title_lst.append(title.text)

        playlist_link_lst = []
        for link in playlist_link:
            playlist_link_lst.append(link.get_attribute('href'))

        playlist_videos_lst = []
        for videos in playlist_videos:
            playlist_videos_lst.append(videos.text)

        self.new_title = []
        self.new_playlist_link = []
        self.new_playlist_videos = []

        for i in title_lst:
            if i != "":
                self.new_title.append(i)

        for j in playlist_link_lst:
            if j != "":
                self.new_playlist_link.append(j)

        for k in playlist_videos_lst:
            if k != "":
                self.new_playlist_videos.append(k)


        for i,j,k in zip(self.new_title, self.new_playlist_videos, self.new_playlist_link):
            data = [keyword,i,j,k]
            super().populate_csv(filename, data)

        print(title_lst)
        print(playlist_link_lst)
        print(playlist_videos_lst)



# An implementor class which calls all
# the fucntions from above class and implements
# Scraper
class Scraper_Implementor(Scraper):
    def get_playlist(self,read_filename,write_filename, url):
        super().read_csv(read_filename)
        print(self.keywords_lst)
        super().make_csv(write_filename)
        for i in self.keywords_lst:
            super().session()
            time.sleep(2)
            self.driver.get(url)
            time.sleep(5)
            super().search(keyword=i)
            super().playlist_scraper(write_filename, keyword=i)
            # super().populate_csv(write_filename)



# Driver Code
obj = Scraper_Implementor()
obj.get_playlist('keywords.csv','test_v3.csv', 'https://www.youtube.com/')
