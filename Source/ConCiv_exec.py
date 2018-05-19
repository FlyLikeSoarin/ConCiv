from battle import Battle1v1


i_battle = Battle1v1(['zebras.txt', 'ponies.txt'], 'map.txt')

isPlaying = True

while isPlaying:
    print(i_battle.draw())
    command = input(' INPUT COMMAND >> ')
    i_battle.input_command(command)