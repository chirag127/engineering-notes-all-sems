 Here is the content in markdown format for the given topic:

## Experiment 2 - Study of Socket Programming and Client – Server model

1. Socket Programming: Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. The two sockets then communicate with each other by sending and receiving data.

2. Client-Server Model: The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients. Often clients and servers communicate over a computer network on separate hardware. A server is a system with resources and a task which it provides to a client. A client is a system that utilises the resources or task provided by the server.

3. Client - The client initiates communication with the server by either connecting to the server or requesting for any service. After the request for service is received by the server, the client waits for the server to respond and acts according to the response.

4. Server - The server waits for requests from clients and listens on specific ports on the IP address. Once a request is received from a client, the server processes the request and sends back a response to the client. The server can handle requests from multiple clients simultaneously.

**Advantages:**
- Scalability: Client-server model is highly scalable as more servers can be added to handle increasing load.
- Flexibility: Servers and clients can be interchanged easily.
- Data centralization: Data can be stored centrally at the server which can be accessed by multiple clients.
- Work distribution: Work can be distributed efficiently among multiple servers to improve performance.

**Disadvantages:**
- Require dedicated servers: Client-server model requires dedicated servers which can add to cost.
- Single point of failure: If the server fails, the entire system fails. Additional measures need to be taken to handle failures.
- Security: Since data is stored centrally, security is important and breaches can lead to loss of sensitive data. Additional security measures are required.