import Three4One
import data


def main():
    sealed_products = data.sealed_products_three_4_one()
    sealed, prices = Three4One.scrapping(sealed_products)
    Three4One.createExcelFile(sealed, prices)

main()