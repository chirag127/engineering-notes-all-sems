### Hash functions

A hash function is a mathematical function that maps an arbitrary binary string (called the message) to a binary string of fixed size (called the hash value or the digest). A hash function is also known as a message digest or a checksum. A hash function can be used to verify the integrity and authenticity of a message, as well as to generate digital signatures and encryption keys.

A cryptographic hash function is a special type of hash function that has the following properties:

- **Pre-image resistance**: Given a hash value, it is computationally infeasible to find a message that produces that hash value. This means that a hash function cannot be reversed or inverted.
- **Second pre-image resistance**: Given a message and its hash value, it is computationally infeasible to find another message that produces the same hash value. This means that a hash function is collision-free or one-way.
- **Collision resistance**: It is computationally infeasible to find two different messages that produce the same hash value. This means that a hash function is unique or injective.

Some examples of cryptographic hash functions are:

- **MD5**: A 128-bit hash function that was widely used in the past, but is now considered insecure due to its vulnerability to collision attacks.
- **SHA-1**: A 160-bit hash function that was also widely used in the past, but is now deprecated due to its weakness to collision attacks.
- **SHA-2**: A family of hash functions that include SHA-224, SHA-256, SHA-384, and SHA-512, with different output sizes. They are considered secure and widely used in various applications.
- **SHA-3**: A family of hash functions that include SHA3-224, SHA3-256, SHA3-384, and SHA3-512, with different output sizes. They are based on a different design principle than SHA-2 and are considered more resistant to future attacks.

The process of hashing a message can be illustrated as follows:

![Hashing process](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Cryptographic_Hash_Function.svg/1200px-Cryptographic_Hash_Function.svg.png)

Source: