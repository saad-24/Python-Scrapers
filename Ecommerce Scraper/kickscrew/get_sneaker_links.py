import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get('https://www.kickscrew.com/collections/air-jordan?page=7&product_type=Jackets')

global next_btn
wait = WebDriverWait(driver, 5)

product_link_lst = []
print('yes')
category_name = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@class="ais-Menu-item ais-Menu-item--selected"]/div/a/span[1]')))
b = category_name.text
try:
    next_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@aria-label="Next"]')))
except:
    products = driver.find_elements(By.XPATH, '//li[@class="ais-Hits-item"]/article/a')
    for product in products:
        try:
            oosbadge = driver.find_element(By.XPATH, "//span[contains(text(),'Out of Stock')]")
        except:
            product_link_lst.append(product.get_attribute('href'))
            print(product.get_attribute('href'))

while next_btn:
    products = driver.find_elements(By.XPATH, '//li[@class="ais-Hits-item"]/article/a')
    for product in products:
        try:
            oosbadge = driver.find_element(By.XPATH, "//span[contains(text(),'Out of Stock')]")
        except:
            product_link_lst.append(product.get_attribute('href'))
            print(product.get_attribute('href'))

    try:
        next_link = driver.find_element(By.XPATH, '//a[@aria-label="Next"]')
        a = next_link.get_attribute('href')
    except:
        break

    driver.get(a)

print(product_link_lst)