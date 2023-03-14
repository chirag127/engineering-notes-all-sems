### Introduction to client-server computing

- Client-server computing is a software architecture model that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients. 
- Clients and servers communicate over a computer network or on the same computer using a common language and rules, called a communications protocol. 
- Servers are classified by the services they provide, such as web servers, file servers, database servers, etc. 
- Clients usually do not share any of their resources, but they request content or service from a server. Clients initiate communication sessions with servers, which await incoming requests. 
- The client-server model is a distributed application structure, which means that the application logic and data management functions are split among different devices or processes. 
- There are different styles of client-server computing, based on how the presentation, application logic and data management functions are partitioned between the client and server device. 
- Some of the advantages of client-server computing are:
  - Scalability: Servers can handle multiple clients simultaneously and new servers can be added to increase the capacity of the system. 
  - Modularity: Clients and servers can be developed and maintained independently, as long as they follow the same protocol. 
  - Security: Servers can enforce access control policies and protect sensitive data from unauthorized clients. 
  - Performance: Clients can offload computation-intensive tasks to servers, which can have more processing power and memory. 
- Some of the disadvantages of client-server computing are:
  - Complexity: Clients and servers need to coordinate and synchronize their actions and handle errors and failures. 
  - Dependency: Clients depend on the availability and reliability of servers, which can be affected by network congestion, power outages, hardware failures, etc. 
  - Bottlenecks: Servers can become overloaded by too many client requests, which can degrade the performance and responsiveness of the system. 
  - Security: Clients and servers need to protect their communication from eavesdropping, tampering, and spoofing by malicious parties. 

- A simple example of client-server computing is the World Wide Web, where a web browser is a client that requests web pages from a web server, which responds with the requested content. 
- A simple ASCII diagram of client-server computing is:

```
    +--------+      request      +--------+
    | Client | ----------------> | Server |
    +--------+                   +--------+
                  response
    +--------+ <---------------- | Server |
    | Client |                   +--------+
    +--------+
```

: Client–server model - Wikipedia
: Definition of Client/server - Gartner Information Technology Glossary