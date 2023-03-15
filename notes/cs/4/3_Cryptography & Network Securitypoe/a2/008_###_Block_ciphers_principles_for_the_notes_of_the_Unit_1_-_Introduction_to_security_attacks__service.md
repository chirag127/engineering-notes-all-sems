 Here are the notes for ### Block ciphers principles for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers:

Block ciphers principles:
- Block ciphers encrypt blocks of plaintext into blocks of ciphertext. The block size is usually 64 or 128 bits.
- To be secure, a block cipher must be resistant against all types of attacks like brute force attack, differential cryptanalysis, etc.
- This is achieved using Shannon's theory of confusion and diffusion which states that a secure block cipher must confuse the relationship between the plaintext and ciphertext and diffuse the statistical properties of the plaintext over the ciphertext.

Shannon's theory of confusion and diffusion:
- Confusion: The relationship between the plaintext and ciphertext should be made as complex as possible. This can be achieved using substitution-permutation networks.
- Diffusion: The statistical properties of the plaintext should be diffused over the entire ciphertext block. This can be achieved using permutations over bits or bytes of the block.

Feistel structure:
- A Feistel structure splits the block into two halves and performs multiple rounds of encryption. Each round involves applying a function to one half using the other half as input.
- The advantage is that decryption uses the same structure but with the order of operations reversed. This makes implementation easy.
- DES uses a Feistel structure with 16 rounds.

Data Encryption Standard(DES):
- DES is a symmetric-key algorithm for the encryption of electronic data.
- It uses a 56-bit key to encrypt 64-bit blocks of plaintext into ciphertext.
- Though once very popular, DES is now considered insecure due to its small key size.
- Triple DES (3DES) was devised to overcome this by applying DES encryption thrice with two or three different keys to increase the key size.

[Additional points on modes of operation, differential cryptanalysis, etc. can be included with examples and diagrams for better understanding.]