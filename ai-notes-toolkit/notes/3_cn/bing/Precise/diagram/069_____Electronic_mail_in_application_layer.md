### Electronic mail in application layer

Electronic mail (email) is a method of exchanging messages between people using electronic devices. Email operates across computer networks, primarily the Internet. In the application layer of the OSI model, email is one of the protocols used for communication.

Here is an ASCII diagram that illustrates the process of sending an email from the sender to the recipient through the application layer:

```
Sender's device                      Email server                      Recipient's device
+----------------+                   +------------+                   +-----------------+
|                |   SMTP request    |            |   SMTP delivery   |                 |
|  Email client  |------------------>|            |------------------>|   Email client  |
|                |                   |            |                   |                 |
+----------------+                   +------------+                   +-----------------+
```

In this diagram, the sender composes an email using an email client on their device. The email client sends the email to the email server using the Simple Mail Transfer Protocol (SMTP). The email server then delivers the email to the recipient's email client, also using SMTP.
