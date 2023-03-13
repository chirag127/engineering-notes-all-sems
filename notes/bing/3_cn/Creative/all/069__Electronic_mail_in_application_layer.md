### Electronic mail in application layer

- Electronic mail (or email) is an application layer service that allows users to exchange messages and information over the internet .
- Email is one of the most popular and widely used services of the internet.
- Email has three main components: user agents, mail servers, and protocols .

  - User agents are the applications that allow users to create, read, and send emails. Examples of user agents are Outlook, Gmail, Thunderbird, etc .
  - Mail servers are the computers that store and forward emails. Each mail server has a mailbox for each user and a message queue for outgoing emails .
  - Protocols are the rules and standards that govern the communication between user agents and mail servers. There are two main types of protocols: SMTP and POP/IMAP .

- SMTP (Simple Mail Transfer Protocol) is the protocol that is used to send emails from one mail server to another. SMTP uses a client-server model, where the sender's mail server acts as the client and the receiver's mail server acts as the server  .
- SMTP has three phases: handshaking, transfer, and closure  .

  - Handshaking is the phase where the client and the server establish a connection and exchange greetings and parameters  .
  - Transfer is the phase where the client sends the email message to the server, along with the sender and receiver addresses  .
  - Closure is the phase where the client and the server terminate the connection and acknowledge the successful or unsuccessful transfer  .

- SMTP uses a simple text-based format for the email message, which consists of two parts: the header and the body  .

  - The header contains information such as the sender, receiver, subject, date, etc  .
  - The body contains the actual content of the message, which can be plain text, HTML, or attachments  .

- SMTP can only handle ASCII characters, so if the message contains non-ASCII characters or binary data, it has to be encoded using schemes such as MIME (Multipurpose Internet Mail Extensions) or Base64  .
- SMTP does not provide any security or authentication features, so it is vulnerable to attacks such as spamming, spoofing, or interception  .
- POP (Post Office Protocol) and IMAP (Internet Message Access Protocol) are the protocols that are used to retrieve emails from the mail server to the user agent. POP and IMAP use a client-server model, where the user agent acts as the client and the mail server acts as the server  .
- POP allows the user to download the emails from the mail server and delete them from the server. POP is simple and efficient, but it does not support multiple clients or synchronization  .
- IMAP allows the user to access the emails on the mail server without downloading them. IMAP supports multiple clients, synchronization, and folder management. IMAP is more complex and flexible, but it requires more bandwidth and storage  .
- POP and IMAP also do not provide any security or authentication features, so they are vulnerable to attacks such as eavesdropping, tampering, or impersonation  .
- To enhance the security and authentication of email protocols, extensions such as SSL (Secure Sockets Layer), TLS (Transport Layer Security), or S/MIME (Secure/Multipurpose Internet Mail Extensions) can be used  .

- A possible mnemonic to remember the email protocols is: **S**end **M**essages **T**o **P**eople, **P**ick **O**r **P**eek, **I**nbox **M**