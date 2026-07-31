# RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for **Routing Protocol for Low-Power and Lossy Networks**.
- It is an **IPv6** routing protocol that is standardized for the **Internet of Things (IoT)** by **Internet-Engineering Task Force (IETF)**  .
- It is designed for **resource-constrained** networks that have **heterogeneous traffic**, **low bandwidth**, **high packet loss**, and **dynamic topology**  .
- It forms a **tree-like topology** that is based on different optimizing process called **Objective Function (OF)** .
- It supports both **many-to-one** and **one-to-one** communication, as well as **multicast** and **anycast** .
- It uses **Destination Oriented Directed Acyclic Graphs (DODAGs)** as the routing structure, where each node has a **rank** that indicates its position in the graph  .
- It defines three types of control messages: **DODAG Information Object (DIO)**, **Destination Advertisement Object (DAO)**, and **DODAG Information Solicitation (DIS)**  .
- DIO messages are used to **advertise** the DODAG and its parameters, such as the OF, the rank, and the prefix  .
- DAO messages are used to **inform** the DODAG root or a parent node about the **downward routes** to the destination nodes  .
- DIS messages are used to **request** DIO messages from neighboring nodes  .
- RPL has several advantages, such as **scalability**, **adaptability**, **energy efficiency**, and **interoperability** with other IPv6 protocols  .
- RPL also has some challenges, such as **security**, **reliability**, **mobility**, and **performance**  .