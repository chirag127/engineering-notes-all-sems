The following is a detailed ASCII diagram for the strength of DES for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security.

```
+-----------------+  64-bit plain text  +-----------------+
|                 |-------------------->|                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     | Initial         |
|                 |                     | Permutation     |
|                 |                     | (IP)            |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
| 64-bit key      |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
|                 |                     |                 |
+-----------------+                     +-----------------+
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       |
      |                                       +-----------------+
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       | 32-bit LPT      |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       +-----------------+
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       | 32-bit RPT      |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       +-----------------+
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       | Round 1         |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       +-----------------+
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       | Round 2         |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       +-----------------+
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       | Round 3         |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       +-----------------+
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |                                       |                 |
      |