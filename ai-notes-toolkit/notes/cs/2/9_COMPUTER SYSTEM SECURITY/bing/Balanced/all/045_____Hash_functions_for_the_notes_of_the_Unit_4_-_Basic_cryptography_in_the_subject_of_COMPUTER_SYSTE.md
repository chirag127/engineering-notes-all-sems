# Hash functions

- A hash function is a mathematical function that maps an arbitrary binary string (called the message) to a binary string of fixed size (called the hash value or the digest).
- A hash function is said to be cryptographic if it has some special properties that make it suitable for security applications, such as authentication, integrity, and digital signatures.
- Some of the desirable properties of a cryptographic hash function are:
  - Pre-image resistance: Given a hash value, it should be computationally hard to find a message that produces that hash value. This means that a hash function should not be reversible or invertible.
  - Second pre-image resistance: Given a message, it should be computationally hard to find another message that produces the same hash value. This means that a hash function should not have collisions or duplicate outputs for different inputs.
  - Collision resistance: It should be computationally hard to find any two messages that produce the same hash value. This means that a hash function should have a large output space and a uniform distribution of outputs.
- Some examples of cryptographic hash functions are:
  - SHA-1: A hash function that produces a 160-bit output. It was widely used in many security protocols, but it is now considered insecure due to the discovery of collisions in 2017.
  - SHA-2: A family of hash functions that produce outputs of 224, 256, 384, or 512 bits. They are based on the same design as SHA-1, but with some modifications to improve security. They are currently the standard hash functions recommended by NIST.
  - SHA-3: A family of hash functions that produce outputs of 224, 256, 384, or 512 bits. They are based on a different design than SHA-1 and SHA-2, using a sponge construction that allows variable input and output lengths. They are the winners of the NIST hash function competition in 2012.
  - MD5: A hash function that produces a 128-bit output. It was widely used in many security applications, but it is now considered insecure due to the discovery of collisions in 2004.
  - RIPEMD-160: A hash function that produces a 160-bit output. It is based on the MD4 design, but with some modifications to improve security. It is used in some cryptographic protocols, such as Bitcoin.