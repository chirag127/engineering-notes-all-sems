#### TCP/IP Client Sockets in Networking

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet.
- A socket can be used to connect Java’s I/O system to other programs that may reside either on the local machine or on any other machine on the Internet.
- A TCP socket is defined by the IP address of the machine and the port it uses. The IP address identifies the host, and the port number identifies the service on the host.
- The TCP socket guarantees that all data is received and acknowledged, and that the data is delivered in the same order as it was sent.
- To create a TCP client socket in Java, you need to do the following steps:
  - Import the java.net and java.io packages.
  - Create an instance of the Socket class by specifying the host name and port number of the server.
  - Obtain the input and output streams of the socket using the getInputStream() and getOutputStream() methods.
  - Perform read and write operations on the streams using the methods of the java.io classes, such as BufferedReader, PrintWriter, DataInputStream, DataOutputStream, etc.
  - Close the socket and the streams when the communication is over using the close() method.
- A simple example of a TCP client socket in Java is shown below:

```java
import java.net.*;
import java.io.*;

public class TCPClient {
  public static void main(String[] args) {
    // The host name and port number of the server
    String host = "www.example.com";
    int port = 80;

    try {
      // Create a socket object
      Socket socket = new Socket(host, port);

      // Obtain the input and output streams of the socket
      InputStream in = socket.getInputStream();
      OutputStream out = socket.getOutputStream();

      // Send a request to the server
      PrintWriter writer = new PrintWriter(out, true);
      writer.println("GET / HTTP/1.1");
      writer.println("Host: " + host);
      writer.println();

      // Receive the response from the server
      BufferedReader reader = new BufferedReader(new InputStreamReader(in));
      String line;
      while ((line = reader.readLine()) != null) {
        System.out.println(line);
      }

      // Close the socket and the streams
      socket.close();
      in.close();
      out.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

- A possible mnemonic to remember the steps of creating a TCP client socket in Java is: **SIPROC** (Socket, Input, Output, Read, Write, Close).
- Some advantages of using TCP sockets are :
  - They provide reliable and ordered data delivery, ensuring that no data is lost or corrupted.
  - They support flow control and congestion control, adjusting the data rate according to the network conditions.
  - They support full-duplex communication, allowing data to be sent and received simultaneously.
- Some disadvantages of using TCP sockets are :
  - They introduce more overhead and latency, due to the additional features such as acknowledgments, retransmissions, and handshakes.
  - They are not suitable for real-time applications, such as voice or video streaming, where some data loss or reordering is acceptable.
  - They consume more network resources, such as bandwidth and memory, than UDP sockets.
- Some examples of applications that use TCP sockets are :
  - Web browsers and web servers, using the HTTP protocol.
  - Email clients and servers, using the SMTP, POP3, or IMAP protocols.
  - File transfer clients and servers, using the FTP or SCP protocols.
  - Remote login clients and servers, using the Telnet or SSH protocols.
  - Database clients and servers, using the SQL or NoSQL protocols.