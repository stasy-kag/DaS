import sys
import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/137.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}


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
    r = requests.get(url, headers=headers, timeout=10)
    time.sleep(5)
    if r.status_code != 200:
        raise Exception(f"HTTP error {r.status_code}")

    soup = BeautifulSoup(r.text, "html.parser")
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