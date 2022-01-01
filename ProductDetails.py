from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import etree
from selenium.webdriver.common.by import By
import datetime, re

driver = webdriver.Chrome('C:\\Users\\akkha\\Documents\\chromedriver.exe')
driver.set_window_size(200, 300)
baseUrl = "https://www.amazon.com"

def get_details(url_of_product):
    driver.get(url_of_product)
    soup = BeautifulSoup(driver.page_source, features='html.parser')
    dom = etree.HTML(str(soup))
    prime_free_del = False

    date = datetime.date.today()
    product_desc = driver.find_element(by=By.ID, value="productTitle").text

    try:
        variants = driver.find_element(by=By.CLASS_NAME, value="dimension-values-list")
        has_variant = True
    except:
        has_variant = False

    try:
        subSave = driver.find_element(by=By.ID, value="snsAccordionRowMiddle")
        subPrice = driver.find_element(by=By.ID, value="sns-tiered-price").text
        savePercent = driver.find_element(by=By.CLASS_NAME, value="discountText").text
        subNSave = True
    except:
        subNSave, subPrice, savePercent = False, '', ''

    try:
        choice = driver.find_element(by=By.ID, value="a-popover-amazons-choice-popover")
        is_a_choice = True
    except:
        is_a_choice = False

    try:
        renew = driver.find_element(by=By.ID, value="gsbbUsedPrice")
        renewed = True
    except:
        renewed = False

    try:
        freereturn = driver.find_element(by=By.ID, value="creturns-policy-anchor-text")
        hasFreeReturn = True
    except:
        hasFreeReturn = True
        
    try:
        seller_rank = driver.find_element(by=By.XPATH, value='//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[3]/td/span/span[1]/text()[1]')
        seller_rank = re.findall('\d+', '%s' % seller_rank)
        if seller_rank < 500:
            best_seller = True
        else:
            best_seller = False
    except:
        best_seller = False

    try:
        limited_deal = driver.find_element(by=By.XPATH, value='//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[1]').text
        limited_deal = True
    except:
        limited_deal = False

    try:
        ship_msg = driver.find_element(by=By.ID, value="price-shipping-message")
        if 'Get Fast, Free Shipping with' in ship_msg.text:
            free_ship = False
            prime_free_del = True
        else:
            free_ship = True
    except:
        free_ship = False

    try:
        ship_over = driver.find_element(by=By.XPATH, value='//*[@id="mir-layout-DELIVERY_BLOCK-slot-DELIVERY_MESSAGE"]/text()')
        if 'orders over' in ship_over:
            ship_over_high = True
        else:
            ship_over_high = False
    except:
        ship_over_high = False

    try:
        coupon_badge = driver.find_element(by=By.CLASS_NAME, value='couponBadge')
        coupon_badge = True
    except:
        coupon_badge = False

    price = driver.find_element(by=By.ID, value="priceblock_ourprice").text
    available = 0
    driver.close()

file = open('file.csv', mode="r", encoding='utf-8')
lines = file.readlines()

get_details(lines[0])

