import threading

from constants import *

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client_socket.send(send_length)
    client_socket.send(message)


def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except Exception as e:
            print(f"Error: {e}")
            break


def create_user():
    while True:
        username = input("Usuario: ")
        send(username)
        response = client_socket.recv(2048).decode(FORMAT)

        print(response)

        if response != USER_EXISTS:
            break


if __name__ == '__main__':
    create_user()

    thread = threading.Thread(target=receive_messages)
    thread.start()

    while True:
        msg_to_server = input("> ")
        send(msg_to_server)

        if msg_to_server == DISCONNECT_MSG:
            break
