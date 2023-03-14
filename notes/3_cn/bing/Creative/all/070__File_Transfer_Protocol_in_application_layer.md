### File Transfer Protocol in application layer

- File Transfer Protocol (FTP) is an application layer protocol that allows users to transfer files between hosts over a network.
- FTP uses two separate TCP connections: a control connection and a data connection.
- The control connection is used to exchange commands and responses between the client and the server. The data connection is used to transfer the actual files.
- FTP follows a client-server model, where the client initiates the connection and requests files from the server.
- FTP supports both active and passive modes for establishing the data connection.
- In active mode, the client sends its IP address and port number to the server using the PORT command, and the server initiates the data connection to the client.
- In passive mode, the server sends its IP address and port number to the client using the PASV command, and the client initiates the data connection to the server.
- FTP supports both binary and ASCII modes for transferring files. Binary mode transfers the files as they are, while ASCII mode converts the files to a standard format before transferring.
- FTP supports various commands for manipulating files and directories on the server, such as LIST, RETR, STOR, DELE, MKD, RMD, etc.
- FTP also supports authentication, where the client sends its username and password to the server using the USER and PASS commands, and the server verifies them before granting access.
- FTP is widely used for uploading and downloading files from web servers, sharing files among users, and backing up data.

#### Mnemonics and learning tricks for FTP

- To remember the difference between active and passive modes, think of the acronym APAD: Active - Port, Passive - Pasv.
- To remember the difference between binary and ASCII modes, think of the acronym BAIT: Binary - As Is, ASCII - Translated.
- To remember some of the common FTP commands, think of the acronym LRSMD: List, Retrieve, Store, Make, Delete.