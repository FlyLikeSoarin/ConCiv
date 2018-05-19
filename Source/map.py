from units import Unit
from city import City


def two_last_digits(i):
    if 10 > i >= 0:
        return '0' + str(i)
    else:
        return str(i)[-2:]


class Vector2i:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __add__(self, other):
        return Vector2i(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class SurfaceTile:

    def __init__(self, walkable, str_texture, save_symbol):
        self.walkable = walkable
        self.str_texture = str_texture

    def __repr__(self):
        return self.save_symbol

    def __str__(self):
        return self.save_symbol

    save_symbol = '#'


class Ocean(SurfaceTile):

    def __init__(self):
        self.walkable = False
        self.str_texture = ['~~~~', '~~~~']

    save_symbol = 'o'


class Mountain(SurfaceTile):

    def __init__(self):
        self.walkable = False
        self.str_texture = ['^^^^', '^^^^']

    save_symbol = 'm'


class Savanna(SurfaceTile):

    def __init__(self):
        self.walkable = True
        self.str_texture = ['%%%%', '%%%%']

    save_symbol = 's'


class Forest(SurfaceTile):

    def __init__(self):
        self.walkable = True
        self.str_texture = ['@@@@', '||||']

    save_symbol = 'f'


class EmptyTile(SurfaceTile):

    def __init__(self):
        self.walkable = False
        self.str_texture = ['    ', '    ']

    save_symbol = ' '


class UnitTile(SurfaceTile):

    def __init__(self, fraction):
        self.walkable = False
        self.str_texture = ['UNIT', str(fraction[0:4])]

    save_symbol = 'u'


class CityTile(SurfaceTile):

    def __init__(self, fraction):
        self.walkable = False
        self.str_texture = ['CITY', str(fraction[0:4])]

    save_symbol = 'c'


class Map:

    def __init__(self, size):
        self.size = Vector2i(size.x, size.y)

        self.empty_object = -1
        self.default_tile = Savanna()

        self.surface_table = [
            [self.default_tile for i in range(self.size.y)] for j in range(self.size.x)
        ]
        self.object_dict = dict()
        self.fraction_dict = dict()
        self.type_dict = dict()

    def load_map(self, filename):

        with open(filename, 'r') as file:

            self.size = Vector2i(*file.readline().split())
            self.surface_table = [
                [self.default_tile for i in range(self.size.y)] for j in  range(self.size.x)
            ]
            self.object_dict = dict()

            for i in range(self.size.y):
                raw_line = file.readline()
                line = raw_line.split()

                for j in range(self.size.x):

                    if line[j] == Mountain.save_symbol:
                        self.surface_table[i][j] = Mountain()

                    elif line[j] == Ocean.save_symbol:
                        self.surface_table[i][j] = Ocean()

                    elif line[j] == Savanna.save_symbol:
                        self.surface_table[i][j] = Savanna()

                    elif line[j] == Forest.save_symbol:
                        self.surface_table[i][j] = Forest()

    def save_map(self, filename):

        with open(filename, 'w') as file:

            file.write(str(self.size.x))
            file.write(' ')
            file.write(str(self.size.y))
            file.write('\n')

            for i in range(self.size.y):

                for j in range(self.size.x):

                    file.write(str(self.surface_table[i][j]))
                    file.write(' ')

                file.write('\n')

    def add_entity(self, entity_id, pos, fraction, type):

        if pos.x in range(self.size.x) and pos.y in range(self.size.y):
            self.object_dict[entity_id] = pos
            self.fraction_dict[entity_id] = fraction
            self.type_dict[entity_id] = type

    def rem_entity(self, entity_id):

        self.object_dict.pop(entity_id)

    def get_position(self, entity_id):
        return self.object_dict[entity_id]

    def get_tile(self, tile_pos, current_player):

        for target_id, pos in self.object_dict.items():
            if pos == tile_pos:
                if self.type_dict[target_id] == 'Unit':
                    return UnitTile(self.fraction_dict[target_id]).str_texture
                elif self.type_dict[target_id] == 'City':
                    return CityTile(self.fraction_dict[target_id]).str_texture
        if tile_pos.x in range(self.size.x) and tile_pos.y in range(self.size.y):
            return self.surface_table[tile_pos.x][tile_pos.y].str_texture
        else:
            return EmptyTile().str_texture

    def move(self, direction, entity_id):

        offsets = {'r': Vector2i(0, 1), 'l': Vector2i(0, -1),
                   'd': Vector2i(1, 0), 'r': Vector2i(-1, 0)}
        dest_pos = self.object_dict[entity_id] + offsets[direction]
        if dest_pos not in self.object_dict.items()\
                and self.surface_table[dest_pos.x][dest_pos.y].walkable:
            self.object_dict[entity_id] = self.object_dict[entity_id] + offsets[direction]

    def attack(self, offset, entity_id):

        for target_id, pos in self.object_dict.items():
            if pos == self.object_dict[entity_id] + offset:
                return target_id
        return -1

    def execute_string(self, exec_string, entity_id):

        exec_list = exec_string.split('_')
        results = []

        for command in exec_list:

            if command[0] == 'm':
                self.move(command[1], entity_id)
                results.append(['moved'])

            if command[0] == 's':
                pos = self.get_position(entity_id)
                self.rem_entity(entity_id)
                results.append(['city build', pos])

            '''if command[0] == 'a':
                print(int((str(command[1:]).split('^'))[0]),
                      int((str(command[1:]).split('^'))[0]))
                target_id = self.attack(
                    Vector2i(int((str(command[1:]).split('^'))[0]),
                             int((str(command[1:]).split('^'))[0])),
                    entity_id
                )
                results.append(['damaged', target_id])'''

            if command[0] == 'd':
                results.append(['died'])

        return results

