#### Datagram in Networking

A datagram is a basic unit of data transfer in a packet-switched network. A datagram consists of a header and a payload. The header contains information such as the source and destination addresses, the protocol type, and the length of the datagram. The payload contains the actual data to be transmitted. 

Datagrams are used in connectionless communication systems, where there is no established path or session between the sender and the receiver. Each datagram is routed independently by the intermediate network devices, such as routers or switches, based on the information in the header. There is no guarantee that the datagrams will arrive in the same order, or at all, at the destination.  

Datagrams are suitable for applications that can tolerate some loss or delay of data, such as voice or video streaming, or that require low overhead and high speed, such as real-time gaming. Datagrams are also useful for broadcasting or multicasting data to multiple recipients. 

One example of a protocol that uses datagrams is the User Datagram Protocol (UDP), which is a transport layer protocol that provides a simple and unreliable service for sending and receiving datagrams over the Internet. UDP datagrams can carry up to 65,507 bytes of data, and have a header of 8 bytes. UDP datagrams are often encapsulated in IP packets, which are another example of datagrams at the network layer. IP packets can carry up to 65,535 bytes of data, and have a header of 20 bytes. IP packets are the basic unit of data exchange in the Internet Protocol (IP), which is the main protocol for routing data across the Internet.  

Here is an example of how to create and send a UDP datagram in Java, using the `java.net.DatagramSocket` and `java.net.DatagramPacket` classes:

```java
// Create a datagram socket
DatagramSocket socket = new DatagramSocket();

// Create a byte array to store the data to be sent
byte[] data = "Hello, world!".getBytes();

// Create a datagram packet with the data, the destination address, and the destination port
InetAddress address = InetAddress.getByName("example.com");
int port = 1234;
DatagramPacket packet = new DatagramPacket(data, data.length, address, port);

// Send the datagram packet
socket.send(packet);

// Close the datagram socket
socket.close();
```