 Here is the content in markdown format for the topic ### TCP/IP Client Sockets for the notes of the Unit 3 - Scripting in the subject of Web Technology:

### TCP/IP Client Sockets

- TCP/IP Client Sockets are a way for a client application to connect to a server application.
- A client socket initiates communication with a server socket which listens for incoming client connections.
- Once a connection is established, data can be sent and received through the sockets.
- The sockets utilize the TCP protocol to provide reliable, ordered, and error-checked delivery of transmitted data.

Advantages:
- Reliable data transmission with error checking and correction.
- Ordered data delivery. Data is received in the same order it was sent.
- congestion controlled to avoid overwhelming networks.

Disadvantages:
- Slower than UDP due to the additional overhead.
- Some latency as packets may be buffered and retransmitted if needed.

Example Code (Python):
```python
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
sock.connect(server_address)

try:
    # Send data
    message = b'This is the message.  It will be repeated.'
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('Received: ', data)

finally:
    print('closing socket')
    sock.close()
```

Applications:
- Web browsing (HTTP)
- Email (SMTP, POP3, IMAP)
- Remote login (SSH)
- File transfer (FTP)
- Streaming media
- Real-time communications (VoIP)

I hope this helps! Let me know if you would like me to elaborate on any of the points or add more details.