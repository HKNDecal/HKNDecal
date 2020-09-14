This is a very simple messaging app between two people AJ (Server) and Cody (Client).
In the folder "no-encryption" all messages are sent as plaintext. If you have an eavesdropper inspect the packets on wireshark, you'll see all the messages!

If you take a look at the "encryption" folder, there is a folder for the public-keys (which are available for everyone) and a folder for the private keys (each person can only see their key). If you run the server and then the client, you'll notice the messages are still being sent as before but the eavesdropper in wireshark can't see anything!





PRE-REQUISTIES:
-python3
    modules:
        -cryptography (2.4.2>=)
-wireshark (installed & run with enough permission to view network traffic at the loopback address)



HOW-TO RUN:
1. chmod +x server.py (or server-ENCRYPT.py)
2. chmod +x client.py (or client-ENCRYPT.py)
    2a: If you can't do either of the above you'll need to run the code with python directly (ex: "python3 server.py")
3. Run the server.py first AND THEN run client.py
4. Open Wireshark, start listening on the loopback address. I also recommend filtering tcp only (maybe even port based if you have a lot of misc packets captured).
5. Now have the client send a message (keep it a bit brief, there's an allocated buffer size for the message in the code, if it goes beyond this you'll have undefined behavior).
6. Have the server reply and chat for a bit (ex: have AJ ask Cody for his password, have Cody ask AJ what his credit card number is, etc...)
7. On wireshark, take a look at the messages sent and if it's encrypted you should see a large blob of nothing for the data portion of the packet and if it is not you'll see the plaintext message exactly sent.


If you have issues email/slack adithyaj@
