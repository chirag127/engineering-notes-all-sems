### TCP/IP Client Sockets

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet .
- A socket can be used to connect Java’s I/O system to other programs that may reside either on the local machine or on any other machine on the Internet.
- TCP socket is a connection-oriented socket that uses the Transmission Control Protocol (TCP).
- TCP socket is defined by the IP address of the machine and the port it uses.
- TCP socket requires three packets to set up a connection: the SYN packet, the SYN-ACK packet, and the ACK packet.
- TCP socket has built in error checking and will re transmit missing packets.
- To create a TCP client socket in Java, you need to use the `java.net.Socket` class .
- The constructor for the `Socket` class has parameters that specify the host name and the port number of the server.
- The `Socket` class provides methods to get the input and output streams of the socket, which can be used to send and receive data over TCP .
- The `Socket` class also provides methods to close the socket, check the connection status, and set or get various socket options.
- A simple example of a TCP client socket in Java is shown below:

```java
import java.io.*;
import java.net.*;

public class TCPClient {
    public static void main(String[] args) {
        try {
            // Create a socket to connect to the server
            Socket socket = new Socket("localhost", 8000);

            // Get the input and output streams of the socket
            DataInputStream input = new DataInputStream(socket.getInputStream());
            DataOutputStream output = new DataOutputStream(socket.getOutputStream());

            // Send a message to the server
            output.writeUTF("Hello from client");

            // Receive a message from the server
            String message = input.readUTF();
            System.out.println("Server says: " + message);

            // Close the socket
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```