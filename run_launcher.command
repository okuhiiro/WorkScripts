#!/bin/sh

# エラーが発生した時点で処理終了
set -e

# このスクリプトの実行ディレクトリに移動
cd `dirname $0`

# .zshrcの関数を呼ぶ方法でもよい
# `work`

SELECT_SCRIPT=$(ls ./run/ | peco)
python ./run/${SELECT_SCRIPT}

# ターミナルを終了
# killall Terminal
