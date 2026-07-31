# File Transfer Protocol

- File Transfer Protocol (FTP) is a standard communication protocol used for the transfer of computer files from a server to a client on a computer network.
- FTP is built on a client–server model architecture using separate control and data connections between the client and the server.
- The control connection is used to authenticate the user and send commands, while the data connection is used to transfer the files.
- FTP can operate in two modes: active and passive.
  - In active mode, the client starts listening for incoming data connections from the server on a specified port.
  - In passive mode, the client initiates both the control and data connections to the server, and the server responds with the port number for the data connection.
- FTP can transfer files in two modes: binary and ASCII.
  - In binary mode, the files are transferred as raw data, preserving the exact content and format.
  - In ASCII mode, the files are converted to a standard text format, which may cause some data loss or corruption.
- FTP can also support secure file transfer using encryption and authentication mechanisms, such as SSL/TLS or SSH .
- FTP is widely used for transferring files over the Internet and between computer systems, but it has some limitations and drawbacks, such as:
  - FTP does not encrypt the data or the credentials, making it vulnerable to eavesdropping and tampering.
  - FTP does not support resume or partial transfers, meaning that if a transfer is interrupted, it has to start from the beginning.
  - FTP does not support file synchronization, compression, or checksum verification, which can affect the performance and reliability of the transfers.
  - FTP does not support file locking, versioning, or access control, which can cause conflicts and errors when multiple users access the same files.
- FTP can be used within an internal network of computers, or online between different web servers.
- FTP makes it possible and easy to transfer multiple files simultaneously.
- FTP requires an Internet connection in order to execute FTP transfers.