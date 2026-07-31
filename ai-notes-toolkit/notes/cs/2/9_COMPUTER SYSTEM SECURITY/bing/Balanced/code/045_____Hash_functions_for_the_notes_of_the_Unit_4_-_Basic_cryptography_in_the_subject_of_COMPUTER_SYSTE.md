### Hash functions

A hash function is a mathematical function that maps an arbitrary input (also called a message) to a fixed-length output (also called a hash or a digest). A hash function has the following properties:

- It is easy to compute the hash value for any given input, but hard to find an input that produces a given hash value (pre-image resistance).
- It is hard to find two different inputs that produce the same hash value (collision resistance).
- Small changes in the input produce large changes in the hash value (avalanche effect).

A cryptographic hash function is a hash function that has additional security properties that make it suitable for cryptographic applications, such as:

- Authentication: A hash function can be used to verify the integrity and authenticity of a message or a file, by comparing the hash value computed by the sender and the receiver. For example, a digital signature is a hash value that is encrypted with the sender's private key, and can be verified by anyone with the sender's public key.
- Encryption: A hash function can be used to derive a secret key from a password or a passphrase, by applying the hash function multiple times (key stretching). For example, a password-based encryption scheme uses a hash function to generate a key that is used to encrypt and decrypt the data.
- Proof of work: A hash function can be used to create a computational challenge that requires a certain amount of time and resources to solve, by requiring the hash value to satisfy some criteria (such as having a certain number of leading zeros). For example, a proof-of-work system is used by some cryptocurrencies to secure the network and prevent spam transactions.

Some examples of cryptographic hash functions are:

- SHA-1: A 160-bit hash function that was widely used until it was broken in 2017, when researchers found a collision (two different inputs that produce the same hash value).
- SHA-2: A family of hash functions that include SHA-224, SHA-256, SHA-384, and SHA-512, with different output lengths. They are more secure than SHA-1, but still vulnerable to some attacks.
- SHA-3: A family of hash functions that include SHA3-224, SHA3-256, SHA3-384, and SHA3-512, with different output lengths. They are based on a different design than SHA-1 and SHA-2, and are considered more resistant to attacks.
- MD5: A 128-bit hash function that was widely used until it was broken in 2004, when researchers found a collision. It is still used for some non-critical applications, such as file verification.