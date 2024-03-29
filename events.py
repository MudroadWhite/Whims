from flask_socketio import SocketIO
from app import socketio

def connect_callback(data):
    print('Template callback')

@socketio.on('connect')
def handle_connect(json):
    print('template event: ' + str(json))
    socketio.emit('template response', json, callback=connect_callback)
    # pass


def send_chat_callback(data):
    print('Template callback')


@socketio.on('send chat')
def handle_send_chat(json):
    print('template event: ' + str(json))
    socketio.emit('template response', json, callback=send_chat_callback)


def response_chat_callback():
    print('Template callback')


@socketio.on('response chat')
def handle_response_chat(json):
    print('template event: ' + str(json))
    socketio.emit('template response', json, callback=response_chat_callback)


########################

@socketio.on('test')
def test_handle(data):
    print("Received test socket event! Data:{s}".format(s=data))

def templateCallback(json):
    print('Template callback')

@socketio.on('my event')
def handle_my_template_event(json):
    print('template event: ' + str(json))
    socketio.emit('template response', json, callback=templateCallback)