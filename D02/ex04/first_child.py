import sys
from random import randint


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):

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

        data = []
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
            data.append([int(cols[0]), int(cols[1])])
        return data

    class Calculations:

        def __init__(self, data):
            self.data = data

        def counts(self):
            tails = 0  # количество [0,1]
            heads = 0  # количество [1,0]
            for row in self.data:
                if row[0] == 0:
                    tails += 1
                else:
                    heads += 1
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            return (heads / total) * 100, (tails / total) * 100

    class Analytics(Calculations):
        def predict_random(self, num_predict):
            l = []
            for _ in range(num_predict):
                num = randint(0, 1)
                l.append([num, 1 - num])
            return l

        def predict_last(self):
            return self.data[-1]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Неверное количество аргументов.")
    obj = Research(sys.argv[1])
    data = obj.file_reader()
    print(data)

    calc = obj.Calculations(data)
    heads, tails = calc.counts()
    print(heads, tails)

    frac = calc.fractions(heads, tails)
    print(*frac)

    analytic = Research.Analytics(data)
    print(*analytic.predict_random(4))
    print(analytic.predict_last())
