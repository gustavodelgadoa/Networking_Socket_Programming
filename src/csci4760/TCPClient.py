from socket import *

serverName = 'localHost'
serverPort = 5001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

integer_string = input('Please enter a number x where 1 < x < 100: ')
sentence = input('Client of Gustavo Delgado' + integer_string)

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()