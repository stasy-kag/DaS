import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def find_row_values(soup, name):
    rows = soup.find_all('div', class_='row')

    for row in rows:
        title_div = row.find('div', class_='rowTitle')
        if title_div and title_div.text.strip() == name:
            cols = row.find_all('div', class_='column') + row.find_all('div', class_='column alt')
            values = [col.text.strip() for col in cols if col.text.strip()]
            return (name, *values)
    raise Exception(f"Field '{name}' not found")


def main():
    if len(sys.argv) != 3:
        sys.exit()

    url = f'https://finance.yahoo.com/quote/{sys.argv[1].upper()}/financials/?p={sys.argv[1].lower()}'

    options = Options()

    options.page_load_strategy = 'eager'

    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(5)
    except TimeoutException:
        print("Warning: Page load timed out but continuing...")

    soup = BeautifulSoup(driver.page_source, "html.parser")
    div = soup.find('div', class_='tableContainer')
    if not div:
        raise Exception(f"Table container not found on '{url}'")
    result = find_row_values(div, sys.argv[2])
    return result


if __name__ == "__main__":
    try:
        print(main())
    except Exception as e:
        print(e)