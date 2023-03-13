### File Transfer Protocol in Application Layer

File Transfer Protocol (FTP) is a protocol used in the application layer of the OSI model to transfer files between hosts over a TCP-based network. FTP is widely used to exchange files between clients and servers on the internet.

#### How FTP works?

FTP uses the client-server model, where the client initiates a connection to the server and requests to transfer files. The server listens for incoming connections and responds to the client's requests. FTP uses two channels for communication between the client and server:

- **Control Channel:** The control channel is used for sending commands and responses between the client and server. The control channel uses TCP port 21.
- **Data Channel:** The data channel is used for transferring the actual file data. The data channel uses TCP port 20.

#### Mnemonics and Learning Tricks for FTP

- **File Transfer Protocol = FTP = File Transfer Party:** You can imagine FTP as a party where you transfer files between hosts.
- **FTP = For The People:** You can remember FTP as a protocol that is used for the people to transfer files over the internet.

#### Advantages of FTP

- FTP is a widely used protocol for transferring files over the internet.
- FTP provides authentication and encryption mechanisms to secure file transfers.
- FTP allows transferring large files in a reliable and efficient way.

#### Disadvantages of FTP

- FTP is an old protocol and has some security vulnerabilities.
- FTP is not suitable for transferring sensitive data over the internet.
- FTP uses two channels for communication, which can cause firewall issues.

#### Example of using FTP

Suppose you want to transfer a file from your computer to a web server. Here are the steps you need to follow:

1. Connect to the web server using an FTP client software, such as FileZilla.
2. Enter the server's hostname, username, and password in the FTP client software.
3. Navigate to the directory on the server where you want to upload the file.
4. Drag and drop the file from your computer to the FTP client software.
5. The file will be transferred to the server over the data channel.

#### Applications of FTP

- FTP is widely used in the web hosting industry to upload and manage website files.
- FTP is used by software developers to upload and download software updates.
- FTP is used by graphic designers to transfer large image files.