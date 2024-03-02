import LigaMagic
import Three4One
import products
import utils


def main():
     three_sealed, three_prices = Three4One.scrapping(products.translate_product(products.sealed_products, "en"))
     liga_sealed, liga_prices = LigaMagic.liga_sealed_scrapping(products.translate_product(three_sealed, "pt"))

     utils.createExcelFile(three_sealed, three_prices, liga_sealed, liga_prices, 5.37)

main()