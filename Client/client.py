import socket
import logs

IP = "127.0.0.1"
PORT = 2252

client = socket.socket()
client.bind((IP, PORT))


def send(message):
    client.send(message.encode("utf-8"))
    logs.add_log(f"[CLIENT] Send to server: {message}", "INFO")
