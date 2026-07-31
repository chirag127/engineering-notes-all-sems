File Transfer Protocol (FTP) is a standard communication protocol used for the transfer of computer files from a server to a client on a computer network. FTP is built on a client–server model architecture using separate control and data connections between the client and the server.

The following diagram shows the basic steps of an FTP session:

```
+--------+             +--------+
| Client |             | Server |
+--------+             +--------+
    |                      |
    |  Control connection  |
    |--------------------->|  Port 21
    |                      |
    |  USER username       |
    |--------------------->|
    |                      |
    |  PASS password       |
    |--------------------->|
    |                      |
    |  230 Logged in       |
    |<---------------------|
    |                      |
    |  PASV                |
    |--------------------->|
    |                      |
    |  227 Entering Passive|
    |  Mode (h1,h2,h3,h4,p1,p2)
    |<---------------------|
    |                      |
    |  Data connection     |
    |--------------------->|  Port p1*256+p2
    |                      |
    |  RETR filename       |
    |--------------------->|
    |                      |
    |  150 Opening data    |
    |  connection          |
    |<---------------------|
    |                      |
    |  File content        |
    |<---------------------|
    |                      |
    |  226 Transfer complete
    |<---------------------|
    |                      |
    |  QUIT                |
    |--------------------->|
    |                      |
    |  221 Goodbye         |
    |<---------------------|
    |                      |
    |  Close connections   |
    |<-------------------->|
    |                      |
```

: File Transfer Protocol - Wikipedia