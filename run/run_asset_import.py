# -*- coding: utf-8 -*-
"""
Unityの起動時間を短縮するため、時間があるときに起動しておくコマンド
"""
import os
import subprocess
from yui.constants import (
    YUI_ROOT, YUI_UNITY_PATH
)

# 起動するUnityプロジェクトパスのリスト
path_list = (
    os.path.join(YUI_ROOT, "resources/yui"),
    os.path.join(YUI_ROOT, "resources_develop_ios/yui"),
    os.path.join(YUI_ROOT, "client_yui_android/yui"),
)

for path in path_list:
    os.chdir(path)
    print("{}のブランチ".format(path))
    subprocess.call("git rev-parse --abbrev-ref HEAD", shell=True)
    subprocess.call("git pull", shell=True)
    subprocess.call(
        "{} -quit -batchmode -projectPath {}".format(
            YUI_UNITY_PATH, path
        ),
        shell=True
    )
    print("")

print("Done")
