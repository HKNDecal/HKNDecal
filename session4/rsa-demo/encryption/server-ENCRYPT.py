#!/usr/bin/env python3

import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from rsa_setup import key_loader
from rsa_setup import CLIENT_NAME
from rsa_setup import SERVER_NAME

# Server [AJ] - RSA Encryption Demo

def intro():
    print("~~~~Welcome to Decal Chat v2 RSA ENCRYPTED~~~~")
    print("Logged in as: {0}\n".format(SERVER_NAME))


def server(host="localhost",port=59720,buf_size=10240):
    priv,pub = key_loader(SERVER_NAME)
    sock = socket.socket()
    sock.bind((host,port))
    sock.listen()
    print("Ready to receive at {0}:{1}".format(host,port))
    conn, addr = sock.accept()
    print("Connected by: {0}".format(addr))
    while True:
        data = conn.recv(buf_size)
        if not data:
            print("[SERVER LOG]: Host quit")
            conn, addr = sock.accept()
        else:
            recvStr = priv.decrypt(data,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
            recvStr = recvStr.decode()
            print('[{0}]: {1}'.format(CLIENT_NAME,recvStr))
            sendStr = input("Type a message to reply: ")
            sendThis = pub.encrypt(sendStr.encode(),padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
            conn.sendall(sendThis)

if __name__ == "__main__":
    intro()
    server()