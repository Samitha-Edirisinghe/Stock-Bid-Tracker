import socket
import threading

class ServerSubHandler(threading.Thread):
    def __init__(self, main, soc):
        self.main = main
        self.soc = soc
        super().__init__()

    def run(self):
        print("Connection start")

    def subscriber(self, message):
        out = None
        try:
            out = self.soc.makefile(mode="w")
            out.write(message)
            print(f"notification {message}")
            out.flush()
        except IOError:
            print(f"Cannot send messages [{message}]")
        finally:
            if out:
                out.close()
