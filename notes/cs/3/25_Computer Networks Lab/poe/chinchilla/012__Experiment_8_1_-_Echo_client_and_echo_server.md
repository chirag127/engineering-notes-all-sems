### Experiment 8.1 - Echo client and echo server

In this experiment, we will learn about the Echo client and Echo server. Echo client and Echo server are two simple programs that can be used to understand the basic concepts of client-server communication.

#### Echo Server

An Echo server is a program that listens for incoming connections from clients and echoes back whatever the client sends. Here are the steps involved in creating an Echo server:

1. Create a server socket using the `socket()` function provided by the socket module in Python.
2. Bind the server socket to a specific address and port using the `bind()` function.
3. Listen for incoming connections using the `listen()` function.
4. Accept incoming connections using the `accept()` function.
5. Receive data from the client using the `recv()` function.
6. Echo back the received data to the client using the `send()` function.
7. Close the connection using the `close()` function.

#### Echo Client

An Echo client is a program that connects to an Echo server and sends a message to the server. The server then echoes back the message to the client. Here are the steps involved in creating an Echo client:

1. Create a client socket using the `socket()` function provided by the socket module in Python.
2. Connect to the server using the `connect()` function and specifying the server address and port.
3. Send a message to the server using the `send()` function.
4. Receive the echoed back message from the server using the `recv()` function.
5. Close the connection using the `close()` function.

#### Implementation

To implement the Echo server and Echo client programs, we can use the Python socket module. Here is an example code for the Echo server:

```python
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```

And here is an example code for the Echo client:

```python
import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))
```

#### Conclusion

In this experiment, we learned about the Echo server and Echo client programs, which are used to demonstrate the basic concepts of client-server communication. We learned about the steps involved in creating an Echo server and Echo client, and we also saw example code for both programs. By understanding the Echo server and Echo client, we can gain a better understanding of how client-server communication works.