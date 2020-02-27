#Author: Montana Esguerra
#Date: 2/24/2020
#Filename: smtp1.py
#Description: Simple SMTP server

from socket import *

from pip._vendor.distlib.compat import raw_input

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.nyu.edu"# Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
# Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO mje349\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFromCommand = 'MAIL FROM: mje349@nyu.edu\r\n'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')

# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptCommand = 'RCPT TO: mje349@nyu.edu\r\n'
clientSocket.send(rcptCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start

#Custom Email Message
message = raw_input("Enter your message: ")
clientSocket.send(message.encode())
#End of Custom Message

#clientSocket.send(msg.encode())

# Fill in end

# Message ends with a single period.
# Fill in start
#period = '\r\n.\r\n'
clientSocket.send(endmsg.encode())
#Print Custom message
#print('Message: \"' + message + "\" sent")
print('Message: ' + msg + ' sent!')

recv6 = clientSocket.recv(1024).decode()
print(recv6)

if recv6[:3] != '250':
    print('250 reply not received from server')

# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '221':
    print('221 reply not received from server.')
# Fill in end