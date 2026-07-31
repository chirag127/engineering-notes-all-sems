# File Transfer Protocol

- File Transfer Protocol (FTP) is a standard communication protocol used for the transfer of computer files from a server to a client on a computer network.
- FTP is built on a client–server model architecture using separate control and data connections between the client and the server.
- The control connection is used to authenticate the user and send commands, while the data connection is used to transfer the files.
- FTP can operate in two modes: active and passive.
  - In active mode, the client starts listening for incoming data connections from the server on a specified port.
  - In passive mode, the client initiates both the control and data connections to the server, and the server responds with the port number for the data connection.
- FTP can transfer files in two modes: binary and ASCII.
  - In binary mode, the files are transferred as raw bytes, preserving the exact content and format of the files.
  - In ASCII mode, the files are converted to a standard text format, which may alter the content and format of the files.
- FTP can also support various commands for file access, file transfer, and file management, such as list, rename, delete, append, etc.
- FTP is widely used for transferring files over the Internet and between computer systems, but it has some limitations and security risks .
  - FTP does not encrypt the data or the credentials, making them vulnerable to interception and tampering .
  - FTP does not support resume or pause of file transfers, which can cause problems for large or interrupted transfers .
  - FTP does not support compression or encryption of file transfers, which can affect the performance and security of the transfers .
- To overcome some of the limitations and risks of FTP, other file transfer protocols have been developed, such as Secure File Transfer Protocol (SFTP), which uses SSH to encrypt the data and the credentials.