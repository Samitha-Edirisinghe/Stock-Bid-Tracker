import socket
import threading
import csv


class ClientThread(threading.Thread):
    def run(self):
        pass  # add code here


def set_login():
    pass  # add code here


def read_record(search_term, filepath):
    found = False
    symbol: str = ""
    price = ""
    with open(filepath, "r") as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            symbol = row[0]
            price = row[1]
            if symbol == search_term:
                found = True
                break
    if found:
        print("Base Price:", price)
    else:
        print("-1")


host = "localhost"
port = 2021
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    out = sock.makefile("w")
    inp = sock.makefile("r")
    client_thread = ClientThread()
    client_thread.start()
    username = input("Username:")
    password = input("Password:")
    set_login()
    print("You are logged in")
    search_term = input("Enter symbol:")
    filepath = "D:\\stocks.csv"
    read_record(search_term, filepath)
    line = ""
    while True:
        line = input("Enter bid:")
        out.write(line + "\n")
        out.flush()
        print(username, "Bid")
