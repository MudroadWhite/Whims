# For learning purpose

import socket

# TODO: make client also send server messages

def client():
    # 0. Socket settings
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 1. `CONNECT` to some remote addr and port
    s.connect((socket.gethostname(), 1234))
    # 2. Wait for server to accept the connection

    while True:
        full_msg = ''
        while True:
            # 3. Make a buffer of 1024. Received messages will be stored in the buffer
            # TODO: is that a locked operation?
            msg = s.recv(8)
            if len(msg) <= 0:
                break
            full_msg += msg.decode("utf-8")

        if len(full_msg) > 0:
            print(full_msg)


if __name__ == '__main__':
    client()