# This script is for scraping products from amazon, where products are each product is enclosed in "a-section" class and anchor tag of product have "a-link-normal" class. Please check accordingly for scraping.
# This script only extracts URL of amazon.com and save them to a file
# You need to pass the 1st page URL of product search.

from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\Users\\akkha\\Documents\\chromedriver.exe')
driver.set_window_size(200, 300)
baseUrl = "https://www.amazon.com"

def get_product_links(url):
    all_urls = []
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, features='html.parser')
    dom = etree.HTML(str(soup))
    next_btn = driver.find_elements(by=By.CLASS_NAME, value="a-last")
    product_tag_class = "a-link-normal"
    individual_product_section = "a-section a-spacing-medium"
    el = soup.find_all("div", {"class":individual_product_section})
    for a in el:
        product_a = a.find('a', {"class":product_tag_class})
        product_href = str(product_a["href"])
        full_href = baseUrl + product_href
        if full_href not in all_urls:
            all_urls.append(full_href)

    file = open(file='penProducts.csv', mode='a+', encoding='utf-8')
    for x in all_urls:
        file.write(x+"\n")
    file.close()

    if next_btn:
        next_btn[0].click()
        get_product_links(driver.current_url)    
    driver.close()


get_product_links("https://www.amazon.com/s?k=pen&i=office-products&refresh=1&ref=glow_cls&page=292")