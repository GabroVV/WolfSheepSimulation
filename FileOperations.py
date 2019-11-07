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
    def create_json():
        with open('pos.json', 'w') as file:
            file.close()




    @staticmethod
    def append_to_json(dictionary):
        with open('pos.json', 'a') as file:
            json.dump(dictionary,file,indent=True)
