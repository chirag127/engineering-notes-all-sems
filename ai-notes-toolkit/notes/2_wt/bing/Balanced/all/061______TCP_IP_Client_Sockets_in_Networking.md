#### TCP/IP Client Sockets in Networking

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet.
- A socket can be used to connect Java’s I/O system to other programs that may reside either on the local machine or on any other machine on the Internet.
- A TCP socket is defined by the IP address of the machine and the port it uses. The IP address identifies the host, and the port number identifies the service on the host.
- The TCP socket guarantees that all data is received and acknowledged, and that the data is delivered in the same order as it was sent.
- To create a TCP client socket in Java, you need to do the following steps:
  - Import the java.net and java.io packages.
  - Create an instance of the Socket class by specifying the host name and port number of the server.
  - Get the input and output streams of the socket using the getInputStream() and getOutputStream() methods.
  - Use the input and output streams to communicate with the server using the read() and write() methods.
  - Close the socket using the close() method when the communication is done.
- To create a TCP client socket in C#, you need to do the following steps:
  - Import the System.Net and System.Net.Sockets namespaces.
  - Create an instance of the IPEndPoint class by specifying the IP address and port number of the server.
  - Create an instance of the Socket class by specifying the address family, socket type, and protocol type that the socket uses to make connections.
  - Connect the socket to the server using the Connect() method and passing the IPEndPoint object as a parameter.
  - Get the NetworkStream object of the socket using the Socket.GetStream() method.
  - Use the NetworkStream object to communicate with the server using the Read() and Write() methods.
  - Close the socket using the Close() method when the communication is done.
- A possible mnemonic to remember the steps for creating a TCP client socket is **I SING C**:
  - **I**mport the packages or namespaces
  - **S**pecify the host name and port number or the IP address and port number
  - **I**nstantiate the Socket class
  - **N**egotiate the connection with the server
  - **G**et the input and output streams or the network stream
  - **C**ommunicate with the server and close the socket
- Some advantages of using TCP sockets are :
  - They provide reliable and ordered data delivery
  - They handle congestion control and flow control
  - They support error detection and correction
  - They are widely used and supported by many protocols and applications
- Some disadvantages of using TCP sockets are :
  - They have more overhead and latency than UDP sockets
  - They are not suitable for real-time or multicast applications
  - They are vulnerable to SYN flooding attacks
  - They are not scalable for large-scale distributed systems
- Some examples of applications that use TCP sockets are :
  - Web browsers and servers
  - Email clients and servers
  - File transfer clients and servers
  - Remote login and shell services
  - Database clients and servers
- A possible ASCII diagram of a TCP client socket communicating with a TCP server socket is:

```
    TCP client socket                             TCP server socket
    -----------------                             -----------------
    | IP: 120.1.1.1  |                           | IP: 189.1.1.1  |
    | Port: 1234     |                           | Port: 80       |
    -----------------                             -----------------
          |                                             |
          |  SYN (seq=x)                               |
          |-------------------------------------------->|
          |                                             |
          |                            SYN-ACK (seq=y,  |
          |<--------------------------------------------| 
          |  ACK (seq=x+1, ack=y+1)                     |
          |-------------------------------------------->|
          |                                             |
          |  Data (seq=x+1, ack=y+1, data="GET /")      |
          |-------------------------------------------->|
          |                                             |
          |                            Data (seq=y+1,   |
          |<--------------------------------------------| 
          |  ack=x+9, data="HTTP/1.1 200 OK")           |
          |

```
