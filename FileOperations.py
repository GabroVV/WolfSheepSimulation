import csv
import json


class FileOperations:

    @staticmethod
    def create_csv():
        with open('alive.csv', 'w', encoding='UTF-8', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Turn number', 'Number of alive sheep'])

    @staticmethod
    def append_to_csv(list):
        with open('alive.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(list)

    @staticmethod
    def create_json(list):
        with open('pos.json', 'w') as file:
            json.dump(list, file, indent=1)

    @staticmethod
    def append_to_json(dictionary):
        with open('pos.json', 'a') as file:
            file.seek(0, 2)
            size = file.tell()
            file.truncate(size-4)
            file.write(json.dumps(dictionary, indent=True))
            file.write(",]}  ")

    @staticmethod
    def delete_last_coma(self):
        with open('pos.json', 'a') as file:
            file.seek(0, 2)
            size = file.tell()
            file.truncate(size-5)
            file.write("]}  ")
