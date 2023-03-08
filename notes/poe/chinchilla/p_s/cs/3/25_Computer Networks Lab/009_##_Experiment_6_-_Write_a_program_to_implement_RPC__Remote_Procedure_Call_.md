## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

Remote Procedure Call (RPC) is a protocol that allows a computer program to call a subroutine or a procedure on another computer without being aware of the details of network communication. In this experiment, we will be implementing RPC using Python.

### Steps to implement RPC

1. Install the 'rpcudp' module using pip. This module provides a simple RPC implementation over UDP.
2. Define the functions that you want to call remotely. These functions should be defined in a separate file, which will be imported by both the client and server programs.
3. Write the server program. The server program should create an instance of the RPC server using the 'rpcudp.Server' class from the 'rpcudp' module. The server should register the functions that it wants to make available to clients using the 'register_function' method of the server object.
4. Write the client program. The client program should create an instance of the RPC client using the 'rpcudp.Client' class from the 'rpcudp' module. The client should call the remote functions using the 'call' method of the client object.
5. Run the server program and the client program in separate terminals. The client program should be able to call the functions defined in the server program.

### Advantages of RPC

- Allows for the separation of concerns between the client and server programs.
- Provides a simple and efficient way to call remote functions.
- Can be used to implement distributed systems.

### Disadvantages of RPC

- Requires network communication, which can introduce latency and increase complexity.
- Can be vulnerable to security attacks, such as man-in-the-middle attacks.

### Example

Let's say we have a server program that defines a function 'add_numbers' that takes two arguments and returns their sum. The client program can call this function remotely using RPC.

Server program:

```
from rpcudp.server import RPCServer

def add_numbers(a, b):
    return a + b

server = RPCServer(('localhost', 8000))
server.register_function(add_numbers)

server.run()
```

Client program:

```
from rpcudp.client import RPCClient

client = RPCClient('localhost', 8000)

result = client.call('add_numbers', 5, 10)

print(result) # Output: 15
```

### Applications of RPC

- Distributed systems
- Microservices architecture
- Client-server applications