### Block ciphers principles for the notes of the Unit 1 - Introduction of security attacks, services and mechanism in the subject of Cryptography & Network Security
Block ciphers are symmetric encryption algorithms that operate on fixed-size blocks of plaintext, typically 64 or 128 bits, to produce ciphertext of the same size. They use a shared secret key for encryption and decryption. 

Principles:
1. Confidentiality: Block ciphers ensure that the original plaintext cannot be easily derived from the ciphertext without the key.
2. Key management: The key must be securely shared between the sender and receiver to ensure confidentiality.
3. Pseudo-randomness: The ciphertext should appear random for the same plaintext and key.
4. Feistel structure: Many block ciphers use a Feistel structure, which divides the plaintext into two halves and applies a series of operations to each half.
5. Substitution-permutation network (SPN): Another common structure used in block ciphers is the SPN, which uses substitution and permutation operations to scramble the plaintext.
6. Modes of operation: Block ciphers can be used in different modes of operation, such as ECB, CBC, CFB, OFB, CTR, to provide different levels of security and functionality.
