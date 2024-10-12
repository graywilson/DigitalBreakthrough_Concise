from product import Product


def read_db() -> list[Product]:
    pass


def get_subcategories(products: list[Product]) -> list[list[Product]]:
    pass


def get_groups(subcategory: list[Product]) -> list[str]:
    pass


def choose_group(product: Product, groups: list[str]) -> str:
    pass


def get_group_properties(group: list[Product]) -> list[str]:
    pass


def get_product_properties(product: Product, properties: list[str]):
    pass


def save_table(products: Product, group_name: str, properties: list[str]):
    pass
