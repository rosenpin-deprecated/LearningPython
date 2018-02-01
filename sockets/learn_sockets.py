from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('smtp.gmail.com', 587))
s.send('HELO smtp.gmail.com\n\n')
print s.recv(10000)
s.send('STARTTLS')
print s.recv(10000)
s.send('')
