Protocols are a set of rules that govern the communication between different applications or devices on the web. The web uses various protocols to enable the exchange of data, such as text, images, audio, video, etc. Some of the common protocols that govern the web are:

- TCP/IP (Transmission Control Protocol/Internet Protocol): This is the fundamental protocol that defines how data is transmitted and routed over the internet. It consists of two layers: the IP layer, which handles the addressing and delivery of packets, and the TCP layer, which ensures the reliability and order of data transmission.
- DNS (Domain Name System): This is the protocol that translates domain names, such as www.google.com, into IP addresses, such as 142.250.64.100, that can be understood by computers. It uses a hierarchical system of servers that store and update the mappings between domain names and IP addresses.
- HTTP (HyperText Transfer Protocol): This is the protocol that defines how web browsers and web servers communicate and exchange web resources, such as webpages, images, etc. It uses a request-response model, where the browser sends a request for a resource to the server, and the server responds with the resource or an error message.
- HTTPS (HyperText Transfer Protocol Secure): This is the protocol that adds encryption and authentication to HTTP, to ensure the security and privacy of web communication. It uses SSL (Secure Sockets Layer) or TLS (Transport Layer Security) protocols to encrypt the data and verify the identity of the server and the client.
- FTP (File Transfer Protocol): This is the protocol that enables the transfer of files between computers on the web. It uses a client-server model, where the client initiates a connection to the server and requests to upload or download files. The server then grants or denies the access and transfers the files accordingly.

### Protocols Governing Web

The following diagram illustrates the basic architecture of the web and the protocols involved in each layer:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Web Browser  |    |    Web Server   |    |    DNS Server   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|      HTTPS      |    |      HTTPS      |    |       DNS       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|       SSL       |    |       SSL       |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|       TCP       |    |       TCP       |    |       UDP       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|       IP        |    |       IP        |    |       IP        |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Ethernet     |    |    Ethernet     |    |    Ethernet     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```