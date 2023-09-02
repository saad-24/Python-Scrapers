import tkinter as tk
from tkinter import filedialog
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
from csv import writer

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper App")

        self.file_button = tk.Button(root, text="Choose File", command=self.choose_file)
        self.file_button.pack()

        self.search_option = tk.StringVar(root)
        self.search_option.set("firstname_lastname")
        self.search_option_label = tk.Label(root, text="Search in:")
        self.search_option_label.pack()

        self.search_option_menu = tk.OptionMenu(root, self.search_option, "firstname", "lastname", "full_name")
        self.search_option_menu.pack()

        # self.scrap_option = tk.StringVar(root)
        # self.scrap_option.set("all")
        # self.scrap_option_label = tk.Label(root, text="Scrap records with:")
        # self.scrap_option_label.pack()

        # self.scrap_option_menu = tk.OptionMenu(root, self.scrap_option, "all", "number")
        # self.scrap_option_menu.pack()

        self.search_button = tk.Button(root, text="Search and Scrape", command=self.search_and_scrape)
        self.search_button.pack()

    def choose_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    def search_and_scrape(self):
        # keyword = self.keyword_entry.get()
        search_option = self.search_option.get()
        print(search_option)
        print(type(search_option))
        # scrap_option = self.scrap_option.get()

        # with open(self.filepath, "r") as file:
        #     urls = file.readlines()

        search_list = []
        with open(self.filepath, "r") as file:
            for line in file:
                search_list.append(line.strip())

        with open('output.csv', "w", encoding="utf8", newline="") as csvfile:
            csv = writer(csvfile)
            columns = ['Title', 'Age', 'Vehicle', 'Address', 'Phone Number']
            csv.writerow(columns)

        for search_keyword in search_list:
            print(search_keyword)
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get('https://www.hitta.se/')

            time.sleep(10)
            try:
                driver.find_element(By.XPATH, '//button[@id="modalConfirmBtn"]').click()
            except:
                pass
            time.sleep(2)
            v=driver.find_element(By.XPATH, '//input[@id="sokHittaInput"]')
            v.send_keys(search_keyword)
            for i in range(5):
                try:
                    v.send_keys(Keys.ENTER)
                    break
                except:
                    pass
            # time.sleep(2)
            # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ENTER)

            time.sleep(5)
            try:
                driver.find_element(By.XPATH, '//button[@id="modalConfirmBtn"]').click()
            except:
                pass
            driver.find_element(By.XPATH, '//a[@data-test="search-result-tabs"][2]').click()
            time.sleep(5)

            a = driver.find_elements(By.XPATH, '//li[@data-trackcat="search-result-row"]')

            # div_to_find = '//button[@data-test="phone-link"]'

            # filtered_element = []

            for i in a:
                name = i.find_elements(By.XPATH, '//h2[@data-test="search-result-title"]/a')

            new_filtered_elements = []
            # for i in filtered_element:
            #     name = i.find_elements(By.XPATH, '//h2[@data-test="search-result-title"]/a')

            for i in name:    
                all = i.text
                print(all)
                name_parts = all.split()
                first_name = name_parts[0]
                last_name = ' '.join(name_parts[1:])

            # Example code:
                if search_option == "firstname":
                    if search_keyword == first_name:  # Assuming search_keyword is your keyword
                        new_filtered_elements.append(i.get_attribute('href'))
                        print(first_name)
                elif search_option == "lastname":
                    if search_keyword == last_name:
                        new_filtered_elements.append(i.get_attribute('href'))
                elif search_option == "fullname":
                    if search_keyword == all:
                        new_filtered_elements.append(i.get_attribute('href'))

            print(new_filtered_elements)
            for i in new_filtered_elements:
                print(i)
                driver.get(i)
                time.sleep(10)

                try:
                    a = driver.find_element(By.XPATH, '//div[@data-trackcat="phone-numbers"]')
                except:
                    continue
                if a:
                    title_lst = []
                    title_lst.append(driver.find_element(By.XPATH, '//h1[@data-test="h1-title"]').text)

                    age_lst = []
                    try:
                        age = driver.find_element(By.XPATH, '//div[@class="style_textContainer__97faA"]//p')
                        match = re.search(r'\d+', age.text)

                        if match:
                            numeric_value = int(match.group())
                            age_lst.append(numeric_value)
                        else:
                            age_lst.append("Not Found")
                    except:
                        age_lst.append("Not Found")

                    address_lst = []

                    try:
                        address = driver.find_element(By.XPATH, '//span[@data-test="full-address"]')
                        address_lst.append(address.text)
                    except:
                        address_lst.append("Not Found")

                    registered_vehicles = []
                    try:
                        vehicle = driver.find_element(By.XPATH, '//div[@data-test="vehicle-content"]')
                        try:
                            vehicle.find_element(By.XPATH, '//p[@data-test="no-vehicle-content"]')
                            registered_vehicles.append("Not Found")
                            print('it is here')
                        except:
                            vehicle.find_element(By.XPATH,'//p[@data-test="registered-vehicles"]')
                            print('Yeahhh here')
                            register_vehicle = driver.find_element(By.XPATH,'//p[@data-test="registered-vehicles"]')
                            print(register_vehicle.text, 'yeah')
                            match = re.search(r'(\d+)\s+fordon', register_vehicle.text)

                            if match:
                                owned_count = int(match.group(1))
                                registered_vehicles.append(owned_count)
                            else:
                                registered_vehicles.append('Not Found')
                                print('no actually here')
                    except:
                        registered_vehicles.append('Not Found')

                    number_lst = []
                    try:
                        number_button = driver.find_element(By.XPATH, '//div[@data-trackcat="phone-numbers"]')
                        number_button.click()
                        try:
                            number = driver.find_element(By.XPATH, '//button[@data-test="show-number"]')
                            number_lst.append(number.text)
                        except:
                            number_lst.append("Not Found")
                    except:
                        pass

                    print(title_lst, age_lst, registered_vehicles, address_lst, number_lst)
                    # data = []
                    # data.extend([title_lst, age_lst, registered_vehicles, address_lst])
                    with open('output.csv', "a", encoding="utf8", newline="") as csvfile:
                        for i,j,k,l,m in zip(title_lst, age_lst, registered_vehicles, address_lst, number_lst):
                            csv = writer(csvfile)
                            data = [i,j,k,l,m]
                            csv.writerow(data)

                # except Exception as e:
                #     print(f"An exception occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()
