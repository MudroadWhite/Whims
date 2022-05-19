# For learning purpose

import socket

# https://pythonprogramming.net/sockets-tutorial-python-3/
# https://www.ibm.com/docs/en/zos/2.4.0?topic=tcpip-basic-socket-calls
# https://www.youtube.com/watch?v=XXfdzwEsxFk

# TODO: make client also send server messages

def server():
    # 0. Set the configuration
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 1. `BIND` to a local port address
    # TODO: why get host name?
    s.bind((socket.gethostname(), 1234))
    # 3. Start LISTENing
    s.listen(5)

    while True:
        # 4. ACCEPT connection. Accept will wait until a `CONNECT` request has been received
        # The weird new socket seems to be part of the default specification of the ACCEPT method
        # On server's side, two sockets has bound to the same port
        # TODO: how many sockets can be bound to a port at server/client side? Unlimited?
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        # 5. Continuously send messages to client side
        clientsocket.send(bytes("Hey there!!!","utf-8"))
        clientsocket.close()


if __name__ == '__main__':
    server()