from string import ascii_letters
from os import system
from time import sleep
from random import randint

def loh():
    return 0
def create_desk():
    desk = [['-' for i in range(9)] for j in range(9)]

    for i in range(1, 9):
        desk[i][0] = str(i)
        desk[0][i] = ascii_letters[i - 1].upper()
        desk[0][0] = str(' ')

    return desk


def create_dictionary_position():
    return {ascii_letters[i - 1].upper(): i for i in range(1, 9)}


def create_dictionary_color():
    return {'R': 'R', 'G': 'G', 'B': 'B'}


def my_step(desk):
    while True:
        color = input_color()

        insertion_capability = check_color(color, desk)[1]
        avail_pos = check_color(color, desk)[0]

        if insertion_capability:
            print("Possible positions:\n{0}".format(', '.join(avail_pos)))
            position = input_position(avail_pos)
            break
        else:
            print("Select another color!")

    i, j = position_decoding(position)
    desk[i][j] = color

    return desk


def position_decoding(position):
    dict_pos = create_dictionary_position()
    i = int(position[1])
    j = int(dict_pos.get(position[0]))

    return (i, j)


def bot_step(desk):
    # print("Wait for your opponent's move...")
    list_color = ['R', 'G', 'B']

    while True:
        color = get_color((list_color[randint(0, 2)]))
        insertion_capability = check_color(color, desk)[1]
        avail_pos = check_color(color, desk)[0]

        if insertion_capability:
            position = avail_pos[randint(0, len(avail_pos) - 1)]
            break

    i, j = position_decoding(position)
    desk[i][j] = color
    sleep(2)

    return desk


def input_color():
    dict_color = create_dictionary_color()

    while True:
        color = input("Input color(one symbol: R, G or B): ")
        if (color != "exit"):
            if (len(color) == 1) and (color in dict_color.keys()):
                color = get_color(color)
                break
            else:
                print("Unknown color!")
        else:
            exit(0)

    return color


def input_position(available_pos):
    while True:
        position = input("\nInput position: ")
        if (len(position) == 2) and (position in available_pos):
            break
        else:
            print("Unknown position!")

    return position


def play_game(desk):
    step = 0

    while True:
        print_desk(desk)

        if not opportunity_play(desk):
            print("\nYou loose!\nGame over.") if step % 2 == 0 else print(
                "\nYou win!\nGame over.")
            break
        elif step % 2 == 0:
            desk = my_step(desk)
            step += 1
        else:
            desk = bot_step(desk)
            step += 1


def opportunity_play(desk):
    list_color = ['R', 'G', 'B']

    for i in list_color:
        if check_color(get_color(i), desk)[1]:
            break
    else:
        return False
    return True


def check_color(color, desk):
    list_position = []
    flag = False
    color_red = 'R'
    color_green = 'G'
    color_blue = 'B'

    for i in range(1, 9):
        for j in range(1, 9):
            if desk[i][j] != color_red and desk[i][j] != color_green and desk[i][j] != color_blue:

                if j != 8 and i != 8:
                    if (color != desk[i - 1][j]) and (color != desk[i + 1][j]) and (color != desk[i][j - 1]) and (
                            color != desk[i][j + 1]):
                        list_position.append(add_tips(i, j))

                elif j == 8 and i == 8:
                    if color != desk[i - 1][j] and color != desk[i][j - 1]:
                        list_position.append(add_tips(i, j))

                elif j == 8 and i != 8:
                    if color != desk[i - 1][j] and color != desk[i][j - 1] and color != desk[i + 1][j]:
                        list_position.append(add_tips(i, j))

                elif j != 8 and i == 8:
                    if color != desk[i - 1][j] and color != desk[i][j - 1] and color != desk[i][j + 1]:
                        list_position.append(add_tips(i, j))

                if not flag:
                    if len(list_position) != 0:
                        flag = True
    if flag:
        return (list_position, flag)
    else:
        return (0, flag)


def get_color(color):
    if color == 'R':
        color = 'R'
    elif color == 'G':
        color = 'G'
    else:
        color = 'B'
    return color


def add_tips(i, j):
    dict_pos = create_dictionary_position()
    return ''.join([key for key, value in dict_pos.items() if value == j]) + str(i)


def print_desk(desk):
    system('clear')

    for i in range(9):
        for j in range(9):
            print(desk[i][j], end=' ')
        print()


def main():
    desk = create_desk()
    play_game(desk)


if __name__ == "__main__":
    main()
