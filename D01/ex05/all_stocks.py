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

    words = str(sys.argv[1])

    l = [i.strip() for i in words.split(",")]

    if sum([i.isalpha() for i in l]) == len(l):
        for i in l:
            if i.capitalize() in COMPANIES.keys():
                print(
                    f"{i.capitalize()} stock price is {STOCKS[COMPANIES[i.capitalize()]]}"
                )
            elif i.upper() in STOCKS.keys():
                COMPANIES_invert = {}
                for keys, values in COMPANIES.items():
                    COMPANIES_invert[values] = keys
                print(
                    f"{i.upper()} is a ticker symbol for {COMPANIES_invert[i.upper()]}"
                )
            else:
                print(f"{i} is an unknown company or an unknown ticker symbol")

    else:
        sys.exit()


if __name__ == "__main__":
    main()
