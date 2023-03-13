Electronic mail is an application layer service in which a user can transfer messages and information with another user. Electronic mail is the most popular service of the internet. It uses several protocols to perform different functions, such as SMTP, POP3, IMAP, MIME, etc.   

The following diagram illustrates the basic architecture of electronic mail in application layer using ASCII art:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    User Agent   |        |    Mail Server  |        |    Mail Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    SMTP Client  |        |    SMTP Server  |        |    SMTP Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    POP3 Client  |        |    POP3 Server  |        |    POP3 Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    IMAP Client  |        |    IMAP Server  |        |    IMAP Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    MIME Client  |        |    MIME Server  |        |    MIME Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    TCP Client   |        |    TCP Server   |        |    TCP Server   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    IP Client    |        |    IP Server    |        |    IP Server    |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    NIC Client   |        |    NIC Server   |        |    NIC Server   |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```

The user agent is the software that the user uses to read, compose, and organize email. The mail server is the server that interacts with user agents and other mail servers to deliver email. SMTP (Simple Mail Transfer Protocol) is the protocol that transfers email from the sender's mail server to the receiver's mail server. POP3 (Post Office Protocol version 3) and IMAP (Internet Message Access Protocol) are the protocols that allow the user agent to retrieve email from the mail server. MIME (Multipurpose Internet Mail Extensions) is the protocol that allows the user agent and the mail server to handle different types of email content, such as text, images, audio, video, etc. TCP (Transmission Control Protocol) and IP (Internet Protocol) are the protocols that provide reliable and routable data transmission between the user agent and the mail server. NIC (Network Interface Card) is the hardware device that connects the user agent and the mail server to the physical network.   

: https://www.tutorialandexample.com/e-mail-in-computer-network
: https://www.slideshare.net/AmishaSahu3/application-layer-protocol-electronic-mail
: https://www.studocu.com/en-us/document/embry-riddle-aeronautical-university/computer-and-network-technologies/application-layer-unit5/48720165
: https://en.wikipedia.org/wiki/Application_layer
: https://www.geeksforgeeks.org/email-protocols/
: https://www.geeksforgeeks.org/application-layer-in-osi-model/