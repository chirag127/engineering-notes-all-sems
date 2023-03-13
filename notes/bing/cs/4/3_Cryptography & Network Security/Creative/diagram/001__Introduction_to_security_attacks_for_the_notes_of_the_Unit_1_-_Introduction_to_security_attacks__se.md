The following is an attempt to draw a detailed ascii diagram for Introduction to security attacks for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

```
+---------------------+   +---------------------+   +---------------------+
|                     |   |                     |   |                     |
|  Security Attacks   |   | Security Services   |   | Security Mechanisms |
|                     |   |                     |   |                     |
+---------------------+   +---------------------+   +---------------------+
|                     |   |                     |   |                     |
| - Passive attacks   |   | - Confidentiality   |   | - Encryption        |
|   - Eavesdropping   |   | - Integrity         |   | - Authentication    |
|   - Traffic analysis|   | - Availability      |   | - Digital signature |
| - Active attacks    |   | - Non-repudiation   |   | - Hash function     |
|   - Masquerade      |   | - Authentication    |   | - Key management    |
|   - Modification    |   | - Access control    |   | - Firewall          |
|   - Repudiation     |   |                     |   |                     |
|   - Replay          |   |                     |   |                     |
|   - Denial of service|   |                     |   |                     |
|                     |   |                     |   |                     |
+---------------------+   +---------------------+   +---------------------+

+---------------------+   +---------------------+   +---------------------+
|                     |   |                     |   |                     |
| Classical Encryption|   | Stream Ciphers      |   | Block Ciphers       |
| Techniques          |   |                     |   |                     |
+---------------------+   +---------------------+   +---------------------+
|                     |   |                     |   |                     |
| - Substitution      |   | - Generate a stream |   | - Divide plaintext  |
|   - Caesar cipher   |   |   of bits (keystream)|   |   into blocks       |
|   - Monoalphabetic  |   | - XOR with plaintext|   | - Apply a key and   |
|   - Vigenere cipher |   | - Examples: RC4,    |   |   a function to each|
|   - Hill cipher     |   |   A5/1, A5/2        |   |   block             |
| - Transposition     |   |                     |   | - Examples: DES,    |
|   - Rail fence cipher|   |                     |   |   AES, IDEA         |
|   - Columnar cipher |   |                     |   |                     |
| - Cryptanalysis     |   |                     |   |                     |
|   - Frequency analysis|   |                     |   |                     |
|   - Brute force     |   |                     |   |                     |
| - Steganography     |   |                     |   |                     |
|   - Hiding data in  |   |                     |   |                     |
|     images, sounds, |   |                     |   |                     |
|     etc.            |   |                     |   |                     |
|                     |   |                     |   |                     |
+---------------------+   +---------------------+   +---------------------+

+---------------------+   +---------------------+   +---------------------+
|                     |   |                     |   |                     |
| Modern Block Ciphers|   | Data Encryption     |   | Triple DES          |
| Principles          |   | Standard (DES)      |   |                     |
+---------------------+   +---------------------+   +---------------------+
|                     |   |                     |   |                     |
| - Confusion         |   | - 64-bit block size |   | - Apply DES three   |
|   - Make the relation|   | - 56-bit key size   |   |   times with three  |
|     between key and |   | - Fiestel structure |   |   different keys    |
|     ciphertext      |   | - 16 rounds         |   | - Effective key size