File Transfer Protocol (FTP) is an application layer protocol that is used to transfer files between local and remote file systems. It runs on top of TCP, like HTTP. To transfer a file, FTP uses two TCP connections in parallel: a control connection and a data connection. The control connection is used to send commands and responses between the client and the server, while the data connection is used to send the actual file. The control connection is initiated on port 21 and the data connection is initiated on port 20.

The following diagram illustrates the basic architecture of FTP in the application layer:

```
+----------------+              +----------------+
|                |              |                |
|   FTP Client   |              |   FTP Server   |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|   Control      |              |   Control      |
|   Connection   |<-----------> |   Connection   |
|   (Port 21)    |              |   (Port 21)    |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|   Data         |              |   Data         |
|   Connection   |<-----------> |   Connection   |
|   (Port 20)    |              |   (Port 20)    |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|   TCP Layer    |              |   TCP Layer    |
|                |              |                |
+----------------+              +----------------+
|                |              |                |
|   IP Layer     |              |   IP Layer     |
|                |              |                |
+----------------+              +----------------+
```