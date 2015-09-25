# -*- coding: utf8 -*-
"""
bashの出力で色をつけるカラーコード定義
ex)
    red("test")
"""
def get_color(colorname):
    colors = {
        'clear': '\033[0m',
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
        }

    def func2(c):
        return "{}{}{}".format(colors[colorname], c, colors['clear'])

    return func2

black  = get_color('black')
red    = get_color('red')
green  = get_color('green')
yellow = get_color('yellow')
blue   = get_color('blue')
purple = get_color('purple')
cyan   = get_color('cyan')
white  = get_color('white')

if __name__ == "__main__":
    a = "this is a test message"
    print(red(a))
    print(white(a))
    print(cyan(a))
    print(purple("test ") + yellow("message"))