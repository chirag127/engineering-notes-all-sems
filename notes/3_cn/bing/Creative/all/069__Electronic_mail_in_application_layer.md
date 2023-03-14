### Electronic mail in application layer

- Electronic mail (email) is an application layer service that allows users to exchange messages and information over the internet.
- Email is one of the most popular and widely used services of the internet.
- Email has three basic components: user agents, mail servers, and protocols.
- User agents are the software applications that users use to read, compose, and organize email messages. Examples of user agents are Outlook, Gmail, Thunderbird, etc.
- Mail servers are the computers that store and forward email messages between user agents and other mail servers. Each mail server has a unique domain name and an IP address. Examples of mail servers are mail.google.com, mail.yahoo.com, etc.
- Protocols are the set of rules and commands that govern the communication and data exchange between user agents and mail servers. There are three main protocols involved in email: SMTP, POP3, and IMAP.
- SMTP (Simple Mail Transfer Protocol) is the protocol that is used to send email messages from a user agent to a mail server, or from one mail server to another. SMTP is an application layer and connection-oriented protocol that uses TCP as the transport layer protocol. SMTP commands are used to identify the sender and receiver email addresses, and the message to be sent. Some of the SMTP commands are HELO, MAIL FROM, RCPT TO, DATA, QUIT, etc.
- POP3 (Post Office Protocol version 3) is the protocol that is used to retrieve email messages from a mail server to a user agent. POP3 is an application layer protocol that allows users to access their email offline, by downloading the messages to their local storage. POP3 commands are used to log in, list, retrieve, delete, and quit the mail server. Some of the POP3 commands are USER, PASS, STAT, LIST, RETR, DELE, QUIT, etc.
- IMAP (Internet Message Access Protocol) is the protocol that is used to retrieve email messages from a mail server to a user agent, without downloading them. IMAP is an application layer protocol that allows users to access their email online, by keeping the messages on the remote server. IMAP commands are used to create, delete, rename, select, examine, and logout the mail server. Some of the IMAP commands are LOGIN, CREATE, DELETE, RENAME, SELECT, EXAMINE, LOGOUT, etc.

- The following diagram shows the basic architecture of email:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    User Agent   |        |    Mail Server  |        |    User Agent   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|     SMTP        |------->|     SMTP        |------->|     SMTP        |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|     POP3        |<-------|     POP3        |        |     IMAP        |
|                 |        |                 |<-------|                 |
+-----------------+        +-----------------+        +-----------------+
```

- A mnemonic to remember the three email protocols is: **S**end **P**ick **I**nspect (SMTP, POP3, IMAP).
- A learning trick to understand the difference between POP3 and IMAP is: POP3 **P**ulls the messages from the server, while IMAP **I**nteracts with the messages on the server.