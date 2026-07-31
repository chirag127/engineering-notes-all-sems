Electronic mail is an application layer service that allows users to send and receive messages over the internet. Electronic mail consists of three major components: user agents, mail servers, and protocols.

User agents are the software programs that users interact with to compose, read, and organize email messages. Examples of user agents are Outlook, Gmail, and Thunderbird.

Mail servers are the computers that store and forward email messages. Each mail server has a unique name and an associated mailbox for each user. Mail servers communicate with each other using protocols such as SMTP, POP3, and IMAP.

SMTP (Simple Mail Transfer Protocol) is the protocol that mail servers use to send email messages to each other. SMTP uses a client-server model, where the sending mail server acts as the client and the receiving mail server acts as the server. SMTP uses TCP port 25 to establish a connection and exchange commands and data.

POP3 (Post Office Protocol version 3) and IMAP (Internet Message Access Protocol) are the protocols that user agents use to retrieve email messages from mail servers. POP3 allows the user agent to download all the messages from the mail server and delete them from the server. IMAP allows the user agent to access and manipulate the messages on the mail server without downloading them. POP3 uses TCP port 110 and IMAP uses TCP port 143 to communicate with the mail server.

The following is a simplified ASCII diagram of the electronic mail in the application layer:

```
+-----------------+          +-----------------+          +-----------------+
|                 |          |                 |          |                 |
|   User Agent    |          |   Mail Server   |          |   Mail Server   |
|                 |          |                 |          |                 |
+-----------------+          +-----------------+          +-----------------+
|                 |          |                 |          |                 |
|   POP3 or IMAP  |<-------->|   POP3 or IMAP  |          |   POP3 or IMAP  |
|                 |          |                 |          |                 |
+-----------------+          +-----------------+          +-----------------+
|                 |          |                 |          |                 |
|      SMTP       |--------->|      SMTP       |--------->|      SMTP       |
|                 |          |                 |          |                 |
+-----------------+          +-----------------+          +-----------------+
```