### Experiment 8.2 - Chat

- The objective of this experiment is to design and implement a simple chat application using sockets and threads in Python.
- The chat application allows multiple clients to connect to a server and exchange messages with each other or with the server.
- The chat application consists of two main components: the server and the client.
- The server is responsible for listening for incoming connections, accepting new clients, creating threads for each client, and broadcasting messages to all clients.
- The client is responsible for connecting to the server, sending and receiving messages, and displaying them on the console.
- The server and the client communicate using a predefined protocol that consists of a header and a payload. The header contains the length of the payload and the payload contains the actual message.
- The server and the client use sockets to establish a TCP connection and exchange data. Sockets are endpoints of communication that allow data to flow between processes on the same or different machines.
- The server and the client use threads to handle multiple connections and messages concurrently. Threads are units of execution that run in parallel within a process and share the same memory space.
- The server and the client use locks to synchronize access to shared resources, such as the socket or the list of clients. Locks are mechanisms that prevent multiple threads from modifying the same resource at the same time.
- The server and the client use queues to store and retrieve messages in a FIFO (first-in, first-out) manner. Queues are data structures that allow adding elements at one end and removing them at the other end.