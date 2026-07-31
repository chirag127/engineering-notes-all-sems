# TCP/IP Client Sockets

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet .
- A socket can be used to connect Java’s I/O system to other programs that may reside either on the local machine or on any other machine on the Internet.
- TCP socket is defined by the IP address of the machine and the port it uses.
- A port is a 16-bit number that identifies a specific application or service on a host.
- TCP socket is connection-oriented, which means it requires three packets to set up a connection: the SYN packet, the SYN-ACK packet, and the ACK packet.
- TCP socket also has built-in error checking and will retransmit missing packets.
- To create a TCP client socket in Java, we need to use the following steps :
  - Import the java.net and java.io packages.
  - Create an instance of the Socket class by passing the host name and port number of the server as arguments to the constructor.
  - Obtain the input and output streams of the socket by calling the getInputStream() and getOutputStream() methods.
  - Use the input and output streams to communicate with the server using the read() and write() methods.
  - Close the socket by calling the close() method.
- An example of a TCP client socket in Java is shown below:

```java
import java.net.*;
import java.io.*;

public class TCPClient {
  public static void main(String[] args) {
    // host name and port number of the server
    String host = "www.example.com";
    int port = 80;

    try {
      // create a socket and connect to the server
      Socket socket = new Socket(host, port);

      // obtain the input and output streams of the socket
      InputStream in = socket.getInputStream();
      OutputStream out = socket.getOutputStream();

      // send a request to the server
      String request = "GET / HTTP/1.1\r\nHost: " + host + "\r\n\r\n";
      out.write(request.getBytes());

      // read the response from the server
      byte[] buffer = new byte[1024];
      int n;
      while ((n = in.read(buffer)) != -1) {
        System.out.write(buffer, 0, n);
      }

      // close the socket
      socket.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```