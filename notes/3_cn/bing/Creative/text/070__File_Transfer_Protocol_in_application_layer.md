### File Transfer Protocol in application layer

- File Transfer Protocol (FTP) is an application layer protocol that is used to transfer the files between the local devices (PC, smartphone, etc.) to a server. It transfers both text and binary files over the Internet.
- FTP runs on the top of TCP, like HTTP. To transfer a file, 2 TCP connections are used by FTP in parallel: control connection and data connection.
- Control connection is used for sending control information like user identification, password, commands to change the remote directory, commands to retrieve and store files, etc. The control connection is initiated on port number 21.
- Data connection is used for sending the actual file. A data connection is initiated on port number 20. Only one file can be sent over one data connection. But the control connection remains active throughout the user session.
- FTP sends the control information out-of-band as it uses a separate control connection. Some protocols send their request and response header lines and the data in the same TCP connection. For this reason, they are said to send their control information in-band. HTTP and SMTP are such examples.
- FTP needs to maintain a state about its user throughout the session. It allows three types of data structures: file structure, record structure, and page structure.
- FTP supports several commands for file transfer and management. Some of the FTP commands are: USER, PASS, CWD, RMD, MKD, PWD, RETR, STOR, LIST, etc.
- FTP has some security weaknesses as it uses plaintext (unencrypted) sign-in process. To overcome this, FTP can be used with secure sockets layer (SSL) or transport layer security (TSL) protocols to encrypt the data and user credentials. This is called FTP Secure (FTPS) or FTP Secure Sockets Layer (SSL).
- FTP can also use Secure Shell (SSH) protocol to encrypt the data and user credentials. This is called Secure File Transfer Protocol (SFTP) or SSH File Transfer Protocol.
- FTP can also use Hypertext Transfer Protocol Secure (HTTPS) protocol to encrypt the data and user credentials. This is called Web Distributed Authoring and Versioning (WebDAV) or HTTP File Transfer Protocol.