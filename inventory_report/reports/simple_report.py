from collections import Counter

import datetime


class SimpleReport:
    @staticmethod
    def generate(data: list):
        fabrication_date = []
        best_before_date = []
        companies = []

        for product in data:
            fabrication_date.append(
                datetime.strptime(
                    product.data_de_fabricacao, "%Y/%m/%d"
                ).date()
            )
            best_before_date.append(
                datetime.strptime(product.data_de_validade, "%Y/%m/%d").date()
            )
            companies.append(product.nome_da_empresa)

        most_common_company = Counter(companies).most_common(1)(0)

        for date in best_before_date:
            if date < datetime.date.today():
                best_before_date.remove(date)

        return (
            f"Data de fabricação mais antiga: {min(fabrication_date)}\n"
            f"Data de validade mais próxima: {max(best_before_date)}\n"
            f"Empresa com mais produtos: {most_common_company}\n"
        )
