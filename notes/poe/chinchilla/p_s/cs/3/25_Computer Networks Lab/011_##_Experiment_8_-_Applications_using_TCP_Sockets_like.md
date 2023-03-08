## Experiment 8 - Applications using TCP Sockets like

TCP (Transmission Control Protocol) is a widely used protocol for transmitting data over the internet. It provides reliable, ordered, and error-checked delivery of data between applications, making it ideal for applications that require high reliability, such as email, file transfer, and web browsing.

In this experiment, we will explore some of the applications that use TCP sockets and learn about their implementations. Here are the topics that we will cover:

1. Chat Application using TCP sockets
    - In this application, clients connect to a server using TCP sockets and can send messages to each other.
    - The server acts as a mediator and relays the messages between clients.
    - The implementation involves creating a server socket that listens for incoming connections, accepting client connections, and handling multiple client connections concurrently.
    - This application is commonly used in online chat rooms and instant messaging services.

2. File Transfer Application using TCP sockets
    - This application allows users to transfer files between computers over a network using TCP sockets.
    - The implementation involves creating a client socket that connects to a server socket, sending the file data in chunks, and handling errors or timeouts.
    - This application is commonly used in file-sharing services and remote file access applications.

3. Email Application using TCP sockets
    - This application allows users to send and receive emails over the internet using TCP sockets.
    - The implementation involves establishing a connection to the email server, sending email data in a specific format, and handling email delivery errors and responses.
    - This application is commonly used in email clients such as Microsoft Outlook and Gmail.

4. Web Browsing Application using TCP sockets
    - This application allows users to browse web pages over the internet using TCP sockets.
    - The implementation involves creating a client socket that connects to a web server, sending HTTP requests, and receiving HTTP responses.
    - This application is commonly used in web browsers such as Google Chrome and Mozilla Firefox.

Advantages of using TCP sockets:

- Reliable data transmission: TCP ensures that data is delivered without errors or loss.
- Ordered data delivery: TCP ensures that data is delivered in the same order it was sent.
- Flow control: TCP regulates the amount of data that can be sent at a time to prevent network congestion.
- Error checking: TCP includes error checking mechanisms to ensure data integrity.
- Multiplexing: TCP allows multiple connections to be established on the same port, enabling multiple applications to use the same network resources.

Disadvantages of using TCP sockets:

- Overhead: TCP adds additional data to each message to ensure reliability and ordering, which can increase network traffic and overhead.
- Latency: TCP can introduce latency due to its error checking and flow control mechanisms.
- Complexity: TCP is a complex protocol that requires careful implementation to ensure proper functionality.

Examples of TCP applications:

- FTP (File Transfer Protocol): Used for transferring files between computers.
- SMTP (Simple Mail Transfer Protocol): Used for sending email messages over the internet.
- HTTP (Hypertext Transfer Protocol): Used for browsing web pages over the internet.
- Telnet: Used for remote login to a computer over a network.

In conclusion, TCP sockets are essential for many applications that require reliable and ordered data transmission over a network. Understanding the implementation and use of TCP sockets is crucial for building networked applications that can function effectively and efficiently.