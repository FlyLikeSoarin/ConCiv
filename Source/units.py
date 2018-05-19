from map_object import MapObject
import copy


class Command:
    def __init__(self, name, cost, description, exec_string):
        self.name = name
        self.cost = int(cost)
        self.description = description
        self.exec_string = exec_string

class UnitPrototype:
    def __init__(self, id_counter):
        self.__units_proto = dict()
        self.__production_needed = dict()
        self.__description = dict()
        self.__id_counter = id_counter

    def register_unit(self, unit_prototype, prod_needed, description):
        self.__units_proto[unit_prototype.name] = unit_prototype
        self.__production_needed[unit_prototype.name] = int(prod_needed)
        self.__description[unit_prototype.name] = description

    def unregister_object(self, name):
        del self.__units_proto[name]
        del self.__production_needed[name]
        del self.__description[name]

    def get_needed_production(self, name):
        return self.__production_needed[name]

    def get_unit_list(self):
        units = []
        for unit in self.__units_proto.keys():
            current_unit = unit + ' (' + str(self.__production_needed[unit]) + ' production)'
            current_unit = current_unit + ' - ' + self.__description[unit]
            units.append(current_unit)
        return units

    def clone(self, name):
        unit_instance = copy.deepcopy(self.__units_proto.get(name))
        unit_instance.object_id = next(self.__id_counter)
        return unit_instance


class Unit(MapObject):

    def __init__(self, name, fraction, armour, attack, max_turn_actions):
        super(Unit, self).__init__(name, fraction, armour, attack)
        self.__command_list = []
        self.__max_turn_actions = int(max_turn_actions)
        self.__actions_left = 0

    def next_turn(self):
        self.__actions_left = self.__max_turn_actions

    def add_command(self, command):
        self.__command_list.append(command)

    def command_list(self):
        actions = []
        for action in self.__command_list:
            actions.append(action.name + ' - ' + action.description)
        return actions

    def take_action(self, command):
        for action in self.__command_list:
            if action.name == command and action.cost <= self.__max_turn_actions:
                self.__max_turn_actions -= action.cost
                return action.exec_string
        return '0'

    def get_info(self):
        return str(self.health) + ' health points'

class UnitBuilder:

    def __init__(self, fraction):
        self.__fraction = fraction

    def create_instance(self, unit_string):
        unit_decoded = unit_string.split('\n')
        unit_head = unit_decoded[0].split()
        unit_decoded.pop(0)
        unit = Unit(unit_head[0], self.__fraction, unit_head[2],
                    unit_head[3], unit_head[4])
        for command in unit_decoded:
            com_head = command.split(', ')
            unit.add_command(Command(com_head[0], com_head[1], com_head[2], com_head[3]))
        return unit




