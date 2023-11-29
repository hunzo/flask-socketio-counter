from main import socketio
from time import sleep
from threading import Lock

from flask_socketio import SocketIO, emit

thread = None
thread_lock = Lock()

def background_thread():
    count = 0
    while True:
        sleep(1/1000)
        count += 1
        socketio.emit('response', {
            "data": count
        })
