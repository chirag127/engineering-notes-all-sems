### File Transfer Protocol in Application Layer

- File Transfer Protocol (FTP) is an application layer protocol that is used to transfer files between local and remote file systems over the Internet .
- FTP runs on top of TCP, which provides reliable and ordered delivery of data packets .
- FTP uses two TCP connections in parallel to transfer a file: a control connection and a data connection .
- The control connection is used to exchange commands and responses between the FTP client and the FTP server .
- The data connection is used to transfer the actual file data between the FTP client and the FTP server .
- The control connection remains open throughout the FTP session, while the data connection is opened and closed for each file transfer .
- FTP supports both text and binary files, and can handle different types of file systems and end-of-line characters .
- FTP requires the user to authenticate with a username and password before accessing the files on the server .
- FTP uses a plaintext (unencrypted) sign-in process, which makes it vulnerable to eavesdropping and spoofing attacks .
- FTP can be secured by using encryption protocols such as SSL/TLS or SSH .