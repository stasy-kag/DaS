class Research:
    def file_reader(self):
        file = open("ds.csv", "r", encoding="utf-8")
        return file.read()


if __name__ == "__main__":
    obj = Research()
    print(obj.file_reader())
