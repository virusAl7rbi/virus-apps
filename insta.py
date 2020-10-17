from flask import request, jsonify, Flask
import sqlite3
import socket

conn = sqlite3.connect('insta.db', check_same_thread=False)
cursor = conn.cursor()

app = Flask(__name__)

def ipv4():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ipv4 = s.getsockname()[0]
	s.close()
	return ipv4


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


@app.route('/Add', methods=["POST"])
def AddToDB():
	appid = request.args.get('id')
	name = request.args.get('name')
	androurl = request.args.get('androurl')
	iosurl = request.args.get('iosurl')
	data = """
	INSERT INTO Insta VALUES ('{code}','{name}','{android}','{ios}');
	""".format(code=appid, name=name, android=androurl, ios=iosurl)
	cursor.execute(data)
	conn.commit()
	return jsonify(success=True)


if __name__ == '__main__':
	app.run(port=80) 
