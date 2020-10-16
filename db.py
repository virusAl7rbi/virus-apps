import sqlite3


def insert():
	conn = sqlite3.connect('insta.db')
	cursor = conn.cursor()

	name_app = input('app name => ')
	code_app = input('code app => ')
	android_url = input('android url app => ')
	ios_url = input('ios url app => ')

	values = (name_app, name_app, android_url, ios_url)
	print(values)
	data = """
	INSERT INTO Insta VALUES ('{code}','{name}','{android}','{ios}');
	""".format(code=code_app, name=name_app, android=android_url, ios=ios_url)
	cursor.execute(data)
	conn.commit()


insert()
