### Electronic mail in application layer

- Electronic mail (or email) is an application layer service that allows users to exchange messages and information over the internet.
- Email is one of the most popular and widely used services of the internet .
- Email has two major components: user agents and mail servers.
  - User agents are the software programs that users use to read, compose, and organize email messages. Examples of user agents are Outlook, Gmail, Thunderbird, etc.
  - Mail servers are the servers that interact with user agents and other mail servers to deliver email messages. Mail servers store incoming and outgoing messages in mailboxes.
- Email uses several protocols to perform different functions in the application layer:
  - Simple Mail Transfer Protocol (SMTP) is used to transfer email messages from a sender's mail server to a receiver's mail server . SMTP is a connection-oriented and reliable protocol that uses TCP port 25.
  - Post Office Protocol (POP) is used to retrieve email messages from a mail server to a user agent. POP is a connection-oriented and reliable protocol that uses TCP port 110. POP allows users to download email messages and delete them from the server.
  - Internet Message Access Protocol (IMAP) is used to retrieve email messages from a mail server to a user agent. IMAP is a connection-oriented and reliable protocol that uses TCP port 143. IMAP allows users to access email messages without downloading them and also supports email download. IMAP also allows users to organize and manage email messages in folders on the server.
  - Multipurpose Internet Mail Extensions (MIME) is used to encode and decode email messages that contain non-ASCII characters, images, audio, video, or other attachments . MIME defines the format and structure of email messages and the methods to encode and decode them.
- Email also uses other protocols in the transport layer, network layer, and physical layer to ensure the delivery of email messages over the internet. For example, email uses TCP/IP, DNS, Ethernet, etc.