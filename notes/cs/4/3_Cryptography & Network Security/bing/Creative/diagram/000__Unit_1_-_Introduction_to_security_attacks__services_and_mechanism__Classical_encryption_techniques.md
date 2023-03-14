The following is an attempt to draw a detailed ascii diagram for Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES.

Please note that this is not a complete or accurate representation of the topics, but only a rough sketch based on some web sources. You should consult more reliable and authoritative sources for a better understanding of the concepts.

```
+-----------------------------------------------------------------------------------------------------------------+
| Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniques              |
+-----------------------------------------------------------------------------------------------------------------+
|                                                                                                                 |
| +---------------------+ +---------------------+ +---------------------+ +---------------------+ +--------------+ |
| | Security Attacks    | | Security Services   | | Security Mechanisms | | Classical Encryption| | Steganography| |
| +---------------------+ +---------------------+ +---------------------+ +---------------------+ +--------------+ |
| |                     | |                     | |                     | |                     | |              | |
| | - Passive           | | - Confidentiality   | | - Encryption        | | - Substitution      | | - Hiding     | |
| | - Active            | | - Authentication    | | - Decryption        | | - Transposition     | |   information| |
| | - Interruption      | | - Integrity         | | - Hashing           | | - Cryptanalysis     | |   in other   | |
| | - Interception      | | - Non-repudiation   | | - Digital signature | |                     | |   media      | |
| | - Modification      | | - Access control    | | - Access control    | |                     | |              | |
| | - Fabrication       | | - Availability      | | - Audit trail       | |                     | |              | |
| |                     | |                     | |                     | |                     | |              | |
| +---------------------+ +---------------------+ +---------------------+ +---------------------+ +--------------+ |
|                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------+
|                                                                                                                 |
| +---------------------+ +---------------------+ +---------------------+ +---------------------+ +--------------+ |
| | Stream Ciphers      | | Block Ciphers       | | Shannon's Theory    | | Fiestal Structure   | | DES          | |
| +---------------------+ +---------------------+ +---------------------+ +---------------------+ +--------------+ |
| |                     | |                     | |                     | |                     | |              | |
| | - Encrypt one bit   | | - Encrypt a block   | | - Confusion         | | - Divide the block  | | - 64-bit     | |
| |   at a time         | |   at a time         | | - Diffusion         | |   into two halves   | |   block      | |
| | - Use a keystream   | | - Use a key         | | - Redundancy        | | - Apply a round     | | - 56-bit     | |
| |   generator         | |   schedule          | | - Unicity distance  | |   function to one   | |   key        | |
| | - XOR the plaintext | | - Use a mode of     | |                     | |   half using the    | | - 16 rounds  | |
| |   with the keystream| |   operation         | |                     | |   subkey            | | - S-boxes    | |
| | - Examples: RC4,    | | - Examples: AES,    | |                     | | - Swap the halves   | | - Weak keys  | |
| |   A5/1, E0          | |   Blowfish, IDEA    | |                     | | - Repeat for        | | - Differential| |
| |                     | |                     | |                     | |   several rounds    | |   cryptanalysis| |
| +---------------------+ +---------------------+ +---------------------+ +---------------------+ +--------------+ |
|                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------+
|                                                                                                                 |
| +---------------------+ +---------------------+ +---------------------+ +---------------------+ +--------------+ |
| | Triple DES          | |                     | |                     | |                     | |              | |
| +---------------------+ +----------------