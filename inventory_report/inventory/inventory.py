import csv
from json import load
from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        if "csv" in path:
            with open(path, encoding="utf-8") as file:
                csv_report = csv.DictReader(file)
                csv_list = list(csv_report)
                return Inventory.generate_report(csv_list, type)
        if "json" in path:
            with open(path, encoding="utf-8") as file:
                json_list = load(file)
                return Inventory.generate_report(json_list, type)

    @staticmethod
    def generate_report(list, type):
        if type == "simples":
            return SimpleReport.generate(list)
        elif type == "completo":
            return CompleteReport.generate(list)
        else:
            raise ValueError
