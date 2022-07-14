from inventory_report.inventory.product import Product


def test_relatorio_produto():

    coke = Product(
        28,
        "Coca Cola",
        "Coca Cola",
        "12/03/22",
        "12/03/23",
        "123456",
        "Reservar gelado",
    )

    assert str(coke) == (
        "O produto Coca Cola fabricado em 12/03/22 "
        "por Coca Cola com validade até 12/03/23 "
        "precisa ser armazenado Reservar gelado"
    )
