import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def config():
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get("https://shop.threeforonetrading.com")

    return driver


def scrapping(searches):
    driver = config()

    items = []
    prices = []

    for search in searches:
        search_input = driver.find_element(By.CSS_SELECTOR, ".search-bar__input")
        search_input.clear()
        search_input.send_keys(search)

        search_input.send_keys(Keys.RETURN)

        time.sleep(7)

        product_items = driver.find_elements(By.CSS_SELECTOR, ".product-item")

        for item in product_items:
            title = item.find_element(By.CSS_SELECTOR, ".product-item__title").text
            if search == title:
                items.append(search)
                prices.append(extract_euro_price(item.find_element(By.CSS_SELECTOR, ".price").text))
                break

    finishing(driver)
    return items, prices


def finishing(driver):
    driver.quit()


def extract_euro_price(price):
    pattern = re.compile(r'€\s*(\d+(?:\.\d+)?)')
    matching = pattern.search(price)

    if matching:
        euro_price = matching.group(1)
        return float(euro_price)
    else:
        return None

