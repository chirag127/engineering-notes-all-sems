### File Transfer Protocol

- File Transfer Protocol (FTP) is a standard communication protocol used for the transfer of computer files from a server to a client on a computer network.
- FTP is built on a client–server model architecture using separate control and data connections between the client and the server.
- The control connection is used to authenticate the user and send commands, while the data connection is used to transfer the files.
- FTP can operate in two modes: active and passive.
  - In active mode, the client starts listening for incoming data connections from the server on a specified port.
  - In passive mode, the client initiates both the control and data connections to the server, and the server responds with the port number for the data connection.
- FTP can transfer files in two modes: binary and ASCII.
  - In binary mode, the files are transferred as raw bytes, which preserves the exact content of the files.
  - In ASCII mode, the files are converted to a standard text format, which may alter the content of the files depending on the encoding and line endings.
- FTP can also support various extensions and features, such as encryption, compression, resume, and append.
- FTP is one of the oldest and most widely used file transfer protocols, but it has some limitations and security risks .
  - FTP does not encrypt the data or the credentials, which makes it vulnerable to eavesdropping and tampering .
  - FTP does not verify the integrity of the files, which may result in corrupted or incomplete transfers .
  - FTP does not support file synchronization, which may cause conflicts or inconsistencies between the source and the destination .
- To overcome these issues, various alternatives and enhancements to FTP have been developed, such as Secure FTP (SFTP), FTP Secure (FTPS), and Web Distributed Authoring and Versioning (WebDAV)  .
  - SFTP is a network protocol that provides file access, file transfer, and file management over any reliable data stream, such as Secure Shell (SSH).
  - FTPS is an extension of FTP that adds support for Transport Layer Security (TLS) or Secure Sockets Layer (SSL) encryption.
  - WebDAV is an extension of the Hypertext Transfer Protocol (HTTP) that allows clients to perform remote web content authoring operations.