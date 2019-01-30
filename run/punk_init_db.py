# -*- coding: utf-8 -*-
import os
import subprocess
import mysql.connector
from punk.constants import GSCN_APP_ROOT_PATH
from common.dir_file_manager import delete_pyc

"""
Windowsではinit_dbができないのため
それを行うための代替プログラム
"""

print("--- Start delete_pyc ---")
delete_pyc(GSCN_APP_ROOT_PATH)
print("--- End delete_pyc ---")

print("")

conn = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = ''
)
if(conn.is_connected() == False):
    print("Failed MySQL Connected!!")
    exit()
cursor = conn.cursor()

print("--- Start Drop DataBases ---")
cursor.execute("DROP DATABASE IF EXISTS punk")
cursor.execute("DROP DATABASE IF EXISTS punk_gamelog")
cursor.execute("DROP DATABASE IF EXISTS punk_analytics")
cursor.execute("DROP DATABASE IF EXISTS punk_multiplay")
cursor.execute("DROP DATABASE IF EXISTS punk_guild")
cursor.execute("DROP DATABASE IF EXISTS punk_shard0")
cursor.execute("DROP DATABASE IF EXISTS punk_shard1")
cursor.execute("DROP DATABASE IF EXISTS punk_guild_shard0")
cursor.execute("DROP DATABASE IF EXISTS punk_guild_shard1")
print("--- End Drop DataBases ---")

print("")

print("--- Start Create DataBases ---")
cursor.execute("CREATE DATABASE punk DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
cursor.execute("CREATE DATABASE punk_gamelog DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
cursor.execute("CREATE DATABASE punk_analytics DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
cursor.execute("CREATE DATABASE punk_multiplay DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
cursor.execute("CREATE DATABASE punk_guild DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
cursor.execute("CREATE DATABASE punk_shard0 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
cursor.execute("CREATE DATABASE punk_shard1 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
cursor.execute("CREATE DATABASE punk_guild_shard0 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
cursor.execute("CREATE DATABASE punk_guild_shard1 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci")
print("--- End Create DataBases ---")

print("")

print("--- Start Redis Flush")
subprocess.call("redis-cli -p 6379 -h localhost flushdb", shell=True)
print("--- End Redis Flush")

print("")

print("--- Start syncdb ---")
os.chdir(GSCN_APP_ROOT_PATH)
subprocess.call("python manage.py syncdb --noinput --database=default --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py syncdb --noinput --database=gsc_gamelog --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py syncdb --noinput --database=gsc_analytics --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py syncdb --noinput --database=multiplay --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py syncdb --noinput --database=gsc_guild_common --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py syncdb --noinput --database=gsc_shard0 --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py syncdb --noinput --database=gsc_shard1 --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py syncdb --noinput --database=gsc_guild_shard0 --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py syncdb --noinput --database=gsc_guild_shard1 --settings=settings.develop.local", shell=True)
print("--- End syncdb ---")

print("--- Start gmigrate ---")
subprocess.call("python manage.py gmigrate --database=default --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py gmigrate --database=gsc_gamelog --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py gmigrate --database=gsc_analytics --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py gmigrate --database=multiplay --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py gmigrate --database=gsc_guild_common --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py gmigrate --database=gsc_shard0 --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py gmigrate --database=gsc_shard1 --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py gmigrate --database=gsc_guild_shard0 --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py gmigrate --database=gsc_guild_shard1 --settings=settings.develop.local", shell=True)
print("--- End gmigrate ---")

print("")

# print("--- Start gdio init ---")
# print("--- End gdio init ---")

print("--- Start Other ---")
subprocess.call("python manage.py loaddata submodule/event_type/event_type.json --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py clean_cache --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py createadminuser --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py battle_item_drop_update_appearance --settings=settings.develop.local", shell=True)
subprocess.call("python manage.py slot_update_appearance --settings=settings.develop.local", shell=True)
print("--- End Other ---")
