# -*- coding: utf-8 -*-
"""
UnityのプレイヤーとDLCを初期化する
"""
import os
import re
import shutil

from yui.constants import (
    YUI_ROOT, YUI_CLIENT_RESOUCES_FOR_ROOT
)
from common.dir_file_manager import select_dir, my_rm

# 初期化するリポジトリフォルダを取得
# クライアントのリポジトリはclientという文字列を含むフォルダである必要がある
init_dir = select_dir(YUI_ROOT, re.compile(r'.*client.*'))

print("clientリポジトリ({}フォルダ)のユーザを初期化します\n".format(init_dir))

replace_client_repo_root_path = os.path.join(YUI_ROOT, init_dir)
client_repo_resouces_path = os.path.join(
    replace_client_repo_root_path, YUI_CLIENT_RESOUCES_FOR_ROOT)

my_rm(os.path.join(client_repo_resouces_path, "Yui_Player_uuid.txt"))
my_rm(os.path.join(client_repo_resouces_path, "Yui_Player_Device_Id.txt"))

my_rm(os.path.join(client_repo_resouces_path, "Data"))
my_rm(os.path.join(client_repo_resouces_path, "ResFileVersionInfo.csv"))
my_rm(os.path.join(client_repo_resouces_path, "ResFileVersionInfo.csv.meta"))
my_rm(os.path.join(client_repo_resouces_path, "ResFileVersionInfoNew.csv"))
my_rm(os.path.join(client_repo_resouces_path, "ResFileVersionInfoNew.csv.meta"))
my_rm(os.path.join(client_repo_resouces_path, "ResFileVersionInfoTutorial.csv"))
my_rm(os.path.join(client_repo_resouces_path, "ResFileVersionInfoTutorial.csv.meta"))


print("初期化完了")
