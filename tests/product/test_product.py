from inventory_report.inventory.product import Product


def test_cria_produto():
    coke = Product(
        28,
        "Coca Cola",
        "Coca Cola",
        "12/03/22",
        "12/03/23",
        "123456",
        "Reservar gelado",
    )

    assert type(coke.id) is int
    assert type(coke.nome_da_empresa) is str
    assert type(coke.nome_do_produto) is str
    assert type(coke.data_de_fabricacao) is str
    assert type(coke.data_de_validade) is str
    assert type(coke.numero_de_serie) is str
    assert type(coke.instrucoes_de_armazenamento) is str

    assert coke.id == 28
    assert coke.nome_da_empresa == "Coca Cola"
    assert coke.nome_do_produto == "Coca Cola"
    assert coke.data_de_fabricacao == "12/03/22"
    assert coke.data_de_validade == "12/03/23"
    assert coke.numero_de_serie == "123456"
    assert coke.instrucoes_de_armazenamento == "Reservar gelado"
