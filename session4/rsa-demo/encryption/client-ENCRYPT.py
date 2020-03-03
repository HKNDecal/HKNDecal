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


## Client [Cody] - RSA Encryption Demo

def intro():
    print("~~~~Welcome to Decal Chat v2 RSA ENCRYPTED~~~~")
    print("Logged in as: {0}\n".format(CLIENT_NAME))

def client(host="localhost",port=59720,buf_size=10240):
    priv,pub = key_loader(CLIENT_NAME)
    sock = socket.socket()
    sock.connect((host,port))
    while True:
        myInput = input("Enter a message to send or type 'q'/'Q' to escape: ")
        if myInput.upper() == "Q":
            sock.close()
            return
        msg = myInput.encode()
        ciphertext = pub.encrypt(msg,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        sock.sendall(ciphertext)
        data = sock.recv(buf_size)
        recvStr = priv.decrypt(data,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        recvStr = recvStr.decode()
        print('[{0}]: {1}'.format(SERVER_NAME,recvStr))

if __name__ == "__main__":
    intro()
    client()