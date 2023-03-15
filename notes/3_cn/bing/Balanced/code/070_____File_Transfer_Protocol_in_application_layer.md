### File Transfer Protocol in Application Layer

- File Transfer Protocol (FTP) is an application layer protocol that is used to transfer files between local and remote file systems. It runs on top of TCP, like HTTP .
- FTP uses two TCP connections in parallel to transfer a file: a control connection and a data connection .
- The control connection is used to send commands and responses between the client and the server. It is established first and remains open until the end of the session .
- The data connection is used to transfer the actual file data. It is opened and closed for each file transfer. The data connection can be in one of two modes: active or passive .
- In active mode, the client sends its IP address and port number to the server using the PORT command. The server then initiates the data connection from its port 20 to the client's port .
- In passive mode, the client sends the PASV command to the server. The server responds with its IP address and a random port number. The client then initiates the data connection from any port to the server's port .
- FTP supports both text and binary files. Text files are converted to the appropriate format depending on the operating system of the client and the server. Binary files are transferred as they are without any conversion .
- FTP also supports various commands to manipulate files and directories on the server, such as LIST, RETR, STOR, DELE, MKD, RMD, etc  .
- FTP can use encryption to secure the data and control connections. There are two types of encryption: implicit and explicit.
- Implicit encryption, also known as FTPS, uses port 990 and establishes a TLS/SSL connection before any FTP commands are exchanged. It is more secure but less compatible with firewalls.
- Explicit encryption, also known as FTPES, uses port 21 and starts as a regular FTP connection. It then uses special commands to switch to a TLS/SSL connection. It is less secure but more compatible with firewalls.