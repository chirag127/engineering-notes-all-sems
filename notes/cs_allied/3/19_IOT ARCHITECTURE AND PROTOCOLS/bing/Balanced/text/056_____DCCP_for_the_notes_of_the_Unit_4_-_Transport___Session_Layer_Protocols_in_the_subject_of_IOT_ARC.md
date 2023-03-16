### DCCP

- DCCP stands for **Datagram Congestion Control Protocol**.
- It is a **message-oriented** transport layer protocol that provides **unreliable** data delivery .
- It is designed to solve issues present in UDP and TCP, particularly for **real-time** and **multimedia** (streaming) traffic .
- It implements **reliable** connection setup, teardown, **Explicit Congestion Notification (ECN)**, congestion control, and feature negotiation .
- It supports **pluggable** congestion control modules called **CCIDs** (Congestion Control IDentifiers) that can be selected by the application or negotiated by the endpoints .
- It uses a **packet header** that contains a **sequence number**, a **type** field, and a **checksum** field.
- It defines several **packet types** for different purposes, such as **Request**, **Response**, **Data**, **Ack**, **Close**, etc.
- It uses a **three-way handshake** to establish a connection and a **four-way handshake** to close a connection.
- It uses a **feature negotiation** mechanism to allow the endpoints to agree on various options, such as **CCID**, **ECN**, **checksum coverage**, etc.
- It provides a **socket API** for applications to use DCCP as a transport protocol.