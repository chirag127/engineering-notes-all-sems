### File Transfer Protocol in application layer

- File Transfer Protocol (FTP) is an application layer protocol that is used to transfer files between local and remote devices over the Internet .
- FTP runs on top of TCP, which provides reliable and ordered delivery of data packets .
- FTP uses two parallel TCP connections for each file transfer: a control connection and a data connection  .
- The control connection is used to exchange commands and responses between the FTP client and the FTP server. It remains open throughout the file transfer session .
- The data connection is used to transfer the actual file data between the FTP client and the FTP server. It is opened and closed for each file transfer .
- FTP supports both text and binary files, and can handle different types of file systems and formats .
- FTP requires a plaintext (unencrypted) sign-in process, which involves a username and a password. This makes FTP vulnerable to eavesdropping and unauthorized access .
- FTP can operate in two modes: active mode and passive mode. In active mode, the FTP client initiates both the control and data connections. In passive mode, the FTP client initiates the control connection, but the FTP server initiates the data connection .
- FTP can be used for various applications, such as uploading and downloading files, updating websites, backing up data, transferring large files, and sharing files among users.
- FTP best practices include using secure FTP (SFTP) or FTP over SSL (FTPS) to encrypt the data and sign-in process, choosing strong passwords, limiting the number of concurrent connections, restricting the access permissions, and scanning the files for malware.