class Product:
    def __init__(self, smktp: int, name: str, okpd2: str, measure_unit: str, parameters: str = '', gost: str = '',
                 marking: str = '', kategory: str = ''):
        self.smktp = smktp
        self.name = name
        self.okpd2 = okpd2
        self.measure_unit = measure_unit
        self.parameters = parameters
        self.gost = gost
        self.marking = marking
        self.kategory = kategory
        self.properties = {}
