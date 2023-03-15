### Electronic mail in application layer

Electronic mail (or email) is an application layer service that allows users to exchange messages and information over the internet. Email is one of the most popular and widely used services of the internet. 

The email system consists of three major components:

- **User agent**: The software that the user uses to read, compose, and organize email messages. Examples of user agents are Outlook, Gmail, Thunderbird, etc.
- **Mail server**: The server that interacts with user agents and other mail servers to deliver and store email messages. Each mail server has a unique name and an associated mailbox for each user. Examples of mail servers are smtp.gmail.com, mail.yahoo.com, etc.
- **Simple Mail Transfer Protocol (SMTP)**: The protocol that defines the format and rules for exchanging email messages between mail servers and user agents. SMTP is an application layer protocol that uses TCP as the transport layer protocol. SMTP uses port 25 by default.

The email system also uses two other application layer protocols to retrieve email messages from mail servers:

- **Post Office Protocol (POP)**: A protocol that allows a user agent to download email messages from a mail server and delete them from the server. POP is a simple and stateless protocol that does not support email organization or synchronization. POP uses port 110 by default.
- **Internet Message Access Protocol (IMAP)**: A protocol that allows a user agent to access and manipulate email messages on a mail server without downloading them. IMAP supports email organization, synchronization, and multiple clients. IMAP uses port 143 by default.

The following is a pseudocode example of how email works in the application layer:

```
# User A wants to send an email to User B
# User A uses a user agent to compose an email message
message = create_message(to: userB@domainB.com, from: userA@domainA.com, subject: "Hello", body: "Hi, how are you?")

# User A's user agent contacts User A's mail server using SMTP
connect_to(userA_mail_server, port: 25)

# User A's user agent sends the message to User A's mail server using SMTP commands and responses
send("HELO userA_mail_server")
receive("250 OK")
send("MAIL FROM: userA@domainA.com")
receive("250 OK")
send("RCPT TO: userB@domainB.com")
receive("250 OK")
send("DATA")
receive("354 Start mail input")
send(message)
send(".")
receive("250 OK")
send("QUIT")
receive("221 Bye")

# User A's mail server contacts User B's mail server using SMTP
connect_to(userB_mail_server, port: 25)

# User A's mail server sends the message to User B's mail server using SMTP commands and responses
send("HELO userA_mail_server")
receive("250 OK")
send("MAIL FROM: userA@domainA.com")
receive("250 OK")
send("RCPT TO: userB@domainB.com")
receive("250 OK")
send("DATA")
receive("354 Start mail input")
send(message)
send(".")
receive("250 OK")
send("QUIT")
receive("221 Bye")

# User B's mail server stores the message in User B's mailbox
store_message(userB_mailbox, message)

# User B uses a user agent to retrieve the message from User B's mail server using POP or IMAP
# If User B uses POP
connect_to(userB_mail_server, port: 110)
send("USER userB")
receive("+OK")
send("PASS password")
receive("+OK")
send("LIST")
receive("+OK 1 messages")
send("RETR 1")
receive("+OK")
receive(message)
send("DELE 1")
receive("+OK")
send("QUIT")
receive("+OK Bye")

# If User B uses IMAP
connect_to(userB_mail_server, port: 143)
send("A001 LOGIN userB password")
receive("A001 OK")
send("A002 SELECT INBOX")
receive("A002 OK")
send("A003 FETCH 1 BODY")
receive("A003 OK")
receive(message)
send("A004 LOGOUT")
receive("A004 OK Bye")
```