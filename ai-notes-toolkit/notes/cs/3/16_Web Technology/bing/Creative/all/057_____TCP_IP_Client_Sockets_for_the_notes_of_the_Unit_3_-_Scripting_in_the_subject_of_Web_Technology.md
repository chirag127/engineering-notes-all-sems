# TCP/IP Client Sockets

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet .
- A socket can be used to connect Java’s I/O system to other programs that may reside either on the local machine or on any other machine on the Internet.
- TCP socket is defined by the IP address of the machine and the port it uses.
- A port is a 16-bit number that identifies a specific process or service on a host.
- TCP socket is connection-oriented, which means it requires three packets to set up a connection: the SYN packet, the SYN-ACK packet, and the ACK packet.
- TCP socket has built-in error checking and will retransmit missing packets.
- To create a TCP client socket in Java, we need to use the following steps  :
  - Import the java.net and java.io packages.
  - Create an instance of the Socket class by passing the host name and port number of the server as arguments to the constructor.
  - Get the input and output streams of the socket by calling the getInputStream() and getOutputStream() methods.
  - Use the input and output streams to read and write data to and from the server.
  - Close the socket by calling the close() method.
- An example of a TCP client socket in Java is shown below:

```java
import java.net.*;
import java.io.*;

public class TCPClient {

    public static void main(String[] args) {
        // host name and port number of the server
        String host = "localhost";
        int port = 8080;

        try {
            // create a socket object
            Socket socket = new Socket(host, port);

            // get the input and output streams of the socket
            DataInputStream input = new DataInputStream(socket.getInputStream());
            DataOutputStream output = new DataOutputStream(socket.getOutputStream());

            // send a message to the server
            output.writeUTF("Hello from client");

            // receive a message from the server
            String message = input.readUTF();
            System.out.println("Server says: " + message);

            // close the socket
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```