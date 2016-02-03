# -*- coding: utf-8 -*-
from os import path

HOME = path.expanduser("~")

# 使用Unity
YUI_UNITY_PATH = "/Applications/Unity4.6.8/Unity.app/Contents/MacOS/Unity"

# YUIプロジェクトのROOT
YUI_ROOT = path.join(HOME, "yui/")

# dataリポジトリ
# dataリポジトリのフォルダは1つ想定
# リポジトリROOT
YUI_DATA_REPO_ROOT_DIR = path.join(HOME, "yui/data/")
# dataリポジトリjsonフォルダのパス
YUI_DATA_JSON_DIR = path.join(YUI_DATA_REPO_ROOT_DIR, "server/json/")
YUI_DATA_CSV_DIR = path.join(YUI_DATA_REPO_ROOT_DIR, "server/csv/")

# serverリポジトリ
# serverリポジトリのフォルダは複数想定
# Rootからのjsonフォルダへのパス
YUI_SERVER_JSON_FOR_ROOT = "application/data/json/"

# resourcesリポジトリ
# resourcesリポジトリのフォルダは複数想定
# Rootからのcsvフォルダへのパス
YUI_RESOURCES_CSV_FOR_ROOT = "yui/Assets/Resources/csv/"
YUI_RESOURCES_ASSETBUNDLE_FOR_ROOT = "yui/Assets/assetbundle/"

# clientリポジトリ
# clientリポジトリのフォルダは複数想定
# RootからのResoucesフォルダ
YUI_CLIENT_RESOUCES_FOR_ROOT = "yui/Assets/Resources/"
YUI_CLIENT_RESOUCES_DATA_FOR_ROOT = "yui/Assets/Resources/Data/"



