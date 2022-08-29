import sqlite3

conn = sqlite3.connect('db/bot.db', check_same_thread=False)
cursor = conn.cursor()


def upload_file(name: str, path: str, u_date: str, descript: str, backup: str):
	try:
		cursor.execute('INSERT INTO upload_files (file_name, file_path, upload_date, description, backup) VALUES (?, ?, ?, ?, ?)',
					(name, path, u_date, descript, backup))
		conn.commit()
	except:
		print('error')

