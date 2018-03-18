import random


class NamePool:
    def __init__(self, name_list):
        self.__name_list = name_list

    def pop(self):
        name = self.__name_list[0]
        self.__name_list.pop(0)
        return name

