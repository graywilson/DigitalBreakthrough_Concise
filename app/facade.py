from product import Product
from db.access_reader import AccessReader


def read_db(db_filepath: str) -> list[Product]:
    """

    :param db_filepath: путь до БД
    :return: список объектов Product (перенос записей таблиц в объекты)
    """
    access_reader = AccessReader()
    db_records = access_reader.read_all(db_filepath)
    products = []
    for record in db_records:
        products.append(Product(record[0], record[1], record[6], record[5], parameters=record[4], gost=record[3],
                                marking=record[2]))
    return products


def get_subcategories(products: list[Product]) -> list[list[Product]]:
    """

    :param products: список объектов Product
    :return: список подкатегорий с товарами, объединенными по ОКПД2
    """
    pass


def get_groups(subcategory: list[Product]) -> list[str]:
    """

    :param subcategory: список товаров одной подкатегории
    :return: список групп для данной подкатегории
    """
    pass


def choose_group(product: Product, groups: list[str]) -> str:
    """

    :param product: товар
    :param groups: группы для подкатегории, к которой относится товар
    :return: группа, к которой товар должен быть отнесен
    """
    pass


def get_group_properties(group: list[Product]) -> list[str]:
    """

    :param group: группа с товарами в ней
    :return: свойства для данной группы
    """
    pass


def get_product_properties(product: Product, properties: list[str]):
    """

    :param product: товар
    :param properties: свойства группы товара, в которые необходимо разложить параметры товара
    :return:
    """
    pass


def save_table(products: list[Product], group_name: str, properties: list[str]):
    """

    :param products: список товаров
    :param group_name: название группы, к которой относятся товары
    :param properties: список свойств группы
    :return:
    """
    pass
