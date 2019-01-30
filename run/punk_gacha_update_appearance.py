# -*- coding: utf-8 -*-
import os
import subprocess

from punk.constants import GSCN_APP_ROOT_PATH

"""
ガチャデータの作成
"""

GACHA_NAMES = [
    'g002_friendpoint',
    'g004_ticket',
    'g005_newbie',
    'g007_panel',
    'g012_friendpoint',
    'g024_charge',
    'g025_breakthrough',
    'g031_allunittype',
    'g037_breakthrough',
    'g038_breakthrough',
    'g039_breakthrough',
    'g040_breakthrough',
    'g041_breakthrough',
    'g042_breakthrough',
    'g043_breakthrough',
    'g044_breakthrough',
    'g045_breakthrough',
    'g046_breakthrough',
    'g047_breakthrough',
    'g048_breakthrough',
    'g049_breakthrough',
    'g050_breakthrough',
    'g051_breakthrough',
    'g052_breakthrough',
    'g053_allunittype',
    'g054_allunittype',
    'g101_retry_gift',
]

os.chdir(GSCN_APP_ROOT_PATH)
for gacha_name in GACHA_NAMES:
    subprocess.call("python manage.py {}_update_appearance --settings=settings.develop.local".format(gacha_name), shell=True)

