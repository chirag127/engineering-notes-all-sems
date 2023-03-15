### File Transfer Protocol in application layer

- File Transfer Protocol (FTP) is an application layer protocol that is used to transfer the files between the local devices (PC, smartphone, etc.) to a server. It transfers both text and binary files over the Internet.
- FTP runs on the top of TCP, like HTTP. To transfer a file, 2 TCP connections are used by FTP in parallel: control connection and data connection.
- Control connection: It is used to send commands from the client to the server and receive replies from the server. It is established between the client port 21 and the server port 21. It remains open throughout the FTP session.
- Data connection: It is used to send the actual file data from the server to the client. It is established between the client port 20 and the server port 20. It is opened and closed for each file transfer.
- FTP uses two modes of operation: active mode and passive mode. In active mode, the server initiates the data connection to the client. In passive mode, the client initiates the data connection to the server.
- FTP supports three types of file transfer: ASCII mode, binary mode, and auto mode. ASCII mode is used to transfer text files, binary mode is used to transfer binary files, and auto mode is used to automatically detect the file type and choose the appropriate mode.
- FTP supports four types of file access: anonymous, basic, account, and secure. Anonymous access allows anyone to log in to the server without a username and password. Basic access requires a username and password to log in to the server. Account access requires a username, password, and an account name to log in to the server. Secure access requires a username, password, and an encryption method to log in to the server.
- FTP supports various commands to manipulate files and directories on the server, such as LIST, RETR, STOR, DELE, MKD, RMD, etc.
- FTP is widely used for uploading and downloading files from web servers, sharing files among users, and backing up data to remote servers.
- FTP has some limitations and drawbacks, such as lack of encryption, firewall issues, bandwidth consumption, and file size restrictions.

#### Mnemonics and learning tricks

- To remember the port numbers of FTP, you can use the following mnemonic: FTP uses **21** to control and **20** to send data.
- To remember the modes of FTP, you can use the following acronym: FTP can be **A**ctive or **P**assive.
- To remember the types of file transfer, you can use the following acronym: FTP can transfer files in **A**SCII, **B**inary, or **A**uto mode.
- To remember the types of file access, you can use the following acronym: FTP can access files **A**nonymously, **B**asically, with an **A**ccount, or **S**ecurely.