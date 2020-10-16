from flask import request
from flask import Flask
import sqlite3
import socket

conn = sqlite3.connect('insta.db', check_same_thread=False)
cursor = conn.cursor()

app = Flask(__name__)


@app.route('/Apps', methods=['GET'])
def start():
	appid = request.args.get('id')
	os = request.headers.get('User-Agent')
	if "Android" in os:
		googlePlay = 'SELECT AndroidUrl FROM Insta WHERE AppID={}'.format(str(appid))
		url = cursor.execute(googlePlay).fetchone()[0]
		return f"<script>window.open('{url}','_self');</script>"
	if "IPhone" or "IPad" in os:
		url = cursor.execute('SELECT IosUrl FROM Insta WHERE AppID={}'.format(str(appid)))
		return f"<script>window.open('{url}','_self');</script>"


if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	local_ip = str(s.getsockname()[0])
	app.run(host=local_ip, port=80)
