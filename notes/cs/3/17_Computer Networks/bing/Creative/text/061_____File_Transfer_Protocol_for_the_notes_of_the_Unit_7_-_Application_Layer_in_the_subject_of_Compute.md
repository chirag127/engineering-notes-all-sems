### File Transfer Protocol

- File Transfer Protocol (FTP) is a standard communication protocol used for the transfer of computer files from a server to a client on a computer network.
- FTP is built on a client–server model architecture using separate control and data connections between the client and the server.
- The original specification for FTP was written by Abhay Bhushan in 1971.
- FTP exchanges data using two separate channels known as the command channel to authenticate the user, and the data channel to transfer the files.
- FTP can be used within an internal network of computers, or online between different web servers.
- FTP can transfer multiple files simultaneously.
- FTP requires an Internet connection to execute file transfers.
- FTP supports both active and passive modes of data transfer.
  - In active mode, the client starts listening for incoming data connections from the server on a specified port.
  - In passive mode, the client initiates the data connection to the server on a random port.
- FTP uses plain text to transmit user credentials and data, which makes it vulnerable to eavesdropping and tampering.
- FTP can be secured by using encryption methods such as SSL/TLS or SSH .
  - SSL/TLS (Secure Sockets Layer/Transport Layer Security) is a protocol that encrypts the data and the control channels of FTP.
  - SSH (Secure Shell) is a protocol that encrypts the data channel of FTP and uses a separate protocol called SFTP (SSH File Transfer Protocol) for the control channel .
- FTP can be accessed by using a web browser, a command-line interface, or a dedicated FTP client software.