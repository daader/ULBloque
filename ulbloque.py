def get_width(lines) -> int:
    texte = lines[0]
    return len(texte) - 2

def get_height(lines) -> int:
    return len(lines) - 3

def get_moves(lines) -> int:
    return int(lines[-1])

def get_cars(lines) -> list:
    car_dict = dict()
    for i in range(1, len(lines)-2):
        for j, element in enumerate(lines[i]):
            if element.isalpha():
                car_dict.setdefault(element, []).append((j-1,i-1))
    
    cars = [[] for i in range(len(car_dict))]
    for i, element in enumerate(car_dict):
        cars[i].append(car_dict[element][0])
        if car_dict[element][0][1] == car_dict[element][1][1]:
            cars[i].append('h')
        else:
            cars[i].append('v')

        cars[i].append(len(car_dict[element]))

    car_list = list(car_dict.keys())
    voiture_a = car_list.index('A')
    temp_a = cars[voiture_a]
    del cars[voiture_a]
    cars = [temp_a] + cars
    return cars

map = 'game1.txt' # a enlever et remplacer par argv
def file_decoder(map) -> tuple:
    with open(map, 'r') as gamefile: 

        lines = [line.strip() for line in gamefile.readlines()]

        width = get_width(lines)
        height = get_height(lines)
        moves = get_moves(lines)
        cars = get_cars(lines)

    return width, height, cars, moves

def game_creator(map):

    file_decode = file_decoder(map)

    game = dict()

    game['width'] = file_decode[0]
    game['height'] = file_decode[1]
    game['cars'] = file_decode[2]
    game['max_moves'] = file_decode[3]
    parking_display(game['width'],game['height'])
    return game

def parking_display(width, height):

    display_list = []

    for i in range(height):
        for i in range(width):
            display_list.append("\u001b[41m  \u001b[0m")
        display_list.append('\n')
    print(display_list)
    # for element in display_list:
    #     print(element, end='')

game_creator(map)