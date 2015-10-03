# -*- coding: utf-8 -*-
"""
serverリポジトリのjsonを、dataリポジトリのjsonに置き換える
"""
import os
import subprocess
import re
from yui.constants import (
    YUI_ROOT,
    YUI_DATA_REPO_ROOT_DIR,
    YUI_DATA_JSON_DIR,
    YUI_SERVER_JSON_FOR_ROOT
)
from common.dir_manager import select_dir

# コピー先のパスを取得
# サーバーのリポジトリはserverという文字列を含むフォルダである必要がある
copy_out = select_dir(YUI_ROOT, re.compile(r'.*server.*'))

print("serverリポジトリのjsonを、dataリポジトリのjsonに置き換えます\n")

os.chdir(YUI_DATA_REPO_ROOT_DIR)
print("現在のdataリポジトリ({})のブランチ".format(YUI_DATA_REPO_ROOT_DIR))
subprocess.call("git rev-parse --abbrev-ref HEAD", shell=True)
print("↓")

replace_server_repo_root_path = os.path.join(YUI_ROOT, copy_out)
os.chdir(replace_server_repo_root_path)
print(
    "現在のserverリポジトリ({})のブランチ".format(
    replace_server_repo_root_path))
subprocess.call("git rev-parse --abbrev-ref HEAD", shell=True)
print("")

# serverリポジトリのjsonを、dataリポジトリのjsonに置き換える
# --deleteオプションがあるので注意
subprocess.call(
    "rsync -av --delete {} {}".format(
        YUI_DATA_JSON_DIR,
        os.path.join(replace_server_repo_root_path, YUI_SERVER_JSON_FOR_ROOT)
    ),
    shell=True
)
