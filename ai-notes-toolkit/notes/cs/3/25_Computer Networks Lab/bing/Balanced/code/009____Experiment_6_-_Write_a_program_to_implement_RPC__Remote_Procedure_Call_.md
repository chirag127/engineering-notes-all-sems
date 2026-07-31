## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

- RPC (Remote Procedure Call) is a technique that allows a program to invoke a procedure or a function on a different machine or process as if it were a local call.
- RPC hides the details of the network communication, such as the message formats, protocols, and data marshalling, from the application programmer.
- RPC can be implemented using different models, such as client-server, peer-to-peer, or broker-based.
- In this experiment, we will write a simple RPC program using the client-server model, where the client invokes a remote procedure on the server and receives the result.
- The remote procedure we will implement is a calculator service that can perform basic arithmetic operations, such as addition, subtraction, multiplication, and division.
- We will use Python as the programming language and XML-RPC as the RPC protocol.
- XML-RPC is a standard that uses XML to encode the requests and responses, and HTTP as the transport protocol.
- Python provides a built-in module called xmlrpc that supports both XML-RPC client and server functionality.

### Steps to implement RPC program

1. Import the xmlrpc module in both the client and the server programs.
2. Create a server object using the xmlrpc.server.SimpleXMLRPCServer class, passing the host and port as arguments.
3. Define the remote procedures as regular Python functions, and register them with the server object using the register_function method.
4. Start the server loop using the serve_forever method, which will listen for incoming requests and dispatch them to the registered functions.
5. Create a client object using the xmlrpc.client.ServerProxy class, passing the URL of the server as an argument.
6. Invoke the remote procedures on the client object as if they were local methods, passing the arguments as normal.
7. Handle any exceptions that may occur during the RPC communication, such as xmlrpc.client.Fault or xmlrpc.client.ProtocolError.

### Example code for RPC program

#### Server code

```python
# Import the xmlrpc module
import xmlrpc.server

# Define the remote procedures
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# Create a server object
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))

# Register the remote procedures with the server
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(mul, "mul")
server.register_function(div, "div")

# Start the server loop
print("Server is running on port 8000")
server.serve_forever()
```

#### Client code

```python
# Import the xmlrpc module
import xmlrpc.client

# Create a client object
client = xmlrpc.client.ServerProxy("http://localhost:8000")

# Invoke the remote procedures
try:
    print("Addition: 5 + 3 =", client.add(5, 3))
    print("Subtraction: 5 - 3 =", client.sub(5, 3))
    print("Multiplication: 5 * 3 =", client.mul(5, 3))
    print("Division: 5 / 3 =", client.div(5, 3))
except xmlrpc.client.Fault as f:
    print("Fault occurred:", f.faultCode, f.faultString)
except xmlrpc.client.ProtocolError as p:
    print("Protocol error occurred:", p.errcode, p.errmsg)
```

### Expected output

#### Server output

```
Server is running on port 8000
```

#### Client output

```
Addition: 5 + 3 = 8
Subtraction: 5 - 3 = 2
Multiplication: 5 * 3 = 15
Division: 5 / 3 = 1.6666666666666667
```