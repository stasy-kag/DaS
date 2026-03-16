import os
import logging
import requests
import json
from random import randint

logging.basicConfig(
    filename="analytics.log",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
)


class Research:
    def __init__(self, path):
        self.path = path
        logging.debug(f"Research initialized with path: {path}")

    def file_reader(self, has_header=True):
        logging.debug("Reading file...")

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

        logging.debug(f"File successfully read. {len(data)} rows loaded.")
        return data

    def send_message(self, url, text):
        logging.debug("Sending message to Telegram")
        try:
            payload = {"text": text}
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                url, data=json.dumps(payload), headers=headers, timeout=10
            )

            if response.status_code != 200:
                logging.error(f"Ошибка при отправке в Telegram: {response.text}")
            else:
                logging.info("Сообщение успешно отправлено в Telegram")

        except Exception as e:
            logging.error(f"Не удалось отправить сообщение: {e}")

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.debug("Calculations initialized")

        def counts(self):
            logging.debug("Calculating the counts of heads and tails")
            heads = 0
            tails = 0
            for row in self.data:
                if row[0] == 0:
                    heads += 1
                else:
                    tails += 1
            return heads, tails

        def fractions(self, heads, tails):
            logging.debug("Calculating fractions")
            total = heads + tails
            frac_heads = (heads / total) * 100
            frac_tails = (tails / total) * 100
            return frac_heads, frac_tails


class Analytics(Research.Calculations):
    def predict_random(self, num_predict):
        logging.debug(f"Predicting {num_predict} random outcomes")
        l = []
        for _ in range(num_predict):
            num = randint(0, 1)
            l.append([num, 1 - num])
        return l

    def predict_last(self):
        logging.debug("Returning last observation")
        return self.data[-1]

    def save_file(self, data, file_name, extension="txt"):
        logging.debug(f"Saving report to file: {file_name}.{extension}")
        full = f"{file_name}.{extension}"

        with open(full, "w", encoding="utf-8") as file:
            file.write(data)
        return full
