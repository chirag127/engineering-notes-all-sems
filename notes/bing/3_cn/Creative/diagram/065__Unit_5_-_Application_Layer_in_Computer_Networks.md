## Unit 5 - Application Layer in Computer Networks

The application layer is the topmost layer of the Open Systems Interconnection (OSI) model and the Internet Protocol Suite (TCP/IP) model. It is responsible for providing services and protocols that enable applications to communicate with other applications on different computer systems and networks. The application layer is not an application itself, but an abstraction layer that specifies the shared communications protocols and interface methods used by hosts in a communications network .

Some of the common application layer protocols are:

- **Hypertext Transfer Protocol (HTTP)**: It is a protocol for transferring web pages and other resources over the internet. It uses a client-server model, where the client requests a resource from the server and the server responds with the resource or an error message. HTTP uses Uniform Resource Locators (URLs) to identify and locate resources on the web.
- **File Transfer Protocol (FTP)**: It is a protocol for transferring files between hosts on a network. It also allows users to access, retrieve and manage files on a remote computer. FTP uses a control connection and a data connection to exchange commands and data between the client and the server.
- **Simple Mail Transfer Protocol (SMTP)**: It is a protocol for sending and receiving email messages over the internet. It uses a store-and-forward model, where the sender transfers the message to a mail server, which then forwards it to the recipient's mail server. SMTP also supports attachments, encryption and authentication.
- **Domain Name System (DNS)**: It is a protocol for resolving domain names into IP addresses and vice versa. It uses a hierarchical and distributed database of name servers, which store and update the mappings between domain names and IP addresses. DNS also supports caching, load balancing and security features.
- **Telnet**: It is a protocol for providing remote access to a host computer over a network. It allows users to log on as a remote host and execute commands on the host. Telnet uses a virtual terminal emulation, where the client and the server exchange keystrokes and screen updates.
- **Hypertext Transfer Protocol Secure (HTTPS)**: It is a protocol for secure communication over the internet. It uses HTTP as the application layer protocol and Transport Layer Security (TLS) or Secure Sockets Layer (SSL) as the encryption layer protocol. HTTPS ensures the confidentiality, integrity and authenticity of the data exchanged between the client and the server.

The following diagram illustrates the basic architecture of the application layer in computer networks using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
| Application     |    | Application     |    | Application     |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Transport       |    | Transport       |    | Transport       |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Network         |    | Network         |    | Network         |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Data Link       |    | Data Link       |    | Data Link       |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
| Physical        |    | Physical        |    | Physical        |
| Layer           |    | Layer           |    | Layer           |
+-----------------+    +-----------------+    +-----------------+
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      +-------------------------+-------------------------+
                         Network
```