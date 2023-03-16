### Sockets for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A socket is an endpoint of communication between two processes or devices over a network.
- Sockets can be used to send and receive data using different protocols, such as TCP (Transmission Control Protocol) or UDP (User Datagram Protocol).
- TCP is a reliable, connection-oriented protocol that ensures data integrity and delivery. UDP is an unreliable, connectionless protocol that does not guarantee data integrity or delivery, but is faster and more efficient.
- Both VXWORKS and FREE RTOS support sockets as a way of implementing network communication in embedded systems and real-time operating systems.
- VXWORKS is a proprietary, UNIX-like real-time operating system developed by WindRiver. It is highly scalable and configurable, and can be used for various applications, such as aerospace, defense, industrial, and automotive.
- FREE RTOS is an open source, portable, and scalable real-time operating system that can run on various microcontrollers and platforms. It provides a familiar and standards-based Berkeley sockets interface, as well as an alternative callback interface for advanced users.
- To create a socket in VXWORKS, the function `socket()` is used, which takes three parameters: the domain (AF_INET for IPv4), the type (SOCK_STREAM for TCP or SOCK_DGRAM for UDP), and the protocol (0 for default or IPPROTO_TCP or IPPROTO_UDP for specific).
- To create a socket in FREE RTOS, the function `FreeRTOS_socket()` is used, which takes three parameters: the domain (FREERTOS_AF_INET for IPv4), the type (FREERTOS_SOCK_STREAM for TCP or FREERTOS_SOCK_DGRAM for UDP), and the protocol (0 for default or FREERTOS_IPPROTO_TCP or FREERTOS_IPPROTO_UDP for specific).
- To bind a socket to a specific port number and IP address, the function `bind()` is used in both VXWORKS and FREE RTOS, which takes three parameters: the socket descriptor, the address structure (sockaddr_in for IPv4), and the size of the address structure.
- To listen for incoming connections on a TCP socket, the function `listen()` is used in both VXWORKS and FREE RTOS, which takes two parameters: the socket descriptor and the backlog (the maximum number of pending connections).
- To accept an incoming connection on a TCP socket, the function `accept()` is used in both VXWORKS and FREE RTOS, which takes three parameters: the socket descriptor, the address structure (sockaddr_in for IPv4) of the peer, and the size of the address structure. It returns a new socket descriptor for the accepted connection.
- To connect to a remote server on a TCP socket, the function `connect()` is used in both VXWORKS and FREE RTOS, which takes three parameters: the socket descriptor, the address structure (sockaddr_in for IPv4) of the server, and the size of the address structure.
- To send data on a TCP or UDP socket, the function `send()` or `sendto()` is used in both VXWORKS and FREE RTOS, which takes four parameters: the socket descriptor, the buffer containing the data, the length of the data, and the flags (0 for default or MSG_DONTWAIT for non-blocking). The function `sendto()` also takes two additional parameters: the address structure (sockaddr_in for IPv4) of the destination, and the size of the address structure.
- To receive data on a TCP or UDP socket, the function `recv()` or `recvfrom()` is used in both VXWORKS and FREE RTOS, which takes four parameters: the socket descriptor, the buffer to store the data, the length of the buffer, and the flags (0 for default or MSG_DONTWAIT for non-blocking). The function `recvfrom()` also takes two additional parameters: the address structure (sockaddr_in for IPv4) of the source, and the size of the address structure.
- To close a socket, the function `close()` is used in both VXWORKS and FREE RTOS, which takes one parameter: the socket descriptor.

: https://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_TCP/index.html
: https://www.slideshare.net/sc09b093/vx-works-rtos
: https://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_TCP/API/socket.html
: https://