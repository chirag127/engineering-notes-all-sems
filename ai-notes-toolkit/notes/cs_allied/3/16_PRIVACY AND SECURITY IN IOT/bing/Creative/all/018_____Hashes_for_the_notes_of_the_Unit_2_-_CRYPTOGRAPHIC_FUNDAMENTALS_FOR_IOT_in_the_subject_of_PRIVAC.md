# Hashes

Hashes are a type of cryptographic technique that transforms any form of data into a special text string. The text string is called a hash value, a digest, or a fingerprint of the data. Hashes are used to verify the authenticity and integrity of data, such as passwords, digital signatures, or messages.

## Hash Functions

A hash function is an algorithm that takes an input of any size and produces a fixed-size output. The output is determined by the input, meaning that the same input will always produce the same output. However, the input cannot be easily derived from the output, meaning that the hash function is a one-way function.

Some properties of hash functions are:

- Pre-image resistance: Given a hash value h, it should be difficult to find any input m such that h = hash(m).
- Second pre-image resistance: Given an input m1, it should be difficult to find another input m2 such that hash(m1) = hash(m2).
- Collision resistance: It should be difficult to find any two inputs m1 and m2 such that hash(m1) = hash(m2).

## Hash Algorithms

There are many hash algorithms that are used in cryptography, each with different characteristics and security levels. Some of the most popular hash algorithms are:

- Secure Hash Algorithm 1 (SHA-1): A 160-bit hash algorithm that was widely used until it was broken in 2017 by a collision attack.
- Secure Hash Algorithm 2 (SHA-2): A family of hash algorithms that include SHA-224, SHA-256, SHA-384, and SHA-512. They are more secure than SHA-1 and are widely used in various applications.
- Secure Hash Algorithm 3 (SHA-3): A family of hash algorithms that include SHA3-224, SHA3-256, SHA3-384, and SHA3-512. They are based on a different design than SHA-1 and SHA-2 and are considered to be more resistant to attacks.
- MD2, MD4, and MD5: A series of hash algorithms that were developed by Ronald Rivest. They are no longer considered secure and should not be used for cryptographic purposes.

## Hash Applications

Hashes have many applications in cryptography, such as:

- Password hashing: Hashing passwords before storing them in a database or a server. This way, even if the database or the server is compromised, the attacker cannot recover the original passwords from the hashes. However, password hashing should be done with a salt (a random value added to the password) and a slow hash function (such as bcrypt or scrypt) to prevent brute-force or dictionary attacks.
- Digital signatures: Hashing a message before signing it with a private key. This way, the signature is smaller and faster to verify, and the message integrity is ensured. The hash algorithm used for digital signatures should be collision-resistant, such as SHA-2 or SHA-3.
- Message authentication codes (MACs): Hashing a message with a secret key to produce a tag that authenticates the message. The tag can be verified by anyone who knows the secret key, but cannot be forged by anyone who does not. The hash algorithm used for MACs should be secure and fast, such as HMAC or CMAC.