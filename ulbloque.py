from sys import argv
from getkey import getkey

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

def parse_game(map):

    file_decode = file_decoder(map)

    game = dict()

    game['width'] = file_decode[0]
    game['height'] = file_decode[1]
    game['cars'] = file_decode[2]
    game['max_moves'] = file_decode[3]
    return game

def parking_display(width, height):

    display_list = []

    for i in range(height):
        for i in range(width):
            display_list.append("\u001b[40m  \u001b[0m")
        display_list.append('\n')
    return display_list

def car_formatter(car, name):

    car_colors = ["\u001b[41m", "\u001b[42m", "\u001b[43m", "\u001b[44m", "\u001b[45m", "\u001b[46m"]
    first_car_color = "\u001b[47m"

    if name == 'A':
        car_format = first_car_color + " " + name + "\u001b[0m"
    else:
        order = ord(name) - ord('A')
        color_code = order % 6
        car_format = car_colors[color_code] + " " + name + "\u001b[0m" 
    return car_format

def car_list_inserter(display_list, car, letter, width):
    if car[2] != 0:
        x, y = car[0]
        order = x + y * width + y
        display_list[order] = car_formatter(car, letter)
        if car[2] > 1:
            for i in range(car[2]):
                if car[1] == 'h':
                    order = x+i + y * width + y
                    display_list[order] = car_formatter(car, letter)
                else:
                    order = x + (y+i) * width + (y+i)
                    display_list[order] = car_formatter(car, letter)
    return display_list

def get_game_str(game, move):

    height = game['height']
    width = game['width']

    test_car = [(2,2), 'v', 4]
    display_list = parking_display(game['height'], game['width'])
    for i, car in enumerate(game['cars']):
        letter = chr(65+i)
        car_list_inserter(display_list, car, letter, game['width'])
    game_string = f'move: {move}/{game['max_moves']}\n'
    for element in display_list:
        game_string += element

    return game_string

# def car_remover(game: dict , car_index:int ):
#     game['cars'][car_index] = 0
#     return game


def move_car(game: dict, car_index: int, direction: str):
        game_backup = game

        if direction == 'DOWN':
            x, y = game["cars"][car_index][0]
            game["cars"][car_index][0] = (x, y+1)
        elif direction == 'UP':
            x, y = game["cars"][car_index][0]
            game["cars"][car_index][0] = (x, y-1)
        elif direction == 'LEFT':
            x, y = game["cars"][car_index][0]
            game["cars"][car_index][0] = (x-1, y)
        elif direction == 'RIGHT':
            x, y = game["cars"][car_index][0]
            game["cars"][car_index][0] = (x+1, y)
        x, y = game["cars"][car_index][0]

        if game["cars"][car_index][1] == 'h':
            if (game["cars"][car_index][0][0] + game["cars"][car_index][2]) <= game["height"]:
                return True
            else:
                game = game_backup
                return False
        else:
            if (game["cars"][car_index][0][1] + game["cars"][car_index][2]) <= game["width"]:
                return True
            else:
                game = game_backup
                return False
            
# def is_win(game: dict) -> bool:

#     if game["cars"][1]== 'h':
#         if game["cars"][0][0][1] > (game['width']):
#             return True
#         else:
#             return False
#     else:
#         if game["cars"][0][0][0] >= (game['height']):
#             return True
#         else:
#             return False

print(get_game_str(parse_game(map), 3))