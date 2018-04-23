class MapObject:

    def __init__(self, name, fraction, armour, attack):
        self.name = name
        self.fraction = fraction
        self.health = 100
        self.armour = armour
        self.attack = attack
        self.object_id = -1

    def get_info(self):
        return ''
