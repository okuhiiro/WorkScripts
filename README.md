# はじめに
定型作業を簡略化するためのスクリプトパッケージです.
Macで動作することを前提としています.

# 初期設定
### Pythonバージョン
3.4.3で動作確認をしているため、ない場合はインストールします.

例) pycharmの場合

![pycharm](Images/pycharm_settings.png)

例) Macのpyenvの場合

このディレクトリ以下は3.4.3のPythonで動作する仮想環境などの設定をしてください.
```bash
$ pyenv local 3.4.3
```

### pip install一覧

### プロジェクトROOTをPYTHONPATHに追加し、ROOTからの絶対importを行えるようにします.
.bashrcや.zshrcに以下の記述を追加します.

```bash
WORK_DIR=~/work_scripts/
export PYTHONPATH=$WROK_DIR:$PYTHONPATH
```

### pecoの設定を行います.
.bashrc or .zshrcに下記設定を記述します.

```bash
function work () {
        local SELECT_SCRIPT=$(ls ${WORK_DIR}run/ | peco)
        python ${WORK_DIR}run/${SELECT_SCRIPT}
}
```

### 環境に合わせて各種パスを変更します.
各種constants.pyで宣言されているパスの変数値を環境に合わせて修正します.

# 使用方法 
### ランチャーで実行します. <sub id="permission">[注) 実行権限について](#permission)</sub>
run_launcher.commandを

- Finderでダブルクリック
- Spotlightで選択

### ターミナルから実行します.
```bash
$ work
```

の後、Enterキー

---

<a href="#permission" name="permission">実行権限について</a>
権限で実行できないエラーがでた場合は、付与してください.
