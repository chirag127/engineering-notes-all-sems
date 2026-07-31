Cryptography is the practice of securing communications by using techniques that prevent unwelcome parties from viewing or modifying the data. Cryptography can be used in applications to provide confidentiality, integrity and authenticity to the data. Some of the basic concepts of cryptography in application layer are:

- Plain text: The original message or data that needs to be encrypted or decrypted.
- Cipher text: The encrypted or scrambled message or data that is unintelligible to anyone who does not have the key.
- Algorithm: The mathematical procedure or formula that is used to transform plain text into cipher text and vice versa.
- Key: The secret value or parameter that is used in conjunction with the algorithm to encrypt or decrypt the data.
- Encryption: The process of converting plain text into cipher text using an algorithm and a key.
- Decryption: The process of converting cipher text back into plain text using an algorithm and a key.

There are two main types of cryptography that are used in applications:

- Symmetric key cryptography: A type of cryptography that uses the same key for both encryption and decryption. The key must be shared securely between the sender and the receiver of the data. Symmetric key cryptography is fast and efficient, but it suffers from the key distribution problem, which is how to securely share the key without compromising it.
- Asymmetric key cryptography: A type of cryptography that uses a pair of keys for encryption and decryption. One key is called the public key and the other is called the private key. The public key can be shared openly with anyone, while the private key must be kept secret by the owner. The public key can be used to encrypt data, but only the corresponding private key can decrypt it. Similarly, the private key can be used to sign data, but only the corresponding public key can verify it. Asymmetric key cryptography solves the key distribution problem, but it is slower and more complex than symmetric key cryptography.

A diagram that illustrates the basic concepts of cryptography in application layer is shown below:

### Basic concepts of cryptography in application layer

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Sender      |     |   Network      |     |    Receiver    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Plain text  |     |                |     |    Plain text  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|    Algorithm   |     |                |     |    Algorithm   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|      Key       |     |                |     |      Key       |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Encryption   |     |                |     |   Decryption   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Cipher text  |---->|                |---->|   Cipher text  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```