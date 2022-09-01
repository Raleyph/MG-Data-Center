import sqlite3
import datetime as dt
import os
import re

import logs


def get_file(filename):
    c_time = dt.datetime.fromtimestamp(os.path.getctime(filename))
    c_date = c_time.strftime("%d/%m/%Y, %H:%M:%S")
    u_date = dt.datetime.now().date()

    f_path = os.path.abspath(filename)
    f_size = os.path.getsize(filename)
    
    desc = "Test dddescription of filedsd"
    backup = False
    favorite = False

    add_file(file_name=filename, file_path=f_path, creation_date=c_date, upload_date=u_date,
            size=f_size, description=desc, backup=backup, favorite=favorite)


# добавление сведений о файле в базу данных
def add_file(file_name, file_path, creation_date, upload_date, size, description, backup, favorite):
    conn.execute("INSERT INTO all_files(file_name, file_path, creation_date, upload_date, size, description, backup, favorite) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    (file_name, file_path, creation_date, upload_date, size, description, backup, favorite))
    conn.commit()


try:
    conn = sqlite3.connect('db/files.db', check_same_thread=False)
    cursor = conn.cursor()
except:
    logs.add_log("[SQL] Failed connection to db", "ERROR")

file_name = input("Enter file name: ")
get_file(file_name)

