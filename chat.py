from flask_socketio import SocketIO
from main import app

socketio = SocketIO(app)

def connect_callback(methods=['GET', 'POST']):
    print('Template callback')


@socketio.on('connect')
def handle_connect(json, methods=['GET', 'POST']):
    print('template event: ' + str(json))
    socketio.emit('template response', json, callback=connect_callback)


def send_chat_callback(methods=['GET', 'POST']):
    print('Template callback')


@socketio.on('send chat')
def handle_send_chat(json, methods=['GET', 'POST']):
    print('template event: ' + str(json))
    socketio.emit('template response', json, callback=send_chat_callback)


def response_chat_callback(methods=['GET', 'POST']):
    print('Template callback')


@socketio.on('response chat')
def handle_response_chat(json, methods=['GET', 'POST']):
    print('template event: ' + str(json))
    socketio.emit('template response', json, callback=response_chat_callback)


########################

def templateCallback(methods=['GET', 'POST']):
    print('Template callback')


@socketio.on('my event')
def handle_my_template_event(json, methods=['GET', 'POST']):
    print('template event: ' + str(json))
    socketio.emit('template response', json, callback=templateCallback)

