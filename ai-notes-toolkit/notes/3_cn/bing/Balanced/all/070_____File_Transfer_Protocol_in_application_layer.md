### File Transfer Protocol in application layer

- File Transfer Protocol (FTP) is an application layer protocol that is used to transfer files between local and remote file systems over the Internet .
- FTP runs on top of TCP, which provides reliable and ordered delivery of data packets .
- FTP uses two TCP connections in parallel to transfer a file: a control connection and a data connection .
- The control connection is used to exchange commands and responses between the FTP client and the FTP server . It remains open throughout the entire FTP session .
- The data connection is used to transfer the actual file data between the FTP client and the FTP server . It is opened and closed for each file transfer .
- FTP supports both text and binary files, and can handle different types of file systems and end-of-line characters .
- FTP requires the user to authenticate with a username and password before accessing the server's files . The authentication process is done in plaintext, which means it is not secure and can be intercepted by attackers .
- FTP can operate in two modes: active mode and passive mode . In active mode, the FTP client initiates the data connection to the FTP server. In passive mode, the FTP server initiates the data connection to the FTP client .
- Passive mode is more common and preferred, as it can avoid firewall and NAT issues that may block the data connection in active mode .
- FTP is widely used for uploading and downloading files from web servers, sharing files among users, and backing up data .

#### Mnemonics and learning tricks

- To remember the difference between active and passive mode, you can use the following mnemonic: **A**ctive mode = **A**sk for data connection, **P**assive mode = **P**rovide data connection.
- To remember the port numbers used by FTP, you can use the following trick: FTP uses port **21** for the control connection and port **20** for the data connection. The numbers **21** and **20** are in reverse order, just like the letters **F** and **T** in FTP.
- To remember the commands and responses used by FTP, you can use the following table:

| Command | Description | Response |
| --- | --- | --- |
| USER | Sends the username | 331: User name okay, need password |
| PASS | Sends the password | 230: User logged in |
| CWD | Changes the working directory | 250: Requested file action okay |
| LIST | Lists the files in the current directory | 150: File status okay; about to open data connection |
| RETR | Retrieves a file from the server | 150: File status okay; about to open data connection |
| STOR | Stores a file on the server | 150: File status okay; about to open data connection |
| QUIT | Terminates the FTP session | 221: Service closing control connection |