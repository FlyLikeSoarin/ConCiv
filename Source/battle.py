from map import Map
from map import Vector2i
from fraction import Fraction
from itertools import count
from units import Unit
from city import City
from random import randint


def next_fraction(current_player_id, fraction_num):
    return current_player_id % fraction_num


def random_pos(borders):
    return Vector2i(randint(0, borders.x - 1), randint(0, borders.y - 1))


class Battle1v1:
    def __init__(self, fraction_files, map_file):

        self.id_counter = count()

        self.fractions = []
        for file in fraction_files:
            self.fractions.append(Fraction(file, self.id_counter))

        self.fraction_num = len(self.fractions)
        self.current_player_id = 0

        self.current_player = self.fractions[0].name

        self.objects = dict()

        self.map = Map(Vector2i(0, 0))
        self.map.load_map(map_file)

        for fraction in self.fractions:
            city = fraction.get_city()

            self.objects[city.object_id] = city
            self.map.add_entity(city.object_id, random_pos(self.map.size), fraction.name, 'City')

        self.state = 'choosing object'
        self.current_unit = -1
        self.decision_list = []

    def draw(self):

        str_list = [' ' for i in range(24)]
        str_list[0] = (' ' * 36) + '<< ' + self.current_player + '\'s turn >>'

        if self.state == 'choosing object':
            for i in range(20):
                str_list[i + 2] = str_list[i + 2] + ''.join([str(self.map.surface_table[i][j]) for j in range(20)])

            str_list[2] = str_list[2] + '               << Choose unit/city >>'
            self.decision_list = list()

            for key, obj in self.objects.items():
                if obj.fraction == self.current_player:
                    self.decision_list.append(obj)

            for i in range(len(self.decision_list)):
                str_list[3 + i] += '         ' + str(i) + '. ' + self.decision_list[i].name + \
                                   ' - ' + self.decision_list[i].get_info()

            str_list[3 + i + 1] += '        ' + str(-1) + '. ' + 'end turn'

            return '\n'.join(str_list)

        elif self.state == 'choosing action':
            for i in range(9):
                for j in range(9):

                    str_list[2 + i * 2] += str(self.map.get_tile(
                        self.map.get_position(self.current_unit) + Vector2i(i - 4, j - 4)
                        , self.current_player)[0])
                    str_list[3 + i * 2] += str(self.map.get_tile(
                        self.map.get_position(self.current_unit) + Vector2i(i - 4, j - 4)
                        , self.current_player)[1])

            if isinstance(self.objects[self.current_unit], Unit):

                str_list[2] = str_list[2] + '               << Choose action >>'
                self.decision_list = list()

                for action in self.objects[self.current_unit].command_list():
                    self.decision_list.append(action)

                for i in range(len(self.decision_list)):
                    str_list[3 + i] += '         ' + self.decision_list[i]

            if isinstance(self.objects[self.current_unit], City):

                str_list[2] = str_list[2] + '               << Choose product >>'
                self.decision_list = list()

                for product in self.objects[self.current_unit].get_product_list():
                    self.decision_list.append(product)

                for i in range(len(self.decision_list)):
                    str_list[3 + i] += '         ' + self.decision_list[i]

            return '\n'.join(str_list)

    def input_command(self, command):
        if self.state == 'choosing object':
            try:
                object_local_id = int(command)

                if object_local_id == -1:
                    self.state == 'choosing object'
                    self.current_player_id += 1
                    self.current_player = self.fractions[
                        next_fraction(self.current_player_id, self.fraction_num)
                    ].name
                    if next_fraction(self.current_player_id, self.fraction_num) == 0:
                        for key, map_object in self.objects.items():
                            map_object.next_turn()

                            if isinstance(map_object, City):
                                if map_object.is_ready():

                                    new_unit = map_object.get_unit()
                                    self.objects[new_unit.object_id] = new_unit
                                    self.map.add_entity(new_unit.object_id,
                                                        self.map.get_position(map_object.object_id),
                                                        self.current_player, 'Unit')
                    return

                self.current_unit = self.decision_list[object_local_id].object_id
                self.state = 'choosing action'
            except Exception:
                print('wrong input')

        elif self.state == 'choosing action':
            if isinstance(self.objects[self.current_unit], Unit):
                try:
                    exec_str = self.objects[self.current_unit].take_action(command)
                    self.map.execute_string(exec_str, self.current_unit)
                    self.state = 'choosing object'
                except Exception:
                    print('wrong command')

            elif isinstance(self.objects[self.current_unit], City):
                try:
                    self.objects[self.current_unit].start_production(command)
                    self.state = 'choosing object'
                except Exception:
                    print('wrong product')




