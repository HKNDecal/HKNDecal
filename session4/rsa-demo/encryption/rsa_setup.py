import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


SERVER_NAME = "AJ"
CLIENT_NAME = "Cody"


#def generate_and_store_key(pathForPrivate,pathForPublic,storeEncrypted=True):
#key = rsa.generate_private_key(public_exponent=65537,key_size=2048,backend=default_backend())
#pub = key.public_key()
#pubKey =  pub.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)


def key_loader(username):
    if username.upper() == SERVER_NAME:
        PRIV_PATH = "./private-keys/aj-priv/rsa_priv" 
        PUB_PATH = "./public-keys/cody-pub" 
    else:
        PRIV_PATH = "./private-keys/cody-priv/rsa_priv" 
        PUB_PATH = "./public-keys/aj-pub"  
    
    with open(PRIV_PATH,"rb") as key_file:
        key = serialization.load_pem_private_key(key_file.read(),password=b'mypassword',backend=default_backend())
    with open(PUB_PATH, "rb") as pub_file:
        pub = serialization.load_pem_public_key(pub_file.read(),backend=default_backend())

        
    return (key,pub)
