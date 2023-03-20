 Here are the notes on Hash functions for the Unit 4 - Basic cryptography in COMPUTER SYSTEM SECURITY:

### Hash functions

1. A hash function is a mathematical algorithm that maps data of any size to a fixed-size value.
2. The input to a hash function is called the pre-image and the output is called the digest or hash value.
3. A good hash function should have the following properties:
- Determinism: Same input always produces the same output.
- Efficiency: Produces the hash value quickly.
- Avalanche effect: Small change in input should cause significant change in the hash value.
4. Use cases of hash functions:
- Data integrity: Compare hash of original data with hash of received data to check if data has been modified.
- Digital signatures: Creating a digital signature using hash and private key. The signature can be verified using the corresponding public key and hash of the message.
- Password security: Passwords are hashed using a salt to secure storage. Salt is a random string added to the password before hashing to make dictionary attacks harder.
- Commitments: Hiding information while committing to it by sending hash of information. The information can be later revealed and verified using the hash.
5. Popular hash functions: MD5, SHA-1, SHA-256, SHA-512, etc. MD5 and SHA-1 are vulnerable to collisions and hence not recommended. SHA-256 and SHA-512 are currently secure and recommended.

The content is written in markdown format without any emojis or external links as formal study material for exams. Please let me know if you would like me to modify or add anything.