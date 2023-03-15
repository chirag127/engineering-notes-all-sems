### Process-to-process delivery in transport layer

The transport layer is responsible for providing process-to-process delivery of data between applications running on different hosts. This is achieved through the use of transport layer protocols such as TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

Here is an example of how process-to-process delivery works in the transport layer using the TCP protocol:

```python
# Client-side code
from socket import socket, AF_INET, SOCK_STREAM

serverName = 'hostname'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())

clientSocket.close()
```

```python
# Server-side code
from socket import socket, AF_INET, SOCK_STREAM

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
```

In this example, the client-side code creates a TCP socket and connects to the server using the server's hostname and port number. The client then sends a sentence to the server, which is received and processed by the server-side code. The server capitalizes the sentence and sends it back to the client, where it is received and printed. This is an example of process-to-process delivery, where data is sent from one process (the client) to another process (the server) using the transport layer.