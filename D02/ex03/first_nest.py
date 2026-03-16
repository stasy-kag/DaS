import sys
import os


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        if not os.path.exists(self.path):
            raise Exception(f"Файл {self.path} не существует.")
        with open(self.path, "r", encoding="utf-8") as file:
            lines = file.read().strip().split("\n")

        if len(lines) < 1:
            raise Exception("Файл пустой.")

        if has_header:
            header = lines[0].split(",")
            if len(header) != 2:
                raise Exception("Неверный заголовок.")
            lines = lines[1:]
            if not lines:
                raise Exception("Нет данных в файле.")

        result = []
        for line in lines:
            cols = line.split(",")
            if len(cols) != 2:
                raise Exception(
                    f"Неверное количество колонок: {len(cols)}. Должно быть 2"
                )
            if cols[0] not in ("0", "1") or cols[1] not in ("0", "1"):
                raise Exception("Некорректное содержание колонок. Должно быть 0 или 1")
            if int(cols[0]) + int(cols[1]) != 1:
                raise Exception("Значения должны быть противоположными (0,1 или 1,0)")
            result.append([int(cols[0]), int(cols[1])])
        return result

    class Calculations:
        def counts(self, data):
            heads = 0  # количество [0,1] 
            tails = 0  # количество [1,0]
            for row in data:
                if row[0] == 0:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            return (heads / total) * 100, (tails / total) * 100


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Неверное количество аргументов.")

    obj = Research(sys.argv[1])
    data = obj.file_reader()

    print(data)

    calc = obj.Calculations()
    heads, tails = calc.counts(data)
    print(heads, tails)

    frac = calc.fractions(heads, tails)
    print(*frac)
