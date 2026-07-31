## Experiment 17 - Socket programming using UDP and TCP

Socket programming is a way of communicating between two processes on a network, where one process is the client and the other is the server. In this experiment, we will be exploring socket programming using UDP and TCP protocols. 

### UDP Protocol

1. UDP stands for User Datagram Protocol and is a simple protocol used for sending packets over a network.
2. UDP is connectionless, which means that packets can be sent without establishing a connection.
3. UDP packets are smaller in size as compared to TCP packets, making them faster to transmit.
4. UDP packets are not guaranteed to arrive at their destination, as there is no error checking mechanism in place.
5. UDP is used for applications where speed is more important than reliability, such as online gaming.

### TCP Protocol

1. TCP stands for Transmission Control Protocol and is a more complex protocol used for sending packets over a network.
2. TCP is connection-oriented, which means that a connection must be established before data can be transmitted.
3. TCP packets are larger in size as compared to UDP packets, making them slower to transmit.
4. TCP packets are guaranteed to arrive at their destination, as there is an error checking mechanism in place.
5. TCP is used for applications where reliability is more important than speed, such as file transfers.

### Simple DNS

1. DNS stands for Domain Name System and is used to convert domain names into IP addresses.
2. A simple DNS client and server can be implemented using socket programming.
3. The client sends a request to the server, asking for the IP address of a particular domain name.
4. The server looks up the IP address in its database and sends it back to the client.
5. The client can then use the IP address to establish a connection with the server.

### Data & Time Client/Server

1. A data and time client/server can also be implemented using socket programming.
2. The client sends a request to the server, asking for the current date and time.
3. The server retrieves the current date and time from its system clock and sends it back to the client.
4. The client can then display the date and time on its screen.

### Echo Client/Server

1. An echo client/server can be implemented using socket programming.
2. The client sends a message to the server.
3. The server receives the message and sends it back to the client.
4. The client can then display the message on its screen.

### Iterative & Concurrent Servers

1. Iterative servers handle one client at a time, which means that each client must wait for the previous client to finish before it can be served.
2. Concurrent servers handle multiple clients at the same time, which means that each client can be served simultaneously.
3. Concurrent servers use multithreading or multiprocessing to handle multiple clients at the same time.
4. Iterative servers are simpler to implement but can be slower if there are many clients.
5. Concurrent servers are more complex to implement but can handle more clients at the same time, making them faster.