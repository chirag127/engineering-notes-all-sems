### Hashes

- A hash function is a mathematical function that takes an arbitrary input and produces a fixed-length output, called a hash or a digest.
- A hash function has the following properties:
  - It is deterministic, meaning that the same input always produces the same output.
  - It is one-way, meaning that it is easy to compute the output from the input, but hard to find the input from the output.
  - It is collision-resistant, meaning that it is hard to find two different inputs that produce the same output.
- Hash functions are widely used in cryptography for various purposes, such as:
  - Data integrity, to verify that the data has not been tampered with or corrupted.
  - Authentication, to prove the identity or origin of the data or the sender.
  - Digital signatures, to sign the data with a private key and verify it with a public key.
  - Key derivation, to generate secret keys from passwords or other inputs.
  - Proof of work, to prevent spam or denial-of-service attacks by requiring a certain amount of computational effort to produce a valid output.
- Some examples of hash functions are:
  - SHA-1, SHA-2, and SHA-3, which are standardized by the National Institute of Standards and Technology (NIST) and widely used in various protocols and applications.
  - MD5, which is an older hash function that is no longer considered secure due to its vulnerability to collision attacks.
  - BLAKE2, which is a newer hash function that is faster and more secure than SHA-2 and SHA-3.
  - RIPEMD-160, which is a hash function designed for European applications and compatible with the Bitcoin protocol.