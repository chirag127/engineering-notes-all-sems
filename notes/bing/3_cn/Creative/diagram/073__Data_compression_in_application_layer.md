Data compression is the function of presentation layer in OSI reference model. Compression is often used to maximize the use of bandwidth across a network or to optimize disk space when saving data. Data compression reduces the number of bits that need to be transmitted or stored by using algorithms that eliminate redundancy or irrelevant information.

### Data compression in application layer

The application layer is the topmost layer of the OSI model that provides the interface between the user and the network. The application layer also identifies constraints at the application level such as those associated with authentication, privacy, quality of service, networking devices, and data syntax. Some common application layer protocols that use data compression are:

- File Transfer Protocol (FTP): FTP is a protocol that allows users to transfer files between computers over a network. FTP can use data compression to reduce the size of the files before sending them, which can improve the transfer speed and save bandwidth. FTP can use different compression methods, such as ZIP, GZIP, or BZIP2, depending on the type and format of the files.
- Simple Mail Transfer Protocol (SMTP): SMTP is a protocol that enables the sending and receiving of email messages over a network. SMTP can use data compression to reduce the size of the email messages and attachments before sending them, which can improve the delivery speed and save bandwidth. SMTP can use different compression methods, such as MIME, Base64, or Quoted-Printable, depending on the type and format of the messages and attachments.
- Domain Name System (DNS): DNS is a protocol that translates domain names into IP addresses and vice versa. DNS can use data compression to reduce the size of the DNS messages and responses, which can improve the query speed and save bandwidth. DNS can use a compression method called name compression, which eliminates the repetition of domain name labels in the DNS messages and responses.

The following diagram illustrates the basic architecture of a data compression in application layer using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Application   |    |   Application   |    |   Application   |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Presentation  |    |   Presentation  |    |   Presentation  |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Session       |    |   Session       |    |   Session       |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Transport     |    |   Transport     |    |   Transport     |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Network       |    |   Network       |    |   Network       |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Link     |    |   Data Link     |    |   Data Link     |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Physical      |    |   Physical      |    |   Physical      |
|     Layer       |    |     Layer       |    |     Layer       |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |