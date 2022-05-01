from flask_socketio import SocketIO

# ordinary flask configurations....
app = None
socketio = SocketIO(app)




########################

def templateCallback(methods=['GET', 'POST']):
    print('Template callback')

@socketio.on('my event')
def handle_my_template_event(json, methods=['GET', 'POST']):
    print('template event: ' + str(json))
    socketio.emit('template response', json, callback=templateCallback)

