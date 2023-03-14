The following is a possible ascii diagram for Introduction to security attacks for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

```
+-----------------------------+     +-----------------------------+
| Introduction to security    |     | Classical encryption       |
| attacks, services and       |     | techniques                 |
| mechanisms                  |     |                            |
+-----------------------------+     +-----------------------------+
|                             |     |                            |
| - Security attacks:         |     | - Substitution ciphers:    |
|   - Passive attacks         |     |   - Caesar cipher          |
|   - Active attacks          |     |   - Monoalphabetic cipher  |
|                             |     |   - Polyalphabetic cipher  |
| - Security services:        |     |   - One-time pad           |
|   - Authentication          |     | - Transposition ciphers:   |
|   - Confidentiality         |     |   - Rail fence cipher      |
|   - Integrity               |     |   - Columnar transposition |
|   - Non-repudiation         |     |   - Route cipher           |
|   - Availability            |     |                            |
|                             |     | - Cryptanalysis:           |
| - Security mechanisms:      |     |   - Frequency analysis     |
|   - Encryption              |     |   - Brute force            |
|   - Digital signature       |     |   - Known plaintext        |
|   - Hash function           |     |   - Chosen plaintext       |
|   - Firewall                |     |   - Chosen ciphertext      |
|   - Intrusion detection     |     |                            |
|                             |     | - Steganography:           |
|                             |     |   - Hiding data in images  |
|                             |     |   - Hiding data in audio   |
|                             |     |   - Hiding data in text    |
+-----------------------------+     +-----------------------------+
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          |                                       |
          V                                       V
+-----------------------------+     +-----------------------------+
| Stream and block ciphers    |     | Modern block ciphers       |
|                             |     |                            |
+-----------------------------+     +-----------------------------+
|                             |     |                            |
| - Stream ciphers:           |     | - Block ciphers principles:|
|   - Vernam cipher           |     |   - Block size             |
|   - RC4 cipher              |     |   - Key size               |
|   - Synchronous and         |     |   - Number of rounds       |
|     asynchronous modes      |     |   - Substitution boxes     |
|                             |     |   - Permutation boxes      |
| - Block ciphers:            |     |                            |
|   - Feistel cipher          |     | - Shannon’s theory of      |
|   - DES cipher              |     |   confusion and diffusion: |
|   - AES cipher              |     |   - Confusion:             |
|                             |     |     - Making the relation  |
| - Block cipher modes of     |     |       between plaintext    |
|   operation:                |     |       and ciphertext       |
|   - Electronic codebook     |     |       complex              |
|   - Cipher block chaining   |     |   - Diffusion:             |
|   - Cipher feedback         |     |     - Spreading the        |
|   - Output feedback         |     |       influence of a       |
|   - Counter mode            |     |       single plaintext     |
|                             |     |       bit over many        |
| - Triple DES:               |     |       ciphertext bits      |
|   - Using three DES keys    |     |                            |
|     to encrypt, decrypt and |     | - Fiestal structure:       |
|     encrypt a block         |     |   - A type of block cipher |
|                             |     |     that uses multiple     |
|                             |     |     rounds of encryption   |
|                             |     |     with different subkeys |
|                             |     |