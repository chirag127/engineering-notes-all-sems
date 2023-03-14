Remote login is a process in which a user can log in to a remote computer and use the services that are available on that computer. Remote login is an application layer service that is implemented using protocols such as Telnet or rlogin . The application layer is the topmost layer in the OSI model that provides services directly to the user and the application processes.

The following diagram illustrates the basic architecture of a remote login in the application layer using ASCII characters:

```
+-----------------+      +-----------------+
|                 |      |                 |
|  Local Computer |      | Remote Computer |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  User Interface |      |  Application    |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Telnet Client  |      |  Telnet Server  |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Presentation   |      |  Presentation   |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Session        |      |  Session        |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Transport      |      |  Transport      |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Network        |      |  Network        |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Data Link      |      |  Data Link      |
|                 |      |                 |
+-----------------+      +-----------------+
|                 |      |                 |
|  Physical       |      |  Physical       |
|                 |      |                 |
+-----------------+      +-----------------+
```

The steps involved in a remote login are as follows:

1. The user types something on the local computer, and the local operating system accepts the characters.
2. The local computer does not interpret the characters, but sends them to the Telnet client.
3. The Telnet client transforms the characters to a universal character set called Network Virtual Terminal (NVT) characters and passes them to the local TCP/IP protocol stack.
4. The commands or text in the form of NVT travel through the internet and arrive at the TCP/IP stack at the remote computer.
5. The characters are then delivered to the operating system and then passed to the Telnet server.
6. The Telnet server converts the characters to the format that is understandable by the remote computer.
7. The remote operating system receives the characters from a pseudo-terminal driver, which is a piece of software that pretends that the characters are coming from a terminal.
8. The operating system then passes the characters to the appropriate application program.
9. The application program processes the characters and sends the output back to the pseudo-terminal driver.
10. The pseudo-terminal driver sends the output to the Telnet server, which converts it to NVT characters and passes it to the remote TCP/IP protocol stack.
11. The output in the form of NVT travels through the internet and arrives at the local TCP/IP protocol stack.
12. The output is then delivered to the Telnet client, which converts it to the format that is understandable by the local computer.
13. The local operating system receives the output and displays it on the user interface.
