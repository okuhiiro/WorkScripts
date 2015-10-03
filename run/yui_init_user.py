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
# クライアントのリポジトリはclientという文字列を含むフォルダである必要がある
init_dir = select_dir(YUI_ROOT, re.compile(r'.*client.*'))

print("clientリポジトリ({}フォルダ)のユーザを初期化します\n".format(init_dir))

replace_client_repo_root_path = os.path.join(YUI_ROOT, init_dir)
client_repo_resouces_path = os.path.join(
    replace_client_repo_root_path, YUI_CLIENT_RESOUCES_FOR_ROOT)

os.remove(os.path.join(client_repo_resouces_path, "Yui_Player_uuid.txt"))
os.remove(os.path.join(client_repo_resouces_path, "Yui_Player_Device_Id.txt"))

# try:
#     os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfo.csv"))
# except:
#     pass
# try:
#     os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfo.csv.meta"))
# except:
#     pass
# try:
#     os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfoNew.csv"))
# except:
#     pass
# try:
#     os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfoNew.csv.meta"))
# except:
#     pass
# try:
#     os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfoTutorial.csv"))
# except:
#     pass
# try:
#     os.remove(os.path.join(client_repo_resouces_path, "ResFileVersionInfoTutorial.csv.meta"))
# except:
#     pass

print("初期化完了")
