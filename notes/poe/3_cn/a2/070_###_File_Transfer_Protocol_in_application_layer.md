 Here is the content written in markdown format for the topic ### File Transfer Protocol in application layer:

### File Transfer Protocol in application layer

FTP or File Transfer Protocol is a standard network protocol used to transfer computer files between a client and server on a computer network. FTP is built on a client-server model architecture and uses separate control and data connections between the client and the server.

**Key points to remember:**

1. FTP uses two connections: one for control and one for data. The control connection is used to communicate commands and responses between the FTP client and server. The data connection is used for the actual file transfers.

2. FTP is an application layer protocol that runs on top of the Transport Control Protocol (TCP). It transfers files as byte streams without formatting the data.

3. The FTP client can download files from the server or upload files to the server. The transfer mode can be either ASCII or binary. In ASCII mode, files are transferred in text format while in binary mode the files are transferred as is without any conversion.

4. The client authenticates itself to the server using a username and password. The server then determines what resources the client can access based on the credentials.

5. Some common FTP commands are: `GET` to download a file, `PUT` to upload a file, `PWD` to print the current directory, `CD` to change directory, `LS` to list files, etc.

**Mnemonics:**

- FTP has control connection and data connection
- FTP uses TCP and transfers files as byte streams
- FTP can upload or download files in ASCII or binary mode
- FTP uses username and password for authentication and access control

**Advantages:** Simple to use, widely supported, efficient for transferring large files.
**Disadvantages:** Transfers files with no formatting, no strong security, passwords sent in cleartext.

**Applications:** File sharing, website deployment, software distribution, etc.

[Diagrams and examples can be added here for better understanding]