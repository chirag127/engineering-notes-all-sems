Remote login is a service that allows a user to log in to a remote computer and run applications as if the user were physically at the host computer. Remote login is an example of an application layer service, which is the highest layer in the OSI model and the TCP/IP model. The application layer provides the interface between the user and the network.

There are different protocols that can implement remote login, such as Telnet and SSH. Telnet is an older and insecure protocol that sends data in plain text over the network. SSH is a newer and secure protocol that encrypts data and provides authentication and integrity. Both protocols use a client-server model, where the client initiates a connection request to the server and the server responds with a login prompt. The client then sends the username and password to the server and the server verifies them. If the login is successful, the server creates a virtual terminal for the client and allows the client to execute commands on the remote computer.

The following diagram illustrates the basic architecture of a remote login service using SSH:

```
+----------------+           +----------------+
|                |           |                |
|     User       |           |    Remote      |
|                |           |    Computer    |
+----------------+           +----------------+
|                |           |                |
| Application    |           | Application    |
| Layer          |           | Layer          |
| (SSH Client)   |           | (SSH Server)   |
|                |           |                |
+----------------+           +----------------+
|                |           |                |
| Transport      |           | Transport      |
| Layer          |           | Layer          |
| (TCP)          |           | (TCP)          |
|                |           |                |
+----------------+           +----------------+
|                |           |                |
| Network        |           | Network        |
| Layer          |           | Layer          |
| (IP)           |           | (IP)           |
|                |           |                |
+----------------+           +----------------+
|                |           |                |
| Data Link      |           | Data Link      |
| Layer          |           | Layer          |
|                |           |                |
+----------------+           +----------------+
|                |           |                |
| Physical       |           | Physical       |
| Layer          |           | Layer          |
|                |           |                |
+----------------+           +----------------+
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       |                             |
       +-----------------------------+
               Network
```