from Source import units, name_pool, city


class Fraction:
    def __init__(self, load_file):
        with open(load_file, 'r') as file:
            data = file.read()
        data = data.split('#\n')
        head = data[0].split()
        name_list = data[1].split()
        data.pop(0)
        data.pop(0)
        self.name = head[0]
        self.__unit_builder = units.UnitBuilder(self.name)
        self.__city_builder = city.CityBuilder(head[0], head[1], head[2], head[3],
                                               name_pool.NamePool(name_list))
        for unit_text in data:
            unit_text = unit_text.split('\n')
            production_needed = unit_text[0]
            description = unit_text[1]
            unit_text.pop(0)
            unit_text.pop(0)
            self.__city_builder.add_std_unit(self.__unit_builder.create_instance('\n'.join(unit_text)),
                                             production_needed, description)

    def get_city(self):
        return self.__city_builder.create_instance()


