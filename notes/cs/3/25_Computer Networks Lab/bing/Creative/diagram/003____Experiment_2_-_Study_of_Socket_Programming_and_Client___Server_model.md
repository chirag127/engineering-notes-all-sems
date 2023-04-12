## Experiment 2 - Study of Socket Programming and Client – Server model

### Objective
To understand the concept of socket programming and client-server model in network communication.

### Theory
- A **socket** is a simple communication channel through which two programs communicate over a network.
- A socket supports two-way communication between a **client** and a **server**, using a well-established protocol.
- A **protocol** is a set of rules and behavior that both the server and client must follow in order to establish two-way communication.
- A **client** is a program that requests a service or resource from a server.
- A **server** is a program that provides a service or resource to a client.
- A **client-server model** is a distributed application structure that partitions tasks between the providers of a service (servers) and the requesters of a service (clients).
- A **client-server model** has the following advantages:
  - It allows multiple clients to access the same service or resource concurrently.
  - It reduces the network traffic and improves the performance by distributing the workload among different servers.
  - It enhances the security and reliability by isolating the servers from the clients and implementing authentication and encryption mechanisms.
  - It facilitates the scalability and maintainability by allowing the servers to be upgraded or replaced without affecting the clients.

### Steps
- To implement socket programming and client-server model in C/C++, we need to perform the following steps:
  - **Socket creation**: We use the `socket()` function to create a socket descriptor, which is an integer that identifies the socket. We need to specify the domain, type, and protocol of the socket. The domain can be `AF_INET` for IPv4 or `AF_INET6` for IPv6. The type can be `SOCK_STREAM` for TCP or `SOCK_DGRAM` for UDP. The protocol can be `0` for default or `IPPROTO_TCP` for TCP or `IPPROTO_UDP` for UDP.
  - **Setsockopt**: We use the `setsockopt()` function to manipulate the options for the socket. This is optional but useful for setting some parameters such as reuse of address, buffer size, timeout, etc.
  - **Bind**: We use the `bind()` function to assign a local address and port to the socket. This is necessary for the server socket to listen for incoming connections from the clients.
  - **Listen**: We use the `listen()` function to mark the socket as a passive socket, which means it can accept incoming connection requests from the clients. We need to specify the maximum number of pending connections that can be queued for the socket.
  - **Accept**: We use the `accept()` function to accept an incoming connection request from a client. This function blocks the server until a client connects to the server. It returns a new socket descriptor that is used for communication with the client.
  - **Connect**: We use the `connect()` function to establish a connection with the server. This function blocks the client until the server accepts the connection. It requires the server's address and port as arguments.
  - **Send/Receive**: We use the `send()` and `recv()` functions to send and receive data over the socket. These functions return the number of bytes sent or received, or -1 if an error occurs. We need to specify the socket descriptor, the buffer, the buffer size, and some flags as arguments.
  - **Close**: We use the `close()` function to close the socket and release the resources. This function returns 0 on success, or -1 on error. We need to specify the socket descriptor as an argument.

### Example
- The following is an example of a simple client-server program that uses TCP sockets to exchange messages. The server listens on port 8080 and echoes back whatever the client sends. The client connects to the server and sends a message "Hello, server!" and receives the same message back from the server.

#### Server
```c
// Server program
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

#define PORT 8080 // Port number
#define MAX 1024 // Buffer size

int main()
{
    int server_fd, client_fd; // Socket descriptors
    struct sockaddr_in server_addr, client_addr; // Socket addresses
    socklen_t client_len; // Client address length
    char buffer[MAX];

```
