import socket

HOST = socket.gethostbyname_ex(socket.gethostname())[2]
HOST = HOST[len(HOST)-1]

print()
print('========================================================')
print(' Selamat datang di aplikasi Quiz-Master oleh ZulNs')
print('========================================================')
print(f' Alamat untuk tampilan: "http://{HOST}/"')
print()
print(f' Alamat untuk juri:     "http://{HOST}/juri"')
print()
print(f' Alamat untuk Regu A:   "http://{HOST}/regu/a"')
print(f' Alamat untuk Regu B:   "http://{HOST}/regu/b"')
print(f' Alamat untuk Regu C:   "http://{HOST}/regu/c"')
print(f' Alamat untuk Regu D:   "http://{HOST}/regu/d"')
print('========================================================')
print()

import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room

SIO_PATH = '/socket.io'



app = Flask(__name__)
app.config['SECRET_KEY'] = 'ZulNs'
sio = SocketIO(app, path=SIO_PATH, cors_allowed_origins="*")
sio.init_app(app, async_mode="eventlet")

@app.route('/')
def route_index():
  return render_template("index.html")


@sio.on('connect')
def handle_connect():
  pass


  

@sio.on('disconnect')
def handle_disconnect():
  pass
@sio.on('join')
def handle_join():
  pass


@sio.on("sendMessage")
def handle_message(data):
  emit("broadcast", data, broadcast=True)


if __name__ == '__main__':
  sio.run(app, host=HOST, port=80, debug=False)
