from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from threading import Lock


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"

thread = None
thread_lock = Lock()

socketio = SocketIO(app, cors_allowed_origins="*")

from websocket import background_thread

@app.route("/")
def main():
    context = {
        "data": "hello"
    }
    return render_template("counter.html", data=context)


@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
        emit('response', {
            "data": "connected",
            "count": 0
        })


if __name__ == '__main__':
    socketio.run(app, use_reloader=False, log_output=False)
