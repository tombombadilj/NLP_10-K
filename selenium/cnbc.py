from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import pickle

driver = webdriver.Chrome()

with open('ticker_list', 'rb') as handle:
    b = pickle.load(handle)

URL = "http://www.cnbc.com/quotes/?symbol={s}&tab=news"
c = b[0:5]

csv_file = open('news.csv', 'wb')
writer = csv.writer(csv_file)
writer.writerow(['company', 'headline', 'url', 'time'])

for each in c:
    link = URL.format(s=each)
    driver.get(link)
    listings = driver.find_elements_by_xpath('.//div[@class="headline"]')
    print len(listings)
    for listing in listings:
        list_dict = {}
        company = each
        print company
        headline = listing.find_element_by_xpath('.//span[@ng-bind="asset.headline"]').text
        print headline
        headline_url = listing.find_element_by_xpath('.//a')
        url = headline_url.get_attribute("href")
        print url
        time = listing.find_element_by_xpath('.//span[@class="note ng-binding"]').text
        print time
        list_dict["company"] = company
        list_dict["url"] = headline
        list_dict["ticker"] = url
        list_dict["time"] = time
        writer.writerow(list_dict.values())

driver.close()
csv_file.close()