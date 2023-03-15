### Hash functions

A hash function is a mathematical function that maps an arbitrary binary string (called the message) to a binary string of fixed size (called the hash value or the digest). A hash function is also known as a message digest or a fingerprint of the message.

A cryptographic hash function is a hash function that has special properties desirable for a cryptographic application, such as:

- **Pre-image resistance**: Given a hash value, it is computationally hard to find a message that produces that hash value. This property ensures that a hash function cannot be easily inverted, and that the message cannot be recovered from the hash value.
- **Second pre-image resistance**: Given a message, it is computationally hard to find another message that produces the same hash value. This property ensures that a hash function is collision-resistant, and that the message cannot be replaced by another message with the same hash value.
- **Collision resistance**: It is computationally hard to find two different messages that produce the same hash value. This property ensures that a hash function is unique, and that the hash value can be used as a reliable identifier of the message.

Some examples of cryptographic hash functions are:

- **MD5**: A hash function that produces a 128-bit hash value. It was widely used in the past, but it is now considered insecure due to its vulnerability to collision attacks.
- **SHA-1**: A hash function that produces a 160-bit hash value. It was also widely used in the past, but it is now considered insecure due to its vulnerability to collision attacks.
- **SHA-2**: A family of hash functions that produce hash values of different sizes, such as 224, 256, 384, or 512 bits. It is currently the standard hash function for many applications, such as digital signatures and certificates.
- **SHA-3**: A family of hash functions that produce hash values of different sizes, such as 224, 256, 384, or 512 bits. It is based on a different design than SHA-2, and it is considered more secure and efficient.

Cryptographic hash functions are the basic tools of modern cryptography that are used in information security to authenticate transactions, messages, and digital signatures. The act of hashing is, therefore, running an input into a formula that converts it into an output message of fixed length.