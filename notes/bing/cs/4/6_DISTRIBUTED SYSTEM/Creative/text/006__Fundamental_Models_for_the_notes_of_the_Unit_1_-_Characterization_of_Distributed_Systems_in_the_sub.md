### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are abstract descriptions of properties that are present in all distributed systems, regardless of their specific architectures or applications.
- Fundamental models can help us understand the challenges and trade-offs involved in designing and implementing distributed systems, as well as compare different solutions and approaches.
- There are three main types of fundamental models: architectural models, interaction models, and failure models.

#### Architectural Models
- Architectural models describe the structure and organization of the components of a distributed system and their relationships.
- Architectural models can be classified into two categories: static models and dynamic models.
- Static models focus on the physical layout and configuration of the components, such as the number, type, and location of the nodes and the communication links.
- Dynamic models focus on the behavior and evolution of the components, such as the creation, migration, replication, and termination of the nodes and the communication channels.
- Some common architectural models are:

  - Master-slave: In this model, one node of the distributed system plays the role of master. Here, the master node has complete information about the system and controls the decision making. The other nodes are slaves that execute the tasks assigned by the master and report the results back to the master. This model is simple and efficient, but it has a single point of failure and a scalability bottleneck in the master node .
  - Peer-to-peer: In this model, there is no single master designated amongst the nodes in a distributed system. All the nodes equally share the responsibility of the master. They cooperate and coordinate with each other to perform the tasks and achieve the goals of the system. This model is scalable and fault-tolerant, but it has a high communication overhead and a lack of global knowledge .
  - Client-server: In this model, there are two types of nodes: clients and servers. Clients are nodes that request services from the servers. Servers are nodes that provide services to the clients. This model is widely used in many applications, such as web browsing, email, and file sharing. This model is modular and easy to implement, but it has a performance and reliability dependency on the servers.
  - Broker: In this model, there is a third type of node: broker. Brokers are nodes that act as intermediaries between the clients and the servers. They are responsible for locating the servers that can provide the requested services, forwarding the requests from the clients to the servers, and returning the responses from the servers to the clients. This model is useful for hiding the complexity and heterogeneity of the servers from the clients, but it introduces an additional layer of communication and a potential bottleneck in the brokers.

#### Interaction Models
- Interaction models describe the issues and mechanisms related to the communication and coordination of the components of a distributed system.
- Interaction models can be classified into two categories: synchronous models and asynchronous models.
- Synchronous models assume that there are known bounds on the communication delay, the processing speed, and the clock drift rate of the components. Synchronous models can simplify the design and analysis of distributed algorithms, but they are unrealistic and impractical for most real-world distributed systems .
- Asynchronous models do not assume any bounds on the communication delay, the processing speed, or the clock drift rate of the components. Asynchronous models can capture the reality and uncertainty of distributed systems, but they make the design and analysis of distributed algorithms more complex and challenging .
- Some common interaction models are:

  - Message passing: In this model, the components communicate by sending and receiving messages over the communication channels. Message passing can be either blocking or non-blocking, depending on whether the sender or the receiver waits for the message to be delivered or not. Message passing can also be either point-to-point or multicast, depending on whether the message is sent to one or multiple destinations. Message passing is the most basic and general interaction model, but it requires explicit and low-level programming .
  - Remote procedure call: In this model, the components communicate by invoking procedures or functions on remote nodes as if they were local. Remote procedure call abstracts away the details of message passing and provides a higher-level and more convenient programming interface. Remote procedure call can also support different invocation semantics, such as at-most-once, at-least-once, or exactly-once, depending on the reliability and idempotency of the procedures or