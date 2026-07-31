# Hash functions

A hash function is a mathematical function that maps an arbitrary input (also called a message) to a fixed-length output (also called a hash or a digest). A hash function can be seen as a way of compressing or summarizing the input data. Hash functions are widely used in cryptography and information security for various purposes, such as:

- Authenticating messages and transactions by generating and verifying digital signatures
- Detecting data corruption or tampering by comparing the hash of the original data with the hash of the modified data
- Deriving encryption keys from passwords or other secret inputs by applying a hash function iteratively or with a salt
- Indexing data structures such as hash tables or bloom filters by using the hash of the data as a key or a bit vector
- Proving the existence or non-existence of data by using hash-based data structures such as Merkle trees or hash chains

## Features of hash functions

Not all hash functions are suitable for cryptographic applications. A cryptographic hash function must satisfy some special properties that make it hard to invert, manipulate, or collide. These properties are:

- **Pre-image resistance**: Given a hash value, it should be computationally infeasible to find any input that hashes to that value. This property ensures that the hash function cannot be reversed or inverted, and that the input data cannot be recovered from the hash value.
- **Second pre-image resistance**: Given an input and its hash value, it should be computationally infeasible to find another input that hashes to the same value. This property ensures that the hash function is unique and that the input data cannot be substituted or forged by another data with the same hash value.
- **Collision resistance**: It should be computationally infeasible to find two different inputs that hash to the same value. This property ensures that the hash function is unpredictable and that the output space is large enough to avoid accidental or intentional collisions.

## Examples of hash functions

There are many hash functions that have been designed and standardized for cryptographic purposes. Some of the most common and widely used ones are:

- **MD5**: A 128-bit hash function that was designed in 1991 by Ronald Rivest. It was widely used for file integrity verification, password hashing, and digital signatures, but it is now considered insecure and obsolete due to its vulnerability to collision attacks and other weaknesses.
- **SHA-1**: A 160-bit hash function that was designed in 1995 by the National Security Agency (NSA) as a successor to MD5. It was widely used for the same purposes as MD5, but it is also now considered insecure and obsolete due to its vulnerability to collision attacks and other weaknesses.
- **SHA-2**: A family of hash functions that was designed in 2001 by the NSA as a successor to SHA-1. It consists of six variants with different output lengths: SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256. It is currently the most widely used and recommended hash function family for cryptographic applications, as it is considered secure and efficient.
- **SHA-3**: A family of hash functions that was designed in 2015 by the National Institute of Standards and Technology (NIST) as a successor to SHA-2. It consists of four variants with different output lengths: SHA3-224, SHA3-256, SHA3-384, and SHA3-512. It is based on a different design principle than SHA-2, called the sponge construction, which makes it more resistant to certain types of attacks. It is also considered secure and efficient, but it is not yet widely adopted or supported.