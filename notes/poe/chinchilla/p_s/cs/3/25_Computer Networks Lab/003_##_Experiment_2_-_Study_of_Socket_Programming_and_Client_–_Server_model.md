## Experiment 2 - Study of Socket Programming and Client – Server model

Socket programming is a way of connecting two nodes on a network to communicate with each other. A socket is a software endpoint that establishes communication between different processes on different nodes. In this experiment, we will study socket programming and the client-server model.

### Client-Server Model

The client-server model is a distributed computing architecture in which a client requests services from a server, and the server provides the requested services to the client. The client sends a request to the server, and the server processes the request and sends a response back to the client. This model is widely used in networking applications like web servers, email servers, and chat applications.

### Socket Programming

Socket programming is a way of implementing networking protocols. It provides a low-level interface for sending and receiving data over a network. Socket programming allows applications to communicate with each other using the Internet Protocol (IP) suite, which includes TCP, UDP, and IP.

#### Advantages of Socket Programming

- Socket programming provides a simple and efficient way of exchanging data between different applications.
- It is platform-independent and can be used on any operating system.
- Socket programming allows for real-time communication between applications, which is essential for many networking applications.

#### Disadvantages of Socket Programming

- Socket programming requires a good understanding of networking concepts.
- It can be difficult to debug and troubleshoot socket-based applications.
- Socket programming can be prone to security vulnerabilities if not implemented correctly.

#### Socket Programming Example

Here is an example of a simple client-server application using socket programming:

```
// Server code
#include <sys/socket.h>
#include <netinet/in.h>

int main()
{
    int serverSocket, clientSocket;
    struct sockaddr_in serverAddress, clientAddress;

    serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    memset(&serverAddress, '0', sizeof(serverAddress));

    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = htonl(INADDR_ANY);
    serverAddress.sin_port = htons(8080);

    bind(serverSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress));

    listen(serverSocket, 10);

    while(1)
    {
        char buffer[1024] = {0};
        clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddress, sizeof(clientAddress));
        read(clientSocket, buffer, 1024);
        printf("Message from client: %s\n", buffer);
    }

    return 0;
}

// Client code
#include <sys/socket.h>
#include <netinet/in.h>

int main()
{
    int clientSocket;
    struct sockaddr_in serverAddress;

    clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    memset(&serverAddress, '0', sizeof(serverAddress));

    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(8080);

    inet_pton(AF_INET, "127.0.0.1", &serverAddress.sin_addr);

    connect(clientSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress));

    char* message = "Hello from client";
    send(clientSocket, message, strlen(message), 0);

    return 0;
}
```

This code establishes a connection between a client and a server using sockets. The server listens for incoming connections and prints out any messages it receives from clients. The client sends a message to the server.

### Applications of Socket Programming

Socket programming is used in a wide range of applications, including:

- Web servers
- Email servers
- Chat applications
- Online gaming
- File sharing

### Conclusion

In conclusion, socket programming and the client-server model are essential concepts in networking. Understanding these concepts is crucial for building robust and efficient networking applications. By studying socket programming and the client-server model, you will be equipped with the knowledge to develop networking applications that can communicate with other applications over a network.