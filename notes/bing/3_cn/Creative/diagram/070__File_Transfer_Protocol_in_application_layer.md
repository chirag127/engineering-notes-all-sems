File Transfer Protocol (FTP) is an application layer protocol that is used to transfer files between a local device and a server over the Internet. It uses two TCP connections in parallel: a control connection and a data connection. The control connection is used to send commands and receive responses, while the data connection is used to transfer the actual files.

The following ASCII diagram illustrates the basic architecture of FTP:

```
+----------------+              +----------------+
|                |              |                |
|    Local       |              |    Remote      |
|    Device      |              |    Server      |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|    FTP         |              |    FTP         |
|    Client      |              |    Server      |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|    TCP         |              |    TCP         |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|    IP          |              |    IP          |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|    Ethernet    |              |    Ethernet    |
|                |              |                |
+----------------+              +----------------+
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |                         |   |
     |   |<----------------------->|   |
     |   | Control connection     |   |
     |   | (port 21)              |   |
     |   |                         |   |
     |<---------------------------->|   |
     | Data connection            |   |
     | (port 20)                  |   |
     |                             |   |
```