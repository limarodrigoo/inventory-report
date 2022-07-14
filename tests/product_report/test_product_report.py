from inventory_report.inventory.product import Product


def test_relatorio_produto():

    id = 28
    product_name = "Coca Cola"
    product_company = "Coca Cola"
    manufactured = "12/03/22"
    best_before = "12/03/23"
    serial_number = "123456"
    storage_instructions = ("Reservar gelado",)
    coke = Product(
        id,
        product_name,
        product_company,
        manufactured,
        best_before,
        serial_number,
        storage_instructions,
    )

    assert str(coke) == (
        f"O produto {product_name}"
        f" fabricado em {manufactured}"
        f" por {product_company} com validade"
        f" até {best_before}"
        f" precisa ser armazenado {storage_instructions}."
    )
