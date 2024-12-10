import socket
from threading import Thread


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('0.0.0.0', 2021))
        self.server.listen()

        print("Server is waiting for client request")

        mai = Main()
        mai.start()

        while True:
            client, address = self.server.accept()
            print(f"New client connected {address[0]}")
            client_handler = ClientHandler(client)
            Thread(target=client_handler.run).start()


def send_notification(handler, msg):
    for serv in handler:
        print("subssss")
        serv.subscriber(msg)


class ClientHandler:
    def __init__(self, client):
        self.client = client

    def run(self, mai=None):
        out = None
        in_ = None
        try:
            out = self.client.makefile('w')
            in_ = self.client.makefile('r')
            line = in_.readline()
            while line:
                print(f"Sent from the client: {line}")
                out.write(line)
                out.flush()

                sarray = mai.return_list()
                send_notification(sarray, f"This is sever notification: {line}")
                line = in_.readline()
        except Exception as e:
            print(e)
        finally:
            if out:
                out.close()
            if in_:
                in_.close()
            self.client.close()


class Main:
    def __init__(self):
        self.sarray = []

    def start(self):
        pass

    def return_list(self):
        return self.sarray


Server()
