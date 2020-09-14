#!/usr/bin/env python3
# Cody the Client

from helper import *


def intro():
    print("~~~~Welcome to Decal Chat~~~~")
    print("Logged in as: ", CLIENT_NAME)

def client(host="localhost",port=59700,buf_size=10240):
    s = socket.socket()
    s.connect((host,port))
    while True:
        myInput = input("Enter a message to send or type 'q'/'Q' to escape: ")
        if myInput.upper() == "Q":
            s.close()
            return
        s.sendall(myInput.encode())
        data = s.recv(buf_size)
        print("[{0}] said: {1}".format(SERVER_NAME,data.decode()))


if __name__ == "__main__":
    intro()
    client()