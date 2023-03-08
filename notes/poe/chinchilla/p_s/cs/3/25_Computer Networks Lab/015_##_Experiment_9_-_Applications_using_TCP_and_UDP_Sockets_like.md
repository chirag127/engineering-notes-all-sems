## Experiment 9 - Applications using TCP and UDP Sockets like

In this experiment, we will study the applications that use TCP and UDP sockets. These applications are widely used in the field of networking and are important for communication between different devices.

### TCP Socket Applications

TCP sockets are used in applications that require reliable and ordered data transmission. Some of the common applications that use TCP sockets are:

- Web Browsing: When we access a website, our computer establishes a TCP connection with the web server to request and receive the web page.
- File Transfer: Applications such as FTP, SFTP, and SCP use TCP sockets for transferring files between two devices.
- Email: Email clients use TCP sockets to connect with the email server and retrieve or send emails.

### UDP Socket Applications

UDP sockets are used in applications that require fast and non-reliable data transmission. Some of the common applications that use UDP sockets are:

- Gaming: Online multiplayer games use UDP sockets for fast and real-time data transmission between players.
- Video Streaming: Applications such as YouTube and Netflix use UDP sockets for streaming videos to users.
- DNS: Domain Name System (DNS) uses UDP sockets for resolving domain names into IP addresses.

#### Advantages of TCP Sockets

- Reliable: TCP sockets ensure that all data is transmitted and received without any loss or corruption.
- Ordered: Data is transmitted in the order it was sent, ensuring that the receiver receives the data in the correct sequence.
- Error Detection: TCP has built-in error detection and correction mechanisms, which reduces the chance of data corruption.

#### Disadvantages of TCP Sockets

- Slow: TCP sockets are slower than UDP sockets due to the overhead of error detection and correction mechanisms.
- Overhead: TCP sockets have a higher overhead than UDP sockets, which means it uses more resources.

#### Advantages of UDP Sockets

- Fast: UDP sockets are faster than TCP sockets due to the lack of error detection and correction mechanisms.
- Low Overhead: UDP sockets have a lower overhead than TCP sockets, which means it uses fewer resources.

#### Disadvantages of UDP Sockets

- Unreliable: UDP sockets do not guarantee that all data is transmitted and received without any loss or corruption.
- No Order: Data is transmitted in whatever order it was sent, which means the receiver may receive the data in a different sequence.

In conclusion, TCP and UDP sockets are important for communication between different devices in a network. Each has its advantages and disadvantages, and the choice of which socket to use depends on the specific application requirements.