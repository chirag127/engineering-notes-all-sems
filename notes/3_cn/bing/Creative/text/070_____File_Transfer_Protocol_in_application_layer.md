### File Transfer Protocol in Application Layer

- File Transfer Protocol (FTP) is an application layer protocol that is used to transfer the files between the local devices (PC, smartphone, etc.) to a server .
- It transfers both text and binary files over the Internet.
- It runs on the top of TCP, like HTTP .
- To transfer a file, 2 TCP connections are used by FTP in parallel: control connection and data connection .
- Control connection is used for sending commands and receiving replies between the client and the server .
- Data connection is used for transferring the actual files between the client and the server .
- Control connection remains open throughout the FTP session, while data connection is opened and closed for each file transfer .
- FTP uses port number 21 for control connection and port number 20 for data connection .
- FTP supports two modes of data transfer: active mode and passive mode .
- In active mode, the server initiates the data connection to the client after receiving the client's IP address and port number .
- In passive mode, the client initiates the data connection to the server after receiving the server's IP address and port number .
- Passive mode is preferred when the client is behind a firewall or a NAT device .
- FTP requires the user to authenticate with a username and a password before accessing the server's files .
- FTP uses plaintext (unencrypted) sign-in process, which makes it vulnerable to eavesdropping and hacking .
- FTP can be secured by using encryption protocols such as FTPS (FTP over SSL/TLS) or SFTP (SSH File Transfer Protocol) .