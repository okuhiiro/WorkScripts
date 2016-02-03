# -*- coding: utf-8 -*-
"""
テスト用
"""
import sys
import subprocess

# pythonバージョン
print(sys.version_info)

# シェル、コマンド実行
subprocess.call("echo 'Hello World.'", shell=True)

# シェル、コマンド実行の結果を受け取る
ret = subprocess.check_output("ls")
print(ret)

# 入力待ち
data = input()

if __name__ == '__main__':
    print("__main__")
