## Experiment 5 - Create a Socket for HTTP for Web Page Upload and Download

In this experiment, we will learn how to create a socket for HTTP for web page upload and download. This experiment will help to understand the basic concepts of socket programming in Python and how to use sockets to transfer data over a network.

### Objectives:

- To create a socket for HTTP for web page upload and download.
- To understand the basics of socket programming in Python.
- To learn how to use sockets to transfer data over a network.

### Requirements:

- Python installed on your computer.
- A text editor to write and save Python code.
- Basic knowledge of socket programming in Python.

### Procedure:

1. Create a Python file and name it `http_socket.py`.
2. Import the socket module in the Python file using the `import` keyword.
3. Create a socket object using the `socket()` method of the socket module.
4. Bind the socket object to a specific IP address and port number using the `bind()` method.
5. Listen for incoming connections using the `listen()` method.
6. Accept incoming connections using the `accept()` method.
7. Receive data from the client using the `recv()` method.
8. Send data to the client using the `send()` method.
9. Close the connection using the `close()` method.

### Code:

```python
import socket

# create a socket object
s = socket.socket()

# bind the socket to a specific IP address and port number
s.bind(('localhost', 8000))

# listen for incoming connections
s.listen(5)

# accept incoming connections
conn, addr = s.accept()

# receive data from the client
data = conn.recv(1024)

# send data to the client
conn.send(b'HTTP/1.1 200 OK\r\n\r\nHello, World!')

# close the connection
conn.close()
```

### Explanation:

- The `socket()` method creates a socket object that can be used to send and receive data over a network.
- The `bind()` method binds the socket to a specific IP address and port number.
- The `listen()` method listens for incoming connections.
- The `accept()` method accepts incoming connections and returns a new socket object and the address of the client.
- The `recv()` method receives data from the client.
- The `send()` method sends data to the client.
- The `close()` method closes the connection.

### Conclusion:

In this experiment, we have learned how to create a socket for HTTP for web page upload and download. We have also learned the basic concepts of socket programming in Python and how to use sockets to transfer data over a network. This experiment will help to understand the fundamentals of socket programming and how to use sockets to build network-based applications.