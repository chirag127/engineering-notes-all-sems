### Hash functions for the notes of the Unit 4 - Basic cryptography in the subject of COMPUTER SYSTEM SECURITY

- A hash function is a mathematical function that converts an input value into a compressed numerical value, known as a hash value or digest.
- Hash functions are commonly used in cryptography to ensure the integrity of data.
- The input to a hash function can be of any length, but the output is always of a fixed length.
- A good hash function should have the following properties:
  - It should be deterministic, meaning that the same input will always produce the same output.
  - It should be fast to compute the hash value for any given input.
  - It should be infeasible to generate the same hash output from two different input values (collision resistance).
  - It should be infeasible to regenerate the original input value from the hash value (pre-image resistance).
  - A small change to the input should produce such a drastic change in the output that the new hash value appears uncorrelated with the old hash value (avalanche effect).
- Commonly used hash functions in cryptography include SHA-256, SHA-3, and BLAKE2.
- Hash functions are used in many applications, including digital signatures, message authentication codes (MACs), and password verification.