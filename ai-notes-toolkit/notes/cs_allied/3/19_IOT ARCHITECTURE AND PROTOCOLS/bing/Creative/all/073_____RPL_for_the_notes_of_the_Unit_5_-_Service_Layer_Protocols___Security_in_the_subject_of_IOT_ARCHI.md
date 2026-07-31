# RPL for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for **Routing Protocol for Low-Power and Lossy Networks**  .
- It is an **IPv6** routing protocol that is standardized for the **Internet of Things (IoT)** by **Internet-Engineering Task Force (IETF)** .
- It supports **multipoint-to-point (MP-to-P)**, **point-to-point (P-to-P)** and **point-to-multipoint (P-to-MP)** communications .
- It forms a **tree-like topology** which is based on different optimizing process called **Objective Function (OF)** .
- It assumes two types of nodes in a network: **border router (gateway)** and **ordinary nodes** .
- The gateway has a connection to the **Internet**, hence it connects nodes in an LLN to the Internet .
- It uses **Directed Acyclic Graphs (DAGs)** to represent the network topology and routing paths.
- It defines two types of DAGs: **Destination-Oriented DAG (DODAG)** and **Instance DAG (IDAG)**.
- A DODAG is a subgraph of a DAG that has a single **root node** and a common **objective function**.
- An IDAG is a set of DODAGs that share the same **RPL instance ID** and the same **administrative domain**.
- RPL uses **control messages** to build and maintain the DAGs, such as **DAG Information Object (DIO)**, **DAG Information Solicitation (DIS)**, **Destination Advertisement Object (DAO)**, and **Destination Advertisement Object Acknowledgment (DAO-ACK)**.
- RPL provides **security mechanisms** to protect the control messages and the network topology from **attacks**, such as **replay protection**, **integrity protection**, and **confidentiality protection**.
- RPL also supports **routing metrics** and **constraints** to optimize the routing paths according to the **application requirements** and the **network characteristics**.
- RPL is considered the **de facto routing protocol** for the IoT, but it also has some **challenges** and **limitations**, such as **scalability**, **mobility**, **reliability**, and **interoperability**.