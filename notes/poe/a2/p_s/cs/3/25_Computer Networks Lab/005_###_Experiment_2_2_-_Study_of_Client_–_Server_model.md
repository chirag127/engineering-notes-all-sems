 Here is the content written in markdown format for the given topic:

### Experiment 2.2 - Study of Client – Server model

The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients. Often clients and servers communicate over a computer network on separate hardware. A server machine is a high-performance host that is running one or more server programs which share its resources with clients. A client does not share any of its resources, it requests content or service from the server.

**Advantages:**

- Centralized management: It is easy to manage servers as the resources and services are centralized. Updating software or applying patches can be done at one place.
- Specialization: Servers can be optimized for performing services efficiently. Clients can be thin clients with minimal resources.
- Scalability: It is easy to add more servers if demand increases. Workload can be distributed across multiple servers.
- Security: Sensitive data can be stored centrally on servers which can have additional security measures.

**Disadvantages:**

- Reliability: The system depends on the reliability of the server. If the server goes down, the service becomes unavailable to clients. Additional measures need to be taken to ensure high availability.
- Performance: The network connectivity between clients and servers must be good for acceptable performance. Heavy network traffic or latency can degrade performance.
- Cost: Specialized server hardware and software can be expensive to build and maintain the infrastructure.

**Examples:** Web servers, file servers, database servers, application servers, etc.

**Applications:** E-commerce websites, file sharing, messaging applications, streaming media, online transaction processing, etc.

The client-server model is a very popular distributed system architecture used in many modern applications and technologies due to the advantages it offers. With proper measures taken for reliability and performance, it can be scaled to handle huge workloads and numbers of users.