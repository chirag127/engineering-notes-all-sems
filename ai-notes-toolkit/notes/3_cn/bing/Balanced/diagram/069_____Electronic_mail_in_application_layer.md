Electronic mail is an application layer service in which a user can transfer the messages and information with another user. Electronic mail has three major components: user agents, mail servers, and simple mail transfer protocol (SMTP).

User agents are the software that users use to read, compose, and organize email, such as Outlook, Gmail, or Thunderbird. Mail servers are the servers that interact with user agents and other mail servers to deliver email. SMTP is the protocol that defines how mail servers communicate with each other to send and receive email.

The following ASCII diagram shows how electronic mail works in the application layer:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   User Agent   |       |   Mail Server  |       |   Mail Server  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|    Message     |       |    Message     |       |    Message     |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|    SMTP        |       |    SMTP        |       |    SMTP        |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
| Application    |       | Application    |       | Application    |
| Layer          |       | Layer          |       | Layer          |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```

The diagram shows the following steps:

1. The user composes a message using a user agent and specifies the recipient's email address.
2. The user agent sends the message to the mail server using SMTP.
3. The mail server looks up the domain name of the recipient's email address and finds the corresponding mail server.
4. The mail server sends the message to the recipient's mail server using SMTP.
5. The recipient's mail server stores the message until the recipient accesses it using a user agent.
