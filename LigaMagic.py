import re
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def config():
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.get("https://www.ligamagic.com.br")

    return driver


def liga_sealed_scrapping(scrappings):
    driver = config()

    items = []
    prices = []

    for scrapping in scrappings:
        search = driver.find_element(By.ID, "mainsearch")
        search.clear()
        search.send_keys(scrapping)

        search.send_keys(Keys.RETURN)

        time.sleep(7)

        if driver.find_elements(By.CSS_SELECTOR, ".mtg-linhas"):
            lists = driver.find_elements(By.CSS_SELECTOR, ".box")
            for index in lists:
                title = formatting_name(index.find_element(By.CSS_SELECTOR, ".mtg-name-prod").text)
                if scrapping == title and title not in items:
                    items.append(formatting_name(index.find_element(By.CSS_SELECTOR, ".mtg-name-prod").text))
                    try:
                        index.find_element(By.CSS_SELECTOR, ".price-out-of-stock")
                        prices.append(formatting_price('0.0'))
                    except NoSuchElementException:
                        prices.append(formatting_price(index.find_element(By.CSS_SELECTOR, ".price-min").text))
                else:
                    continue
        else:
            items.append(driver.find_element(By.CSS_SELECTOR, ".nome-principal").text)
            prices.append(formatting_price(driver.find_element(By.CSS_SELECTOR, ".col-prc-menor").text))
    finishing(driver)
    return items, prices


def finishing(driver):
    driver.quit()


def formatting_price(price):
    string_price = re.sub(r'[^0-9,]', '', price).replace(',', '.')

    # Converter para float
    value = float(string_price)

    return value


def formatting_name(name):
    return str.strip(name)
