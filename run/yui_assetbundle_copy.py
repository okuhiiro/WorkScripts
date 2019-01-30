# -*- coding: utf-8 -*-
"""
resoucesリポジトリの.assetbundleをclientにcopyする
"""
import os
import re
import subprocess
from common.dir_file_manager import select_dir
import shutil
from yui.constants import (
    YUI_ROOT,
    YUI_RESOURCES_ASSETBUNDLE_FOR_ROOT,
    YUI_CLIENT_RESOUCES_FOR_ROOT,
    YUI_CLIENT_RESOUCES_DATA_FOR_ROOT
)

print("copy元のresourcesを選択してください")
copy_original_resources_dir = select_dir(YUI_ROOT, re.compile(r'.*resources.*'))

print("")

print("copy先のclientを選択してください")
copy_send_client_dir = select_dir(YUI_ROOT, re.compile(r'.*client.*'))

print("")

print("{}はiosですか? androidですか?".format(copy_send_client_dir))
print("0) ios")
print("1) android")
num = int(input("番号で指定してください > "))
if num == 0:
    platform = "ios/"
elif num == 1:
    platform = "android/"
else:
    raise ValueError("想定していないPlatformです")

print("resourcesリポジトリの.assetbudleを、clientリポジトリにcopyします\n")

copy_original = os.path.join(YUI_ROOT, copy_original_resources_dir, YUI_RESOURCES_ASSETBUNDLE_FOR_ROOT, platform)
print("コピー元は {} です".format(copy_original))

copy_send = os.path.join(YUI_ROOT, copy_send_client_dir, YUI_CLIENT_RESOUCES_DATA_FOR_ROOT)
print("コピー先は {} です".format(copy_send))

# --deleteオプションがあるので注意
os.chdir(copy_original)
subprocess.call(
    "rsync -av --exclude={} --exclude={} --exclude={} --delete {} {}".format(
        "*.meta",
        "*.csv",
        "*.sha1list",
        copy_original,
        copy_send
    ),
    shell=True
)

shutil.copyfile(
    "vesionfile.csv",
    os.path.join(
        YUI_ROOT,
        copy_send_client_dir,
        YUI_CLIENT_RESOUCES_FOR_ROOT,
        "ResFileVersionInfo.csv"
    )
)
shutil.copyfile(
    "vesionfile.csv",
    os.path.join(
        YUI_ROOT,
        copy_send_client_dir,
        YUI_CLIENT_RESOUCES_FOR_ROOT,
        "ResFileVersionInfoNew.csv"
    )
)
