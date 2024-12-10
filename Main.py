import socket
from threading import Thread


class Main(Thread):
    def __init__(self):
        self.arr = []
        super().__init__()

    def run(self):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('0.0.0.0', 2023))
            server_socket.listen()

            while True:
                client, address = server_socket.accept()
                print(f"New client connected {address[0]}")
                server_sub_handler = ServerSubHandler(self, client)
                self.arr.append(server_sub_handler)
                server_sub_handler.start()
        except Exception as e:
            print(e)

    def return_list(self):
        return self.arr
