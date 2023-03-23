

### File Transfer Protocol

File Transfer Protocol (FTP) is an application layer protocol used to transfer files over the internet. It is a standard protocol that is widely used for downloading and uploading files from a remote server to a local machine.

#### Features of FTP

Here are some of the key features of FTP:

- FTP allows users to transfer files between two computers over the internet.

- It uses a client-server model, where the client requests files from the server and the server responds by sending the requested files.

- FTP supports two modes of data transfer: ASCII and binary.

- ASCII mode is used for transferring text files, while binary mode is used for transferring non-text files such as images, videos, and compressed files.

- FTP uses two channels for communication: the control channel and the data channel.

- The control channel is used for sending commands and receiving responses between the client and server, while the data channel is used for transferring files.

#### FTP Commands

FTP uses a set of commands to interact with the server. Some of the commonly used commands are:

- **USER**: This command is used to specify the username to login to the server.

- **PASS**: This command is used to specify the password to login to the server.

- **LIST**: This command is used to list the files and directories on the remote server.

- **CWD**: This command is used to change the current working directory on the remote server.

- **PWD**: This command is used to display the current working directory on the remote server.

- **RETR**: This command is used to retrieve a file from the remote server.

- **STOR**: This command is used to store a file on the remote server.

#### FTP Modes

FTP supports two modes of operation: active mode and passive mode.

- **Active mode**: In this mode, the client initiates a connection to the server on port 21, and the server responds by establishing a data channel on port 20.

- **Passive mode**: In this mode, the client initiates a connection to the server on port 21, and the server responds by providing a port number on which the client can establish a data channel.

#### Security in FTP

FTP is not a secure protocol and is vulnerable to various attacks such as eavesdropping, data tampering, and password sniffing. To add security to FTP, Secure FTP (SFTP) and FTP over SSL/TLS (FTPS) have been developed.

#### Conclusion

FTP is a widely used protocol for transferring files over the internet. It supports two modes of data transfer, two modes of operation, and a set of commands to interact with the server. However, it is not a secure protocol, and SFTP and FTPS have been developed to add security to FTP.