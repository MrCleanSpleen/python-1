'''This is my colors module.

Here is my description of my module.
'''
import random as r

blue = '\033[0;34m'
green = '\033[0;32m'
red = '\033[0;31m'
orange = '\033[1;31m'
purple = '\033[1;35m'
yellow = '\033[0;33m'
magenta = '\033[0;35m'
cyan = '\033[0;36m'
base3 = '\033[1;37m'
base2 = '\033[0;37m'
base1 = '\033[1;36m'
base0 = '\033[1;34m'
base00 = '\033[1;33m'
base01 = '\033[1;32m'
base02 = '\033[0;30m'
base03 = '\033[1;30m'
reset = '\033[0m'
clear = '\033[H\033[2J'

def random_color():
    return r.choice([cyan, red, blue, green, yellow, orange, purple])

if __name__ == '__main__':
    print(clear)
    print(red + 'Red' + reset)
    print(blue + 'Blue' + reset)
    print(green + 'Green' + reset)
    print(purple + 'Purple' + reset)
    print(yellow + 'Yellow' + reset)
    print(orange + 'Orange' + reset)
    print(cyan + 'Cyan' + reset)
    print(base3 + 'Base3' + reset)
    print(base2 + 'Base2' + reset)
    print(base1 + 'Base1' + reset)
    print(base0 + 'Base0' + reset)
    print(base00 + 'Base00' + reset)
    print(base01 + 'Base01' + reset)
    print(base02 + 'Base02' + reset)
    print(base03 + 'Base03' + reset)
