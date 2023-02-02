### security of hash functions for the notes of the Unit 3 - Message Authentication Codes in the subject of Cryptography & Network Security
Hash functions are widely used for message authentication in cryptography. They take an input message and produce a fixed-length output called a hash value. Security of hash functions is important because it ensures the integrity of the message and protects against tampering.

1. Collision Resistance: It means that it is computationally infeasible to find two distinct messages with the same hash value.

2. Pre-Image Resistance: It means that it is computationally infeasible to find an input message that corresponds to a given hash value.

3. Second Pre-Image Resistance: It means that it is computationally infeasible to find a second input message that corresponds to a given hash value.

4. Avalanche Effect: A small change in the input message should result in a significant change in the hash value.

5. Resistance to Length Extension Attack: A hash function should not allow an attacker to extend the length of the original message without changing the hash value.

Hash functions like SHA-256, SHA-3, and BLAKE2 are widely used and considered secure. However, it is important to keep in mind that the security of a hash function depends on the size of its output and the computational power available to attackers.
