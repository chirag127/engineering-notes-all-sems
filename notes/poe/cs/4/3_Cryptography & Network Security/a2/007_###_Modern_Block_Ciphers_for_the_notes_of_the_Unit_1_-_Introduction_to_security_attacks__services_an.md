 Here is the content in markdown format for the topic ### Modern Block Ciphers for the notes of the Unit 1 - Introduction to security attacks, services and mechanism, Classical encryption techniquessubstitution ciphers and transposition ciphers, cryptanalysis, steganography, Stream and block ciphers. Modern Block Ciphers:

### Modern Block Ciphers

- Block ciphers operate on fixed-length groups of bits called blocks. The most common block sizes are 64 and 128 bits.
- According to Claude Shannon's theory of cryptography, an ideal cipher has two properties - confusion and diffusion. Confusion disguises the relationship between the plaintext and ciphertext while diffusion spreads the influence of one plaintext symbol over many ciphertext symbols.
- The Feistel structure is a design strategy for block ciphers. It uses a function (F-function) that operates on half of the block in each round. The structure has high diffusion as the half block interacts with the other half in subsequent rounds. Popular Feistel ciphers are DES and Triple-DES.
- The Data Encryption Standard (DES) is a symmetric-key algorithm that uses a 56-bit key to encrypt 64-bit blocks of data. Though once a popular standard, it is now considered insecure due to its small key size. It has a Feistel structure with 16 rounds.
- The idea behind differential cryptanalysis is to analyze how differences in plaintexts propagate to differences in ciphertexts and use it to deduce key bits. DES has a weakness to this type of attack.
- Block ciphers can be operated in various modes like ECB, CBC, CFB, OFB, and CTR mode to use the cipher for various purposes and to mitigate some issues. For eg, CBC mode adds diffusion and prevents chosen-plaintext attacks.
- Triple DES (3DES) applies DES three times with two/three different keys to strengthen the algorithm against attacks. Though more secure than DES, it is slower and the effective key length is still small. Hence, it is being phased out in favor of AES.