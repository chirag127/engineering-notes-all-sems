# Hash functions for the notes of the Unit 4 - Basic cryptography in the subject of COMPUTER SYSTEM SECURITY

- A hash function is a mathematical function that maps an arbitrary binary string (called the message) to a binary string of fixed size (called the hash value or the digest).
- A cryptographic hash function is a hash function that has special properties desirable for a cryptographic application, such as:
  - The probability of a particular hash value for a random message is very low (about 1/2^n, where n is the size of the hash value in bits).
  - It is computationally hard to find two different messages that have the same hash value (called collision resistance).
  - It is computationally hard to find a message that has a given hash value (called preimage resistance).
  - It is computationally hard to find a message that has a hash value that is similar to a given hash value (called second preimage resistance).
- Cryptographic hash functions are used in information security to authenticate transactions, messages, and digital signatures. They can also be used to generate random numbers, verify data integrity, and protect passwords.
- Some examples of cryptographic hash functions are:
  - MD5: Produces a 128-bit hash value. It is no longer considered secure due to collision attacks.
  - SHA-1: Produces a 160-bit hash value. It is also no longer considered secure due to collision attacks.
  - SHA-2: A family of hash functions that produce hash values of 224, 256, 384, or 512 bits. They are widely used and considered secure.
  - SHA-3: A family of hash functions that produce hash values of 224, 256, 384, or 512 bits. They are based on a different design than SHA-2 and offer more security and flexibility.