from facade import *


def main():
    products = read_db('./data/accdb/spravochnik_tovarov.accdb')
    subcategory_products = get_subcategories(products)

    subcategory_groups = {}
    for subcategory, prods in subcategory_products.items():
        subcategory_groups[subcategory] = get_groups(prods)

    subcategory_groups_products = {}
    for subcategory, prods in subcategory_products.items():
        subcategory_groups_products[subcategory] = {}
        for g in subcategory_groups[subcategory]:
            if g not in subcategory_groups_products[subcategory]:
                subcategory_groups_products[subcategory][g] = []
        for p in prods:
            prod_group = choose_group(p, subcategory_groups[subcategory])
            subcategory_groups_products[subcategory][prod_group].append(p)


if __name__ == '__main__':
    main()
