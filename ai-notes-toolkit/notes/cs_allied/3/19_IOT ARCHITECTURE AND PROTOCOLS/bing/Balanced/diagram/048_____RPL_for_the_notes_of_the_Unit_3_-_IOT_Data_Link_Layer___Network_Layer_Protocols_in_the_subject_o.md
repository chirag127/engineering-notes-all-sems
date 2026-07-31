### RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for **Routing Protocol for Low-Power and Lossy Networks**.
- It is an **IPv6** routing protocol that is standardized for the **Internet of Things (IoT)** by **Internet-Engineering Task Force (IETF)** .
- It forms a **tree-like topology** which is based on different optimizing process called **Objective Function (OF)** .
- It supports both **many-to-one** and **one-to-one** communication.
- It is designed for **resource-constrained networks** that have low power, low bandwidth, high packet loss, and dynamic topology.
- It uses **Destination Oriented Directed Acyclic Graphs (DODAGs)** as the routing structure, where each node has a **rank** that indicates its position in the graph .
- It defines two types of messages: **DODAG Information Object (DIO)** and **DODAG Information Solicitation (DIS)** .
- DIO messages are used to **advertise** the DODAG and its parameters, such as the rank, the OF, and the prefix .
- DIS messages are used to **request** DIO messages from neighboring nodes .
- RPL also supports **local repair** and **global repair** mechanisms to handle topology changes and network failures .
- RPL has several advantages, such as **scalability**, **adaptability**, **energy efficiency**, and **interoperability** .
- RPL also has some challenges, such as **security**, **mobility**, **overhead**, and **performance** .