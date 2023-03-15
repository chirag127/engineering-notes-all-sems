File Transfer Protocol (FTP) is an application layer protocol that is used to transfer files between local and remote devices over the Internet. It runs on top of TCP, like HTTP. To transfer a file, FTP uses two TCP connections in parallel: control connection and data connection. The control connection is used to send commands and receive replies between the client and the server. The data connection is used to transfer the actual file data.

A possible ASCII diagram for FTP in application layer is:

```
+----------------+     +----------------+     +----------------+
| Application    |     | Application    |     | Application    |
| Layer          |     | Layer          |     | Layer          |
|                |     |                |     |                |
| +------------+ |     | +------------+ |     | +------------+ |
| | FTP Client | |     | | FTP Server | |     | | FTP Client | |
| +------------+ |     | +------------+ |     | +------------+ |
+----------------+     +----------------+     +----------------+
| Transport      |     | Transport      |     | Transport      |
| Layer          |     | Layer          |     | Layer          |
|                |     |                |     |                |
| +------------+ |     | +------------+ |     | +------------+ |
| | TCP        | |     | | TCP        | |     | | TCP        | |
| +------------+ |     | +------------+ |     | +------------+ |
+----------------+     +----------------+     +----------------+
| Network        |     | Network        |     | Network        |
| Layer          |     | Layer          |     | Layer          |
|                |     |                |     |                |
| +------------+ |     | +------------+ |     | +------------+ |
| | IP         | |     | | IP         | |     | | IP         | |
| +------------+ |     | +------------+ |     | +------------+ |
+----------------+     +----------------+     +----------------+
| Data Link      |     | Data Link      |     | Data Link      |
| Layer          |     | Layer          |     | Layer          |
|                |     |                |     |                |
| +------------+ |     | +------------+ |     | +------------+ |
| | Ethernet   | |     | | Ethernet   | |     | | Ethernet   | |
| +------------+ |     | +------------+ |     | +------------+ |
+----------------+     +----------------+     +----------------+
| Physical       |     | Physical       |     | Physical       |
| Layer          |     | Layer          |     | Layer          |
|                |     |                |     |                |
| +------------+ |     | +------------+ |     | +------------+ |
| | Cable      | |     | | Cable      | |     | | Cable      | |
| +------------+ |     | +------------+ |     | +------------+ |
+----------------+     +----------------+     +----------------+

Control connection: <------------------------->

Data connection:    <------------------------->

```