Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of hashes for the unit 2 - cryptographic fundamentals for IoT in the subject of privacy and security in IoT.

# Hashes

- A hash is a function that maps an arbitrary input to a fixed-length output, usually a string or a number.
- A hash function has the following properties:
  - It is deterministic, meaning that the same input always produces the same output.
  - It is one-way, meaning that it is easy to compute the output from the input, but hard to find the input from the output.
  - It is collision-resistant, meaning that it is hard to find two different inputs that produce the same output.
- Hash functions are used for various purposes in cryptography, such as:
  - Integrity verification, to check if a message or a file has been tampered with or corrupted.
  - Authentication, to prove the identity or the origin of a message or a file.
  - Digital signatures, to sign a message or a file with a private key and verify it with a public key.
  - Key derivation, to generate a secret key from a password or a passphrase.
  - Proof of work, to prevent spam or denial-of-service attacks by requiring a certain amount of computational effort to generate or verify a hash.
- Some examples of hash functions are:
  - MD5, which produces a 128-bit output. It is no longer considered secure due to its vulnerability to collision attacks.
  - SHA-1, which produces a 160-bit output. It is also no longer considered secure due to its vulnerability to collision attacks.
  - SHA-2, which is a family of hash functions that produce outputs of 224, 256, 384, or 512 bits. It is widely used and considered secure.
  - SHA-3, which is a family of hash functions that produce outputs of 224, 256, 384, or 512 bits. It is based on a different design than SHA-2 and is considered secure.
  - BLAKE2, which is a family of hash functions that produce outputs of 160, 256, or 512 bits. It is based on the design of SHA-3 and is considered secure and fast.