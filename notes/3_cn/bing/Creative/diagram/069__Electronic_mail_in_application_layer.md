Electronic mail is an application layer service that allows users to send and receive messages over the internet. Electronic mail involves two main components: user agents and mail servers. User agents are the software programs that allow users to read, compose, and organize email messages. Mail servers are the servers that store and forward email messages between user agents and other mail servers.

There are three main protocols that are used for electronic mail: SMTP, POP3, and IMAP. SMTP (Simple Mail Transfer Protocol) is the protocol that is used to send email messages from a user agent to a mail server, or from one mail server to another. POP3 (Post Office Protocol version 3) and IMAP (Internet Message Access Protocol) are the protocols that are used to retrieve email messages from a mail server to a user agent. POP3 allows users to download email messages to their local device and delete them from the server. IMAP allows users to access email messages on the server without downloading them, and also supports multiple mailboxes and concurrent access.

The following diagram illustrates the basic architecture of electronic mail in the application layer:

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  User Agent A  |        |  Mail Server A |        |  Mail Server B |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
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
      |                         |                         |
      |<------------------------|                         |
      |  POP3 or IMAP          |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |------------------------>|                         |
      |  SMTP                   |                         |
      |                         |                         |
      |                         |------------------------>|
      |                         |  SMTP                   |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |<------------------------|
      |                         |  POP3 or IMAP          |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      |                         |                         |
      +----------------+        +----------------+        +----------------+
      |                |        |                |        |                |
      |  User Agent B  |        |  Mail Server A |        |  Mail Server B |
      |                |        |                |        |                |
      +----------------+        +----------------+        +----------------+
```