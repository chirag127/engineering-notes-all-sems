### Basic concepts of Cryptography in application layer

Cryptography is the practice of securing communications by using various techniques that prevent unauthorized parties from viewing or altering data. Cryptography can provide confidentiality, integrity, authentication and non-repudiation to the data. Cryptography can be applied in different layers of the network stack, such as the physical layer, the data link layer, the network layer, the transport layer and the application layer. The application layer is the highest level of the network stack, where the user interacts with the software applications that use the network services. Cryptography in the application layer can be used to protect the data that is exchanged between the applications, such as emails, web pages, instant messages, online transactions, etc.

There are two main types of cryptography that can be used in the application layer: symmetric key cryptography and asymmetric key cryptography. Symmetric key cryptography uses the same key to encrypt and decrypt the data, while asymmetric key cryptography uses a pair of keys: a public key and a private key. The public key can be shared with anyone, while the private key must be kept secret. The public key can be used to encrypt the data, and the private key can be used to decrypt it, or vice versa. Symmetric key cryptography is faster and simpler than asymmetric key cryptography, but it has the problem of key distribution: how to securely share the same key with the intended recipients. Asymmetric key cryptography solves this problem by using the public key infrastructure (PKI), where the public keys are certified by trusted authorities and can be verified by anyone.

The following diagram illustrates the basic architecture of a cryptographic system in the application layer:

```
+-----------------+     +-----------------+
|                 |     |                 |
|   Application   |     |   Application   |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  Cryptography   |     |  Cryptography   |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  Transport      |     |  Transport      |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  Network        |     |  Network        |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  Data Link      |     |  Data Link      |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  Physical       |     |  Physical       |
|                 |     |                 |
+-----------------+     +-----------------+
```

The cryptography module in the application layer can use either symmetric or asymmetric algorithms to encrypt and decrypt the data, depending on the application requirements and the security goals. For example, an email application can use asymmetric cryptography to sign and verify the messages, and symmetric cryptography to encrypt and decrypt the message contents. A web application can use asymmetric cryptography to establish a secure connection with the server, and symmetric cryptography to exchange the data over the connection. A blockchain application can use asymmetric cryptography to generate and validate the transactions, and symmetric cryptography to hash and link the blocks.