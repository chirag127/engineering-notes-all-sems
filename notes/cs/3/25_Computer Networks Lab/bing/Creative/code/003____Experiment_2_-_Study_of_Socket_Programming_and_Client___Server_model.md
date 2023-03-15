# Experiment 2 - Study of Socket Programming and Client – Server model

## Introduction

- Socket programming is a way of enabling communication between processes running on different machines over a network.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol.
- A protocol is a set of rules and conventions that define how data is exchanged between processes.
- A client-server model is a distributed application structure that partitions tasks between the providers of a resource or service, called servers, and service requesters, called clients.
- A server is a process that listens for incoming requests from clients and responds accordingly.
- A client is a process that initiates a connection to a server and sends requests for a resource or service.
- A client and a server communicate via sockets using a well-established protocol, such as TCP or UDP.

## Objectives

- To understand the basic concepts of socket programming and client-server model.
- To learn how to create and use sockets in C/C++ programming language.
- To implement a simple client-server application using TCP and UDP protocols.

## Procedure

### TCP Socket Programming

- TCP stands for Transmission Control Protocol, which is a connection-oriented and reliable protocol that ensures in-order and error-free delivery of data.
- To create a TCP socket, we need to specify the domain as AF_INET (IPv4), the type as SOCK_STREAM (stream socket), and the protocol as 0 (default for TCP).
- To establish a TCP connection, the server needs to bind a socket to a local address and port, and listen for incoming connection requests from clients.
- The client needs to specify the server's address and port, and connect to the server's socket.
- Once the connection is established, the client and the server can send and receive data using the read and write functions, or the send and recv functions.
- To terminate the connection, the client and the server can close their sockets.

### UDP Socket Programming

- UDP stands for User Datagram Protocol, which is a connectionless and unreliable protocol that does not guarantee delivery, order, or error-checking of data.
- To create a UDP socket, we need to specify the domain as AF_INET (IPv4), the type as SOCK_DGRAM (datagram socket), and the protocol as 0 (default for UDP).
- To send and receive data, the server and the client do not need to establish a connection, but they need to specify the destination address and port for each datagram using the sendto and recvfrom functions.
- The server and the client can also use the bind function to associate a socket with a local address and port, which can be useful for receiving datagrams from any source.
- To terminate the communication, the server and the client can close their sockets.

## Example

- In this example, we will implement a simple client-server application that allows the client to send a message to the server and receive an echo message from the server.
- We will use both TCP and UDP protocols to demonstrate the difference between them.
- The server will run on the local host (127.0.0.1) and listen on port 8080.
- The client will connect to the server's address and port, and send a message of its choice.
- The server will receive the message and send it back to the client.
- The client will receive the echo message and display it on the screen.
- The communication will end when the client sends an empty message or presses Ctrl+C.

### TCP Server

```c
// TCP server program

// Include the necessary header files
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

// Define the server's address and port
#define SERVER_ADDR "127.0.0.1"
#define SERVER_PORT 8080

// Define the buffer size
#define BUFFER_SIZE 1024

// Define the main function
int main()
{
    // Declare the variables
    int server_socket, client_socket; // Socket descriptors
    struct sockaddr_in server_addr, client_addr; // Socket address structures
    socklen_t client_len; // Length of client address structure
    char buffer[BUFFER_SIZE]; // Buffer for sending and receiving data
    int bytes; // Number of bytes sent or received

    // Create a TCP socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket < 0) // Check for errors
    {
        perror("socket");
        exit(1);
    }

    // Initialize the server address structure