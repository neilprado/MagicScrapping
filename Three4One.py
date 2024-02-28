from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        search_input = driver.find_element("css selector", ".search-bar__input")
        search_input.clear()
        search_input.send_keys(search)

        search_input.send_keys(Keys.RETURN)

        time.sleep(5)

        product_items = driver.find_elements("css selector", ".product-item")

        for item in product_items:
            items.append(item.find_element("css selector", ".product-item__title").text)
            prices.append(item.find_element("css selector", ".price").text)
    print(items)

    finishing(driver)


def finishing(driver):
    driver.quit()
