### Experiment 2.2 - Study of Client – Server model

The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients. 

#### Components of Client-Server Model

The client-server model consists of two main components:

1. Client: The client is a device or software application that requests a service or resource from the server. The client initiates the communication and sends requests to the server.

2. Server: The server is a device or software application that provides a service or resource to the client. The server receives requests from the client and sends responses back.

#### Types of Client-Server Model

There are two types of client-server models:

1. Two-tier architecture: In this architecture, the client communicates directly with the server. The server processes the request and sends the response back to the client. 

2. Three-tier architecture: In this architecture, a middle layer called the application server is added between the client and the server. The client communicates with the application server, which then communicates with the database server to retrieve the required data.

#### Advantages of Client-Server Model

1. Scalability: The client-server model allows for easy scalability by adding more servers to handle increasing client requests.

2. Security: The server can be configured to control access to resources, ensuring secure communication between the client and server.

3. Centralized management: The server can be used to manage and monitor client requests, making it easier to maintain the system.

#### Disadvantages of Client-Server Model

1. Complexity: The client-server model can be complex to implement and maintain, especially in large systems.

2. Dependency: The client is dependent on the server to provide the required service or resource, which can lead to performance issues if the server is overloaded.

#### Applications of Client-Server Model

The client-server model is used in various applications, including:

1. Web applications: In web applications, the client communicates with the web server to retrieve web pages and other resources.

2. Database management systems: In database management systems, the client communicates with the database server to retrieve and manipulate data.

3. Email systems: In email systems, the client communicates with the mail server to send and receive emails.

In conclusion, the client-server model is a widely used distributed application structure that partitions tasks or workloads between the server and client. It offers advantages such as scalability, security, and centralized management, but also has its drawbacks such as complexity and dependency. Understanding the client-server model is essential for building and maintaining distributed systems.