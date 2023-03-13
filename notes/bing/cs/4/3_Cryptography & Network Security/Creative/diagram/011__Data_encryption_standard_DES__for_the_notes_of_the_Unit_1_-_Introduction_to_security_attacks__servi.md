The following is a detailed ASCII diagram for Data Encryption Standard (DES) for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

```
+----------------+     +----------------+     +----------------+
| 64-bit plain   |     | 64-bit key     |     | 64-bit cipher  |
| text           |     |                |     | text           |
+----------------+     +----------------+     +----------------+
        |                      |                      ^
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      |
+----------------+     +----------------+     +----------------+
| Initial        |     | Key            |     | Inverse        |
| Permutation    |     | Generation     |     | Permutation    |
| (IP)           |     |                |     | (IP^-1)        |
+----------------+     +----------------+     +----------------+
        |                      |                      ^
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      |
+----------------+     +----------------+     +----------------+
| 16 rounds of   |     | 16 subkeys     |     | 16 rounds of   |
| encryption     |     | (48 bits each) |     | decryption     |
| using Feistel  |     |                |     | using Feistel  |
| structure      |     |                |     | structure      |
| and S-boxes    |     |                |     | and S-boxes    |
+----------------+     +----------------+     +----------------+
        |                      |                      ^
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      |
+----------------+     +----------------+     +----------------+
| Swap left and  |     |                |     | Swap left and  |
| right halves   |     |                |     | right halves   |
| (SW)           |     |                |     | (SW)           |
+----------------+     +----------------+     +----------------+
        |                      |                      ^
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      |
+----------------+     +----------------+     +----------------+
| 16 rounds of   |     | 16 subkeys     |     | 16 rounds of   |
| decryption     |     | (48 bits each) |     | encryption     |
| using Feistel  |     |                |     | using Feistel  |
| structure      |     |                |     | structure      |
| and S-boxes    |     |                |     | and S-boxes    |
+----------------+     +----------------+     +----------------+
        |                      |                      ^
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      |
+----------------+     +----------------+     +----------------+
| Inverse        |     | Key            |     | Initial        |
| Permutation    |     | Generation     |     | Permutation    |
| (IP^-1)        |     |                |     | (IP)           |
+----------------+     +----------------+     +----------------+
        |                      |                      ^