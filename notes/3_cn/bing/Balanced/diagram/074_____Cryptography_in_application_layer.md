Cryptography in application layer is a data-security solution that encrypts nearly any type of data passing through an application. When encryption occurs at this level, data is encrypted across multiple (including disk, file, and database) layers. This application layer encryption approach increases security by reducing the number of potential attack vectors.

A possible diagram for cryptography in application layer is:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Application   |      |   Application   |      |   Application   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Encryption    |      |   Encryption    |      |   Encryption    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Transport     |      |   Transport     |      |   Transport     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Network       |      |   Network       |      |   Network       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Data Link     |      |   Data Link     |      |   Data Link     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Physical      |      |   Physical      |      |   Physical      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+

    Sender              Intermediate Node          Receiver
```

The diagram shows how data is encrypted at the application layer before being sent over the network. The intermediate node can only see the encrypted data and cannot decrypt it. The receiver can decrypt the data using the same encryption algorithm and key as the sender. This way, the data is protected from unauthorized access or modification.