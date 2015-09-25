# -*- coding: utf-8 -*-
"""
Unityのプレイヤーを初期化(=新規ユーザ)する
"""
import os
import re

from yui.constants import (
    YUI_ROOT, YUI_CLIENT_RESOUCES_FOR_ROOT
)
from common.dir_manager import select_dir

# 初期化するリポジトリフォルダを取得
init_dir = select_dir(YUI_ROOT, re.compile(r'.*client.*'))

print("clientリポジトリ({}フォルダ)のユーザを初期化します\n".format(init_dir))

replace_client_repo_root_path = os.path.join(YUI_ROOT, init_dir)
client_repo_resouces_path = os.path.join(
    replace_client_repo_root_path, YUI_CLIENT_RESOUCES_FOR_ROOT)

os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfo.csv"))
os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfo.csv.meta"))
os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfoNew.csv"))
os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfoNew.csv.meta"))
os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfoTutorial.csv"))
os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfoTutorial.csv.meta"))

print("初期化完了")