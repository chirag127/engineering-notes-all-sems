# Shannon’s theory of confusion and diffusion

- Confusion and diffusion are two properties of the operation of a secure cipher identified by Claude Shannon in his 1945 classified report A Mathematical Theory of Cryptography .
- These properties, when present, work to thwart the application of statistics and other methods of cryptanalysis .
- Confusion refers to making the relationship between the ciphertext and the symmetric key as complex and involved as possible .
- Diffusion refers to dissipating the statistical structure of plaintext over the bulk of ciphertext.
- Confusion can be achieved by using substitution ciphers, which replace each plaintext symbol with a different ciphertext symbol according to a key-dependent mapping.
- Diffusion can be achieved by using transposition ciphers, which permute the positions of the plaintext symbols according to a key-dependent pattern.
- Confusion and diffusion can be combined by using a fiestal structure, which alternates substitution and transposition operations in multiple rounds.
- A well-known example of a fiestal cipher is the Data Encryption Standard (DES), which uses 16 rounds of substitution and transposition, and a 56-bit key.
- The strength of DES depends on the confusion and diffusion properties of its components, such as the S-boxes, the P-box, and the key schedule.
- Differential cryptanalysis is a technique that exploits the lack of confusion and diffusion in some ciphers by analyzing the differences between pairs of plaintexts and ciphertexts.
- Block cipher modes of operation are methods of applying a block cipher to a message of arbitrary length, by dividing it into blocks and using different techniques to ensure confusion and diffusion across the blocks.
- Triple DES is a variant of DES that applies the DES cipher three times with different keys, to increase the security and resist differential cryptanalysis.