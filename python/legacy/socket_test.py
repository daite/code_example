#!/usr/bin/env python

import socket
HOST = 'www.mayuyuidfc.com'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
resource = '/wp-content/uploads/2014/04/image.jpg'
send_msg = 'GET %s HTTP/1.0\r\nHost: %s\r\n\r\n' %(resource, HOST)
print 'Sending...\n%s' %send_msg
s.sendall(send_msg)

received_data = ""
while True:
	data = s.recv(8192)
	if not data:
		print "Done"
		break
	received_data += data

with open('a.jpg', 'wb') as f:
	f.write(received_data.split('\r\n\r\n')[-1])

s.close()
