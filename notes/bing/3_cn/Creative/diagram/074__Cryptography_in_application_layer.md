Cryptography in application layer is a data-security solution that encrypts nearly any type of data passing through an application. When encryption occurs at this level, data is encrypted across multiple (including disk, file, and database) layers. This application layer encryption approach increases security by reducing the number of potential attack vectors.

Application-layer encryption, or shift-left cryptography, means giving developers more control over what gets encrypted and who gets the keys for decryption. In some cases, the users themselves may be the only parties with the keys. End-to-end encryption is an increasingly popular type of application-layer cryptography. This type of encryption lets organizations enforce access control using key management as well as policy.

The following diagram illustrates the basic architecture of a typical application-layer encryption scheme:

### Cryptography in application layer

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Application  |     |    Application  |     |    Application  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Encryption   |     |    Encryption   |     |    Encryption   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Transport    |     |    Transport    |     |    Transport    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Network      |     |    Network      |     |    Network      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Physical     |     |    Physical     |     |    Physical     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       User A                 Server                  User B
```

In this diagram, User A and User B are the only parties who have the keys to encrypt and decrypt the data. The server acts as a relay for the data, but cannot access its content. The data is encrypted at the application layer, before it is sent to the transport layer. The data remains encrypted across the network and physical layers, until it reaches the application layer of the other user. This way, the data is protected from any unauthorized access or modification.