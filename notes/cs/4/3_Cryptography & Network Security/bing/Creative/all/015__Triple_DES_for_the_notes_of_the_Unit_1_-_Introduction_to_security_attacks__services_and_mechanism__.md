### Triple DES for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers: Block ciphers principles, Shannon’s theory of confusion and diffusion, fiestal structure, Data encryption standard(DES), Strength of DES, Idea of differential cryptanalysis, block cipher modes of operations, Triple DES in the subject of Cryptography & Network Security

- Triple DES (3DES or TDES) is a symmetric-key block cipher, which applies the DES cipher algorithm three times to each data block.
- It was proposed to increase the key size of DES, which was vulnerable to brute-force attacks with increasing computational power.
- It has two variants: 3-key Triple DES (3TDES) and 2-key Triple DES (2TDES).
- 3-key Triple DES uses three different 56-bit keys (K1, K2, K3) for encryption and decryption, resulting in a total key size of 168 bits.
- 2-key Triple DES uses two different 56-bit keys (K1, K2) for encryption and decryption, where K1 = K3, resulting in a total key size of 112 bits.
- The encryption and decryption process of Triple DES is as follows:

  - Encryption: C = E(K3, D(K2, E(K1, P)))
  - Decryption: P = D(K1, E(K2, D(K3, C)))

  where P is the plaintext, C is the ciphertext, E is the encryption function, and D is the decryption function of DES.

- Triple DES has a block size of 64 bits and uses a Feistel network structure with 48 DES-equivalent rounds.
- Triple DES is more secure than DES, but it is also slower and requires more memory.
- Triple DES has been deprecated by NIST in 2017 for new applications and will be disallowed for all applications by the end of 2023 .
- Triple DES has been replaced by the more secure and efficient Advanced Encryption Standard (AES).
- A mnemonic to remember the encryption and decryption process of Triple DES is: EDE for encryption andDED for decryption, where E stands for encryption and D stands for decryption.