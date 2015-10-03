# -*- coding: utf-8 -*-
"""
resourcesリポジトリのcsvを、resourcesリポジトリのcsvに置き換える
"""
import os
import subprocess
import re
from yui.constants import (
    YUI_ROOT,
    YUI_DATA_REPO_ROOT_DIR,
    YUI_DATA_CSV_DIR,
    YUI_RESOURCES_CSV_FOR_ROOT
)
from common.dir_manager import select_dir

# コピー先のパスを取得
# リソースのリポジトリはresourcesという文字列を含むフォルダである必要がある
copy_out = select_dir(YUI_ROOT, re.compile(r'.*resources.*'))

print("resourcesリポジトリのcsvを、dataリポジトリのcsvに置き換えます\n")

os.chdir(YUI_DATA_CSV_DIR)
print("現在のdataリポジトリ({})のブランチ".format(YUI_DATA_REPO_ROOT_DIR))
subprocess.call("git rev-parse --abbrev-ref HEAD", shell=True)
print("↓")

replace_resources_repo_root_path = os.path.join(YUI_ROOT, copy_out)
os.chdir(replace_resources_repo_root_path)
print(
    "現在のresourcesリポジトリ({})のブランチ".format(
    replace_resources_repo_root_path))
subprocess.call("git rev-parse --abbrev-ref HEAD", shell=True)
print("")

# resourcesリポジトリのcsvを、resourcesリポジトリのcsvに置き換える
# csvもdataリポジトリで管理していないもの(effect系のcsv)もあるので
# deleteオプションはつけない
subprocess.call(
    "rsync -av {} {}".format(
        YUI_DATA_CSV_DIR,
        os.path.join(replace_resources_repo_root_path,
                     YUI_RESOURCES_CSV_FOR_ROOT)
    ),
    shell=True
)
