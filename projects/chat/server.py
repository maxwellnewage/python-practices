import threading
from constants import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

users_connected = []
connections = []
lock = threading.Lock()


def user_exists(user):
    with lock:
        return user in users_connected


def broadcast_message(message, sender_conn):
    with lock:
        for conn in connections:
            if conn != sender_conn:
                try:
                    conn.send(message.encode(FORMAT))
                except:
                    connections.remove(conn)


def client_message(conn):
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        return msg
    return None


def auth_user(conn, addr):
    username = None
    authenticated = False

    while not authenticated:
        username = client_message(conn)
        if username:
            if user_exists(username):
                conn.send(USER_EXISTS.encode(FORMAT))
            else:
                with lock:
                    users_connected.append(username)
                    connections.append(conn)
                conn.send(f"Welcome @{username}!".encode(FORMAT))
                print(f"[NEW USER] {username} has joined from {addr}")
                authenticated = True

    return username


def handle_client(conn, addr):
    username = auth_user(conn, addr)

    connected = True
    while connected:
        msg = client_message(conn)

        if msg:
            if msg == DISCONNECT_MSG:
                with lock:
                    users_connected.remove(username)
                    connections.remove(conn)
                conn.send(f"@{username} left the chat.".encode(FORMAT))
                print(f"@{username} left the chat.")
                connected = False
            else:
                msg_formatted = f"@{username}: {msg}"
                print(msg_formatted)
                broadcast_message(msg_formatted, conn)

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == '__main__':
    print("[STARTING] server is starting")
    start()
