### Experiment 2.2 - Study of Client – Server model

- Objective: To understand the basic concepts and working of the client-server model in computer networks.
- Theory: 
  - The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.
  - A server is a computer program or a device that provides a service to another computer program and its user, also known as the client. A server can run on the same computer as the client, or it can run on a remote computer.
  - A client is a computer program that accesses a service made available by a server as part of the client–server model of computer networks. The client initiates an exchange, while the server waits for requests from any available client.
  - Examples of client-server systems include web browsers and web servers, email clients and email servers, and online chat applications.
  - The client-server model is based on the principle of separation of concerns, where each part of the system has a specific role and responsibility. The client is responsible for the user interface and the application logic, while the server is responsible for the data storage and processing.
  - The client-server model allows for modularity, scalability, security, and interoperability of the system. It also enables the distribution of the workload among multiple servers, which can improve the performance and reliability of the system.
- Procedure:
  - To study the client-server model, we will use a simple example of a chat application that allows two users to communicate with each other over a network.
  - The chat application consists of two programs: a chat client and a chat server. The chat client is a graphical user interface that allows the user to enter and send messages, and to receive and display messages from the other user. The chat server is a program that runs on a remote computer and handles the communication between the two chat clients.
  - The chat server listens for incoming connections from chat clients on a specific port number. When a chat client connects to the chat server, the server assigns a unique identifier to the client and adds it to a list of active clients. The server then waits for messages from the client and forwards them to the other client. The server also notifies the clients about the connection and disconnection of the other client.
  - The chat client establishes a connection to the chat server using the server's IP address and port number. The client then sends its username to the server and waits for a confirmation. The client then displays a chat window where the user can enter and send messages, and receive and display messages from the other user. The client also shows the status of the connection and the username of the other user. The client can terminate the connection by closing the chat window or sending a special message to the server.
- Diagram:

```
+-----------------+             +-----------------+             +-----------------+
|                 |             |                 |             |                 |
|   Chat Client   |  <--------> |   Chat Server   |  <--------> |   Chat Client   |
|                 |             |                 |             |                 |
+-----------------+             +-----------------+             +-----------------+
|                 |             |                 |             |                 |
|   User 1        |             |   Port 1234     |             |   User 2        |
|                 |             |                 |             |                 |
+-----------------+             +-----------------+             +-----------------+
```
- Expected Output:
  - The chat application should allow the two users to exchange messages with each other over the network.
  - The chat application should display the messages in a chat window along with the username and timestamp of the sender.
  - The chat application should show the status of the connection and the username of the other user.
  - The chat application should handle the connection and disconnection of the clients gracefully and notify the other user accordingly.
- Conclusion:
  - The client-server model is a widely used architecture for distributed applications that enables the separation of concerns, modularity, scalability, security, and interoperability of the system.
  - The chat application is a simple example of a client-server system that demonstrates the basic concepts and working of the client-server model in computer networks.