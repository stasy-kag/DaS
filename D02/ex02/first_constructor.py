import os
import sys


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):

        if not os.path.exists(self.path):
            raise Exception(f"Файл {self.path} не существует.")

        with open(self.path, "r", encoding="utf-8") as file:
            lines = file.read().strip().split("\n")

            if len(lines) < 1:
                raise Exception("Мало строк в файле")

            header = lines[0].strip().split(",")
            if len(header) != 2:
                raise Exception("Неверный заголовок.")

            for line in lines[1:]:
                line = line.split(",")
                if len(line) != 2:
                    raise Exception(
                        f"Неверное количество колонок:{len(line)}. Должно быть 2"
                    )
                if line[0] not in ("0", "1") or line[1] not in ("0", "1"):
                    raise Exception(
                        "Некорректное содержание колонок. Должно быть 0 или 1"
                    )
                if int(line[0]) + int(line[1]) != 1:
                    raise Exception(
                        "Значения должны быть противоположными (0,1 или 1,0)"
                    )

            return ("\n").join(lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception(
            f"Неверное количество аргументов: {len(sys.argv)}. Должно быть 2 аргумента!"
        )

    obj = Research(sys.argv[1])
    print(obj.file_reader())
