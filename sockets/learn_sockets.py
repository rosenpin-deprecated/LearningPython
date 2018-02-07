from socket import *
import os
import atexit

s = socket(AF_INET, SOCK_STREAM)

s.bind(("0.0.0.0", 80))
s.listen(5)

atexit.register(lambda: s.close())
try:
    while True:
        (connection, addr) = s.accept()
        print("connected to ", addr)
        command = str(connection.recv(1000)).split(" ")
        if command[0] != "GET":
            connection.sendall("Only GET pls :)")
            connection.close()
        else:
            path = os.getcwd() + command[1].split("\\")[0]
            print("file to open %s" % path)
            if os.path.isfile(path):
                f = open(path).read()
                response = "HTTP/1.0 200 Document Follows\n" + "Content-length:" + str(len(f)) + "\n\n" + f

            else:
                response = "HTTP/1.0 404 Not Found\r\n"

            connection.sendall(response)
        connection.close()
except Exception as e:
    s.close()
