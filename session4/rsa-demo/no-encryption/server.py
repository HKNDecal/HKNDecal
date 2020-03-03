#!/usr/bin/env python3
# AJ THE SERVER

from helper import *

def intro():
    print("~~~~Welcome to Decal Chat~~~~")
    print("Logged in as: ", SERVER_NAME)

def server(host="localhost",port=59700,buf_size=BUFFER_SIZE):
    s = socket.socket()
    s.bind((host,port))
    s.listen()
    #print("Ready to receive at {0}:{1}".format(host,port))
    conn, addr = s.accept()
    print("Connected by: {0} at {1}".format(CLIENT_NAME,addr))

    # Server waits for client to talk

    while True:
        data = conn.recv(buf_size) #blocking
        if not data:
            print("[SERVER MSG]: Luke quit")
            conn, addr = s.accept()
        else:
            recvStr = data.decode()
            print('[{0}]: {1}'.format(CLIENT_NAME,recvStr))
            sendStr = input("Type a message to reply: ")
            conn.sendall(sendStr.encode())
    conn.close()

if __name__ == "__main__":
    intro()
    server()