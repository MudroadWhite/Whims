from flask_socketio import SocketIO
from app import socketio

print("events imported")

@socketio.on('test socket event')
def test_callback(methods=['GET', 'POST']):
    print("Received test socket event! From different file")

def connect_callback(methods=['GET', 'POST']):
    print('Template callback')

@socketio.on('connect')
def handle_connect(methods=['GET', 'POST']):
    # print('template event: ' + str(json))
    # socketio.emit('template response', json, callback=connect_callback)
    pass


def send_chat_callback(methods=['GET', 'POST']):
    print('Template callback')


@socketio.on('send chat')
def handle_send_chat(methods=['GET', 'POST']):
    # print('template event: ' + str(json))
    # socketio.emit('template response', json, callback=send_chat_callback)
    pass


def response_chat_callback(methods=['GET', 'POST']):
    print('Template callback')


@socketio.on('response chat')
def handle_response_chat(methods=['GET', 'POST']):
    # print('template event: ' + str(json))
    # socketio.emit('template response', json, callback=response_chat_callback)
    pass


########################

def templateCallback(methods=['GET', 'POST']):
    print('Template callback')


@socketio.on('my event')
def handle_my_template_event(methods=['GET', 'POST']):
    # print('template event: ' + str(json))
    # socketio.emit('template response', json, callback=templateCallback)
    pass

