## Unit 5 - Application Layer in Computer Networks

- The application layer is the highest layer in the protocol suite. It provides services to the user and interacts with network applications  .
- Examples of network applications are web browsers, chat clients, email clients, file transfer, remote login, etc .
- The application layer uses a logical connection, which means that the two application layers assume that there is an imaginary direct connection between them.
- The application layer can use different paradigms for communication, such as client-server, peer-to-peer, or hybrid.
- Client-server paradigm: The service provider is an application program called the server process, and the service requester is another application program called the client process. The server is usually passive and waits for requests from clients, while the client is usually active and initiates the communication. Examples of client-server applications are web, email, FTP, etc.
- Peer-to-peer paradigm: The service provider and the service requester are both application programs running on different peers, which are computers that are not dedicated to be either a client or a server. The peers communicate directly with each other without using a dedicated server. Examples of peer-to-peer applications are file sharing, voice over IP, etc.
- Hybrid paradigm: The service provider and the service requester are both application programs running on different peers, but they also use some servers for coordination or indexing purposes. Examples of hybrid applications are BitTorrent, Skype, etc.
- The application layer protocols define the rules and formats for exchanging messages between applications . They also specify the syntax and semantics of the messages, such as the type, length, order, and meaning of the fields.
- Some common application layer protocols are:

| Protocol | Description | Port number |
| -------- | ----------- | ----------- |
| HTTP | Hypertext Transfer Protocol. It is used to transfer web pages from a web server to a web browser. | 80 |
| HTTPS | Hypertext Transfer Protocol Secure. It is a secure version of HTTP that uses encryption and authentication. | 443 |
| FTP | File Transfer Protocol. It is used to transfer files between a client and a server. | 20 (data), 21 (control) |
| SMTP | Simple Mail Transfer Protocol. It is used to send email messages from a sender to a receiver. | 25 |
| POP3 | Post Office Protocol version 3. It is used to retrieve email messages from a mail server to a mail client. | 110 |
| IMAP | Internet Message Access Protocol. It is used to access and manipulate email messages on a mail server. | 143 |
| DNS | Domain Name System. It is used to translate domain names into IP addresses. | 53 |
| DHCP | Dynamic Host Configuration Protocol. It is used to assign IP addresses and other network parameters to hosts. | 67 (server), 68 (client) |
| SNMP | Simple Network Management Protocol. It is used to monitor and manage network devices. | 161 |

- A mnemonic to remember some of the application layer protocols and their port numbers is:

**H**ave **F**un **S**ending **M**ail **P**ostcards **I**n **D**ifferent **S**tyles

HTTP (80), FTP (20, 21), SMTP (25), POP3 (110), IMAP (143), DNS (53), DHCP (67, 68), SNMP (161)