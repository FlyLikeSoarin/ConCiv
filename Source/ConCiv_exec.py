from Source import fraction

zebras = fraction.Fraction('Source/zebras.txt')
city1 = zebras.get_city()
print(city1.get_product_list(), sep='\n')
city1.start_production('archer')
units = []
for i in range(6):
    print(city1.get_info())
    if city1.next_turn():
        units.append(city1.get_unit())

city1.start_production('archer')
for i in range(6):
    print(city1.get_info())
    if city1.next_turn():
        units.append(city1.get_unit())

units[0].next_turn()

for unit in units:
    print(unit.command_list())

print(units[0].take_action('ml'))