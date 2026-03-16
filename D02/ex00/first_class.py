class Must_Read:
    fail = open("ds.csv", "r", encoding="utf-8")
    print(fail.read())


if __name__ == "__main__":
    m = Must_Read()
