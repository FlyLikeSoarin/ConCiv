from map_object import MapObject
from units import UnitPrototype


class City(MapObject):

    def __init__(self, name, fraction, armour, attack, production, unit_proto):
        super(City, self).__init__(name, fraction, armour, attack)
        self.__production_per_turn = int(production)
        self.__unit_proto = unit_proto
        self.__current_product = ''
        self.__production_needed = 0
        self.__working = False

    def next_turn(self):
        """If return True - product is ready"""
        self.__production_needed -= self.__production_per_turn
        if self.__production_needed <= 0 and self.__working:
            return True
        else:
            return False

    def get_unit(self):
        unit = self.__unit_proto.clone(self.__current_product)
        self.__working = False
        return unit

    def is_ready(self):
        turn_left = max(self.__production_needed // self.__production_per_turn, 0)
        return self.__working and turn_left == 0

    def get_product_list(self):
        return self.__unit_proto.get_unit_list()

    def start_production(self, name):
        self.__working = True
        self.__production_needed = self.__unit_proto.get_needed_production(name)
        self.__current_product = name

    def get_info(self):
        if self.__working:
            turn_left = max(self.__production_needed // self.__production_per_turn, 0)
            info = 'building ' + self.__current_product + ', '
            info = info + str(turn_left) + ' turns until it finished.'
            return info
        else:
            return 'resting...'


class CityBuilder:

    def __init__(self, fraction, std_armour, std_attack, std_production, name_pool, id_counter):
        self.__fraction = fraction
        self.__std_unit_list = UnitPrototype(id_counter)
        self.__id_counter = id_counter
        self.__std_armour = std_armour
        self.__std_attack = std_attack
        self.__std_production = std_production
        self.__name_pool = name_pool

    def create_instance(self):
        name = self.__name_pool.pop()
        city = City(name, self.__fraction, self.__std_armour, self.__std_attack,
                    self.__std_production, self.__std_unit_list)
        city.object_id = next(self.__id_counter)
        return city

    def add_std_unit(self, unit_instance, prod_needed, description):
        self.__std_unit_list.register_unit(unit_instance,
                                           prod_needed, description)


