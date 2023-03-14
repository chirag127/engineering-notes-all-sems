#### TCP Transport layer protocol

TCP (Transmission Control Protocol) is one of the most commonly used transport layer protocols in computer networks. It is a connection-oriented protocol that provides a reliable, ordered, and error-checked data delivery service to applications.

##### Features of TCP

- **Connection-oriented:** TCP establishes a connection between two endpoints (sender and receiver) before transmitting any data. This connection is a virtual circuit that guarantees reliable delivery of data.
- **Reliable:** TCP ensures that all data is delivered to the receiver without any loss or corruption. It uses sequence numbers and acknowledgments to ensure that all packets are received and in the correct order.
- **Ordered:** TCP ensures that all data is received by the receiver in the same order that it was sent by the sender.
- **Error-checked:** TCP uses checksums to detect any errors in the data that is transmitted.
- **Flow control:** TCP uses a sliding window mechanism to control the flow of data between sender and receiver. This ensures that the sender does not overwhelm the receiver with too much data.
- **Congestion control:** TCP uses a variety of techniques to avoid congestion in the network. These techniques include slow start, congestion avoidance, and fast retransmit.

##### Mnemonics and Learning Tricks

- **TCP is like a postal service:** Just like how a postal service ensures that a package is delivered reliably, ordered, and error-checked, TCP ensures that data is delivered reliably, ordered, and error-checked.
- **TCP uses a virtual circuit:** Think of TCP as building a virtual circuit between two endpoints before transmitting any data. This ensures that data is transmitted reliably and in the correct order.

##### Advantages of TCP

- Provides reliable, ordered, and error-checked data delivery service to applications.
- Ensures that all data is received by the receiver in the same order that it was sent by the sender.
- Uses flow control and congestion control mechanisms to avoid network congestion.
- Can be used for a wide range of applications, such as web browsing, email, file transfer, and real-time multimedia streaming.

##### Disadvantages of TCP

- Slower than UDP due to the overhead associated with establishing connections and ensuring reliability.
- May not be suitable for real-time applications that require low latency, such as online gaming or video conferencing.

##### Applications

- Web browsing
- Email
- File transfer
- Real-time multimedia streaming

##### Example Code

```python
import socket

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to a server
server_address = ('localhost', 8000)
sock.connect(server_address)

# send data
message = 'Hello, world!'
sock.sendall(message.encode())

# receive data
data = sock.recv(1024)
print(data.decode())

# close the connection
sock.close()
```

In this example, a TCP socket is created and used to connect to a server. Data is sent using the `sendall()` method and received using the `recv()` method. The connection is closed using the `close()` method.