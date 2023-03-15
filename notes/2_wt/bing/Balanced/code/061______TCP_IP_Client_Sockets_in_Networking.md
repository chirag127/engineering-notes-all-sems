#### TCP/IP Client Sockets in Networking

TCP/IP client sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet. TCP/IP sockets are based on the Transmission Control Protocol (TCP), which ensures that the data is delivered in order and without errors. TCP/IP sockets are defined by the IP address of the machine and the port number that the socket uses to communicate.

To create a TCP/IP client socket in Java, you need to do the following steps :

- Import the java.net and java.io packages, which provide classes and methods for networking and input/output operations.
- Create a Socket object by passing the IP address or hostname and the port number of the server socket that you want to connect to. This will initiate a connection request to the server and block until the connection is established or an exception is thrown.
- Get the input and output streams of the socket by calling the getInputStream() and getOutputStream() methods. These streams allow you to read and write data to and from the socket.
- Use the input and output streams to communicate with the server. You can use various classes and methods from the java.io package to read and write data in different formats, such as bytes, characters, strings, or objects.
- Close the socket by calling the close() method when you are done with the communication. This will release the resources associated with the socket and terminate the connection.

Here is an example of a TCP/IP client socket in Java that connects to a server socket running on localhost and port 8080, and sends and receives a string message:

```java
// Import the java.net and java.io packages
import java.net.*;
import java.io.*;

public class TCPClient {

    public static void main(String[] args) {

        // Declare the socket, input and output streams
        Socket socket = null;
        DataInputStream input = null;
        DataOutputStream output = null;

        try {
            // Create a socket object by passing the IP address and port number of the server
            socket = new Socket("localhost", 8080);

            // Get the input and output streams of the socket
            input = new DataInputStream(socket.getInputStream());
            output = new DataOutputStream(socket.getOutputStream());

            // Write a string message to the output stream
            output.writeUTF("Hello from the client!");

            // Read a string message from the input stream
            String message = input.readUTF();
            System.out.println("Server says: " + message);

            // Close the socket
            socket.close();

        } catch (IOException e) {
            // Handle the exception
            e.printStackTrace();
        }
    }
}
```