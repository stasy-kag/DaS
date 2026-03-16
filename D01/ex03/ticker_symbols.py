import sys


def main():
    COMPANIES = {
        "Apple": "AAPL",
        "Microsoft": "MSFT",
        "Netflix": "NFLX",
        "Tesla": "TSLA",
        "Nokia": "NOK",
    }
    STOCKS = {
        "AAPL": 287.73,
        "MSFT": 173.79,
        "NFLX": 416.90,
        "TSLA": 724.88,
        "NOK": 3.37,
    }

    if len(sys.argv) != 2:
        sys.exit()

    ticker = sys.argv[1].upper()

    company = None
    for key, value in COMPANIES.items():
        if value == ticker:
            company = key
            break

    if company and ticker in STOCKS:
        print(company, STOCKS[ticker])
    else:
        print("Unknown company.")


if __name__ == "__main__":
    main()
