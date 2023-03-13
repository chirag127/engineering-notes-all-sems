The following is a detailed ASCII diagram for the strength of DES for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

```
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  Plaintext      |   |  Ciphertext     |   |  Plaintext      |
|  (64 bits)      |   |  (64 bits)      |   |  (64 bits)      |
|                 |   |                 |   |                 |
+--------+--------+   +--------+--------+   +--------+--------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  Initial        |   |  Final          |   |  Initial        |
|  Permutation    |   |  Permutation    |   |  Permutation    |
|  (IP)           |   |  (FP)           |   |  (IP)           |
|                 |   |                 |   |                 |
+--------+--------+   +--------+--------+   +--------+--------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  16 rounds of   |   |  16 rounds of   |   |  16 rounds of   |
|  encryption     |   |  decryption     |   |  encryption     |
|  using 56-bit   |   |  using 56-bit   |   |  using 56-bit   |
|  key            |   |  key            |   |  key            |
|                 |   |                 |   |                 |
+--------+--------+   +--------+--------+   +--------+--------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  Final          |   |  Initial        |   |  Final          |
|  Permutation    |   |  Permutation    |   |  Permutation    |
|  (FP)           |   |  (IP)           |   |  (FP)           |
|                 |   |                 |   |                 |
+--------+--------+   +--------+--------+   +--------+--------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  Ciphertext     |   |  Plaintext      |   |  Ciphertext     |
|  (64 bits)      |   |  (64 bits)      |   |  (64 bits)      |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +