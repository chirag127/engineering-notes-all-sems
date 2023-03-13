The following is an attempt to draw a detailed ascii diagram for Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES.

```
+-----------------------------------------------------------------------------------------------------------------+
| Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniques              |
+-----------------------------------------------------------------------------------------------------------------+
|                                                                                                                 |
| +-------------------+ +-------------------+ +-------------------+ +-------------------+ +-------------------+ |
| | Security attacks  | | Security services | | Security          | | Classical         | | Steganography     | |
| | - Active          | | - Confidentiality | | mechanisms        | | encryption        | | - Hiding          | |
| | - Passive         | | - Integrity       | | - Cryptographic   | | techniques        | |   information     | |
| | - Insider         | | - Availability    | | - Non-cryptographic| | - Substitution    | | - Types and       | |
| | - Outsider        | | - Authentication  | |                   | | - Transposition   | |   techniques      | |
| | - Replay          | | - Non-repudiation | |                   | | - Cryptanalysis   | | - Applications    | |
| | - Masquerade      | | - Access control  | |                   | |                   | |                   | |
| | - Modification    | |                   | |                   | |                   | |                   | |
| | - Denial of       | |                   | |                   | |                   | |                   | |
| |   service         | |                   | |                   | |                   | |                   | |
| +-------------------+ +-------------------+ +-------------------+ +-------------------+ +-------------------+ |
|                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------+
| Stream and block ciphers                                                                                        |
+-----------------------------------------------------------------------------------------------------------------+
|                                                                                                                 |
| +-------------------+ +-------------------+                                                                     |
| | Stream ciphers    | | Block ciphers     |                                                                     |
| | - Encrypt one bit | | - Encrypt a block |                                                                     |
| |   at a time       | |   of bits at a    |                                                                     |
| | - Use keystream   | |   time            |                                                                     |
| |   generator       | | - Use fixed       |                                                                     |
| | - Examples: RC4,  | |   transformation  |                                                                     |
| |   A5/1, A5/2      | | - Examples: DES,  |                                                                     |
| |                   | |   AES, IDEA       |                                                                     |
| +-------------------+ +-------------------+                                                                     |
|                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------+
| Modern Block Ciphers                                                                                            |
+-----------------------------------------------------------------------------------------------------------------+
|                                                                                                                 |
| +-------------------+ +-------------------+ +-------------------+ +-------------------+ +-------------------+ |
| | Block cipher      | | Shannon's theory  | | Fiestal structure | | Data encryption   | | Block cipher      | |
| | principles        | | of confusion and  | | - A way of        | | standard (DES)    | | modes of          | |
| | - Substitution    | | diffusion         | |   designing       | | - A 64-bit block  | | operation         | |
| | - Permutation     | | - Confusion:      | |   block ciphers   | |   cipher with a   | | - Electronic code | |
| | - Key expansion   | |   complex         | | - Consists of     | |   56-bit key      | |   book (ECB)      | |
| | - Round function  | |   relationship    | |   rounds of       | | - Uses 16 rounds  | | - Cipher block    | |
| | - Iteration       | |   between key and | |   substitution    | |   of fiestal      | |   chaining (CBC)  | |
| | - Invertibility   | |   ciphertext      | |   and permutation | |   structure       | | - Cipher feedback | |
| |                   | | - Diffusion:      | | - Examples: DES,  | | - Vulnerable to   | |   (CFB)           | |
|