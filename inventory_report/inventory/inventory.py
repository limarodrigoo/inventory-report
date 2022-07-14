import csv
from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        with open(path, encoding="utf-8") as file:
            csv_report = csv.DictReader(file)
            csv_list = list(csv_report)
            if type == "simples":
                return SimpleReport.generate(csv_list)
            elif type == "completo":
                return CompleteReport.generate(csv_list)
            else:
                raise ValueError
