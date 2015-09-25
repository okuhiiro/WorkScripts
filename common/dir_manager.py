# -*- coding: utf-8 -*-
"""
ディレクトリ関係の汎用スクリプト
"""
import os
import re


def select_dir(path, pattern):
    """
    対話形式でディレクトリを選択させる
    path: 選択するディレクトリパス
    pattern: pathの階層にあるディレクトリをフィルターするためのパターン
            ex) re.compile(r'.*resources.*')
    return: 選択したディレクトリの名前
    """
    dirs = os.listdir(path)
    i = 0
    select_dirs = []
    for name in dirs:
        if re.search(pattern, name):
            print(str(i) + ") " + name)
            select_dirs.append(name)
            i += 1

    if not select_dirs:
        raise ValueError(
            "{}にはパターン{}に一致するフォルダがありません".format(
                path, pattern))

    num = input("フォルダを番号で指定してください > ")
    try:
        num = int(num)
    except ValueError:
        raise ValueError("フォルダ番号が間違っています")
    try:
        select_dir = select_dirs[num]
    except IndexError:
        raise ValueError("存在しないフォルダ番号です")

    return select_dir




