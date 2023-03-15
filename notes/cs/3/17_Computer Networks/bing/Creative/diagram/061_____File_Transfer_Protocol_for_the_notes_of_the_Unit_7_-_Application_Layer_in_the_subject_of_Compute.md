### File Transfer Protocol

- File Transfer Protocol (FTP) is a standard communication protocol used for the transfer of computer files from a server to a client on a computer network.
- FTP is built on a client–server model architecture using separate control and data connections between the client and the server.
- The original specification for FTP was written by Abhay Bhushan in 1971.
- FTP exchanges data using two separate channels known as the command channel to authenticate the user, and the data channel to transfer the files.
- FTP can be used within an internal network of computers, or online between different web servers.
- FTP can transfer multiple files simultaneously.
- FTP requires an Internet connection to execute file transfers.
- FTP supports both active and passive modes of data transfer.
  - In active mode, the client starts listening for incoming data connections from the server on a port specified by the client.
  - In passive mode, the client initiates both the control and data connections to the server, and the server passively listens for the connections.
- FTP uses plain text to transmit user credentials and data, which makes it vulnerable to eavesdropping and tampering.
- FTP can be secured by using encryption methods such as SSL/TLS or SSH .
  - SSL/TLS (Secure Sockets Layer/Transport Layer Security) is a protocol that encrypts the data and provides authentication and integrity checks.
  - SSH (Secure Shell) is a protocol that encrypts the data and provides authentication and integrity checks, as well as compression and tunneling .
  - SFTP (SSH File Transfer Protocol) is a network protocol that provides file access, file transfer, and file management over any reliable data stream, using SSH as the underlying protocol.