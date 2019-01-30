# -*- coding: utf-8 -*-
"""
ディレクトリ、ファイルなどを操作する関係の汎用スクリプト
"""
import os
import re
import shutil


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


def my_rm(path):
    """
    ファイルやディレクトリ消す
    存在しない場合はなにもしない
    :param path: 消すファイルやディレクトリのパス
    """
    if not os.path.exists(path):
        return

    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(os.path.join(path))

    print ("{}を消しました".format(path))


def delete_pyc(path, is_echo_delete_file_path = False):
    """
    .pycファイルを全部削除する
    :param path:
    :param is_echo_delete_file_path:
    :return:
    """
    count = 0
    for dirpath, _, filenames in os.walk(path):
        #print("{0}を検索しています...".format(dirpath))
        #for dr in dirnames:
        #    print("{0}というディレクトリがあります".format(dr))
        for file in filenames:
            if file[-4:] == ".pyc":
                if is_echo_delete_file_path:
                    print("Delete: " + dirpath + file)
                os.remove(os.path.join(dirpath, file))
                count += 1

    print("Done. Delete .pyc File Count is {}".format(count))

