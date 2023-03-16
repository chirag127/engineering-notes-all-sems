### RPL for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for **Routing Protocol for Low-Power and Lossy Networks**  .
- It is an **IPv6** routing protocol that is standardized for the **Internet of Things (IoT)** by **Internet-Engineering Task Force (IETF)** .
- It supports **multipoint-to-point (MP-to-P)**, **point-to-point (P-to-P)** and **point-to-multipoint (P-to-MP)** communications .
- It forms a **tree-like topology** which is based on different optimizing process called **Objective Function (OF)** .
- It assumes two types of nodes in a network: **border router (gateway)** and **ordinary nodes** .
- The gateway has a connection to the Internet, hence it connects nodes in an LLN to the Internet .
- RPL uses **Directed Acyclic Graphs (DAGs)** to represent the network topology and routing paths.
- A DAG is a graph that has no cycles, meaning that there is no way to start at a node and traverse the graph back to the same node.
- RPL defines two types of DAGs: **Destination-Oriented DAG (DODAG)** and **Instance DAG (IDAG)**.
- A DODAG is a DAG that has a single root node, which is the destination for all the traffic in the DAG.
- An IDAG is a set of DODAGs that share the same OF and configuration parameters.
- RPL uses **DODAG Information Object (DIO)** messages to advertise the DAG information and **DODAG Information Solicitation (DIS)** messages to request the DAG information.
- RPL also uses **Destination Advertisement Object (DAO)** messages to propagate the destination information and **Destination Advertisement Object Acknowledgment (DAO-ACK)** messages to acknowledge the DAO messages.
- RPL provides **security** mechanisms to protect the routing messages and the network topology from various attacks.
- RPL supports **symmetric-key cryptography** and **asymmetric-key cryptography** to secure the message exchange.
- RPL also supports **secure join** and **secure leave** procedures to authenticate the nodes and revoke the compromised nodes.
- RPL can be integrated with other service layer protocols, such as **CoAP**, **MQTT**, **DDS**, etc., to provide end-to-end communication and data exchange for IoT applications.