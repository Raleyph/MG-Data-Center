from threading import Thread
import socket
import threading
import logs

IP = "127.0.0.1"
PORT = 2252


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientSocket) :
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        logs.add_log(f"[SERVER] New connetction to server: {clientAddress}", "INFO")


    def run(self):
        logs.add_log(f"[SERVER] Client connection: {clientAddress}", "INFO")

        message = ""
        while True:
            data = self.csocket.recv(4096)
            message = data.decode()
            logs.add_log(f"[SERVER] Client send to server: {message}", "INFO")

            if message == "":
                break


server = socket.socket()
server.bind((IP, PORT))
server.listen()

while True:
    clientSocket, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientSocket)
    newthread.start()

