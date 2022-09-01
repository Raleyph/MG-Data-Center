import socket
import logs

IP = "127.0.0.1"
PORT = 2252

client = socket.socket()


# соединение хоста и сокета
def connection():
    try:
        client.bind((IP, PORT))
    except:
        logs.add_log("[CLIENT] Failed set host data", "CRITICAL")
        return 0


# отправка запроса на сервер
def send(message):
    client.send(message.encode("utf-8"))
    logs.add_log(f"[CLIENT] Send to server: {message}", "INFO")
