### Protocols Governing Web

Protocols are a set of rules that govern the communication and exchange of data over the internet. Both the sender and receiver should follow the same protocols in order to communicate the data. Protocols are necessary to manage the flow control, access control, error detection, and security of the data transmission.

The web is a massive network of webpages, programs, and files that are accessible via URLs. The web is just one of the applications built on top of the internet protocols, but it is by far the most popular. The web browser loads a webpage using various protocols, such as:

- **DNS (Domain Name System)**: This protocol converts a domain name into an IP address. For example, www.google.com is converted into 142.250.74.196. This allows the web browser to locate the server that hosts the webpage. DNS is also used to provide other information about the domain, such as its mail servers, name servers, and security certificates.
- **HTTP (Hypertext Transfer Protocol)**: This protocol defines how the web browser and the web server communicate with each other. The web browser sends an HTTP request to the web server, asking for a specific resource, such as a webpage, an image, or a file. The web server responds with an HTTP response, which contains the status code, the headers, and the body of the resource. HTTP is a stateless protocol, which means that each request and response are independent and do not keep track of the previous interactions.
- **TLS (Transport Layer Security)**: This protocol provides a secure and encrypted connection between the web browser and the web server. TLS ensures that the data exchanged over the web is protected from eavesdropping, tampering, and forgery. TLS is often used in conjunction with HTTP, forming HTTPS (Hypertext Transfer Protocol Secure). HTTPS is indicated by a padlock icon in the web browser's address bar.

These protocols are built on top of the internet protocols, such as:

- **IP (Internet Protocol)**: This protocol defines how the data packets are routed across the internet. Each data packet contains the source and destination IP addresses, as well as other information, such as the time to live, the protocol type, and the checksum. IP is a connectionless protocol, which means that it does not guarantee the delivery, order, or integrity of the data packets. IP relies on other protocols, such as TCP, to provide these features.
- **TCP (Transmission Control Protocol)**: This protocol provides a reliable and ordered delivery of data packets over the internet. TCP establishes a connection between the sender and the receiver, and divides the data into segments. Each segment contains a sequence number, an acknowledgment number, and a checksum. TCP ensures that the segments are delivered in order, without errors, and without duplication. TCP also controls the flow of data, by adjusting the window size and the congestion window.

There are many other protocols that are used for different purposes on the web, such as:

- **SMTP (Simple Mail Transfer Protocol)**: This protocol is used for sending and distributing outgoing emails. SMTP defines how the email messages are formatted, encoded, and transferred between the mail servers and the mail clients.
- **FTP (File Transfer Protocol)**: This protocol is used for transferring files between a client and a server. FTP allows the client to browse, upload, download, rename, and delete files on the server. FTP can use either TCP or UDP as the underlying transport protocol.
- **POP (Post Office Protocol)**: This protocol is used for retrieving emails from a mail server. POP allows the client to download and delete the messages from the server. POP is often used in conjunction with SMTP, forming a mail delivery system.
- **IMAP (Internet Message Access Protocol)**: This protocol is used for accessing and managing emails on a mail server. IMAP allows the client to synchronize the messages with the server, and to perform various operations, such as searching, sorting, and flagging. IMAP is more advanced and flexible than POP, as it allows the client to access multiple mailboxes and folders on the server.

Some mnemonics and learning tricks for the protocols governing the web are:

- **DNS**: Domain Name System -> Do Not Search (use DNS instead)
- **HTTP**: Hypertext Transfer Protocol -> How To Transfer Pages
- **TLS**: Transport Layer Security -> Trust Lock Secure
- **IP**: Internet Protocol -> I Pack (data into packets)
- **TCP**: Transmission Control Protocol -> Try Checking Packets
- **SMTP**: Simple Mail Transfer Protocol -> Send Mail To People
- **FTP**: File Transfer Protocol ->