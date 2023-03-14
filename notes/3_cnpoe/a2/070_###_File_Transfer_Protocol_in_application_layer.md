 Here is the content in markdown format for the topic -

### File Transfer Protocol in application layer

File Transfer Protocol (FTP) is a standard network protocol used to transfer computer files between a client and server on a computer network. FTP is built on a client-server model architecture and uses separate control and data connections between the client and the server.

Some key points about FTP are:

- FTP uses two ports - port 21 for control connection and port 20 for data connection.
- It works on the application layer of the OSI model.
- It is a plain text protocol, all commands and responses are in ASCII.
- It provides authentication using user ID and password.
- It supports two modes of data transfer - ASCII mode and binary mode. ASCII is used for text files and binary is used for image, audio, video files, etc.
- The main FTP commands are - USER, PASS, LIST, CWD, CDUP, RETR, STOR, DELE, etc.
- Active FTP mode establishes two connections whereas Passive FTP mode uses only one connection.
- Advantages - simple, efficient, widely used. Disadvantages - transmit passwords in cleartext, lacks strong security.

Some key learning tricks to remember FTP -

- Think of FTP as File Transfer over Ports (21, 20)
- USER and PASS are similar to login credentials
- LIST is to list files, CWD/CDUP is to change directory
- RETRieve and STORe are easy to map to download and upload of files
- Active FTP has two connections (extra effort), Passive has one (relaxed)

Hope this helps in learning and understanding FTP in detail. Let me know if you would like me to elaborate on any part or add more details.