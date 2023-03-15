### File Transfer Protocol in application layer

- File Transfer Protocol (FTP) is a standard network protocol used to transfer files from one host to another over a TCP-based network, such as the Internet.
- FTP is built on a client-server architecture and uses separate control and data connections between the client and the server.
- FTP users may authenticate themselves with a clear-text sign-in protocol, normally in the form of a username and password, but can connect anonymously if the server is configured to allow it.
- FTP is defined by RFC 959, which was published in October 1985.
- FTP is an application layer protocol, which means it operates at the top layer of the OSI model, the application layer.
- FTP is commonly used to transfer files between a local computer and a remote server, or between two remote servers.
- FTP can be used to transfer files of any size and type, including text, binary, and multimedia files.
- FTP can be used in active or passive mode. In active mode, the client opens a port and listens, and the server actively connects to it. In passive mode, the server opens a port and listens, and the client actively connects to it.
- FTP can be secured with SSL/TLS, which adds a layer of encryption to the data being transferred.
- FTP has several commands, including `USER` (to specify the username), `PASS` (to specify the password), `CWD` (to change the working directory), `RETR` (to retrieve a file), `STOR` (to store a file), and `LIST` (to list the contents of a directory).
- FTP has some limitations, including the fact that it is not firewall-friendly, it sends login credentials in clear text, and it does not support file synchronization or delta transfers.
- FTP can be used with a variety of FTP clients, including command-line clients, graphical clients, and web-based clients.
- FTP is still widely used, but has largely been replaced by more secure and versatile protocols such as SFTP (Secure File Transfer Protocol) and SCP (Secure Copy Protocol).