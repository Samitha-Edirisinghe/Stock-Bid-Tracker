def receiver(self, rec):
    while True:
        print("I.........................")
        ins = rec.makefile("rb")
        str = None
        while True:
            str = ins.readline()
            if str is None:
                print("Null Input. Please send a valid message")
                continue
            print("Notification from server: " + str)
            break
