import csv
from json import load
from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport
import xml.etree.ElementTree as ET


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
        if "xml" in path:
            with open(path) as file:
                xml_reader = ET.parse(path)
                xml_dom_elements = xml_reader.getroot()
                xml_list = Inventory.generate_xml_list(xml_dom_elements)
                return Inventory.generate_report(xml_list, type)

    @staticmethod
    def generate_report(list, type):
        if type == "simples":
            return SimpleReport.generate(list)
        elif type == "completo":
            return CompleteReport.generate(list)
        else:
            raise ValueError

    @staticmethod
    def generate_xml_list(xml):
        xml_list = []

        for elem in xml.findall("./record"):
            product_info = {}
            for product in elem:
                product_info[product.tag] = product.text
            xml_list.append(product_info)
        return xml_list
