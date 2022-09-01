import config
import sqlite3

conn = sqlite3.connect('db/bot.db', check_same_thread=False)
cursor = conn.cursor()


def user_check(user_id: int):
	register = None

	cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
	rows = cursor.fetchall()

	if rows:
		register = True
	else:
		register = False

	return register


def user_login(user_id: int, user_name: str, username: str, status: str):
	cursor.execute('INSERT INTO users (user_id, user_name, username, status) VALUES (?, ?, ?, ?)', (user_id, user_name, username, status))
	conn.commit()


def user_delete(user_id: int):
	cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
	conn.commit()

