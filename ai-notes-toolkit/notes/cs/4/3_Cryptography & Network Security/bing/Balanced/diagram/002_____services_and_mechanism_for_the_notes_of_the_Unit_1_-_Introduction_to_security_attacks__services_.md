Hello, I am Sydney, your AI assistant. I can help you with your study material on Cryptography & Network Security. Here is the content for the topic you requested:

# Services and Mechanism for the Notes of the Unit 1 - Introduction to Security Attacks, Services and Mechanism, Classical Encryption TechniquesSubstitution Ciphers and Transposition Ciphers, Cryptanalysis, Steganography, Stream and Block Ciphers. Modern Block Ciphers: Block Ciphers Principles, Shannon’s Theory of Confusion and Diffusion, Fiestal Structure, Data Encryption Standard(DES), Strength of DES, Idea of Differential Cryptanalysis, Block Cipher Modes of Operations, Triple DES

## Security Attacks, Services and Mechanism

- Security attacks are any actions that compromise the security goals of confidentiality, integrity, availability, authentication, and non-repudiation of information and systems.
- Security services are the countermeasures that provide protection against security attacks, such as encryption, digital signatures, access control, firewalls, etc.
- Security mechanisms are the specific methods or algorithms that implement security services, such as symmetric and asymmetric ciphers, hash functions, digital certificates, etc.

## Classical Encryption Techniques

- Classical encryption techniques are the methods of transforming plaintext into ciphertext using simple mathematical operations and secret keys.
- Substitution ciphers are the techniques that replace each letter or symbol of the plaintext with another letter or symbol, according to a fixed rule or key. Examples are Caesar cipher, monoalphabetic cipher, polyalphabetic cipher, etc.
- Transposition ciphers are the techniques that rearrange the order of the letters or symbols of the plaintext, according to a fixed rule or key. Examples are rail fence cipher, columnar cipher, permutation cipher, etc.
- Cryptanalysis is the art of breaking encryption techniques, by finding the secret key or the plaintext without the key, using various methods such as frequency analysis, brute force, known plaintext, chosen plaintext, etc.
- Steganography is the art of hiding information in other information, such as embedding a secret message in an image, audio, or video file, without altering the appearance or quality of the cover medium.

## Stream and Block Ciphers

- Stream ciphers are the techniques that encrypt each bit or byte of the plaintext individually, using a keystream that is generated from a secret key and an initialization vector. Examples are RC4, A5/1, A5/2, etc.
- Block ciphers are the techniques that encrypt each block of the plaintext, usually of fixed size, using a secret key and a mode of operation. Examples are DES, AES, IDEA, etc.

## Modern Block Ciphers

- Block ciphers principles are the basic concepts and properties that define how block ciphers work, such as block size, key size, number of rounds, round function, key schedule, etc.
- Shannon’s theory of confusion and diffusion are the two criteria that measure the strength of a block cipher, by making the relationship between the plaintext, ciphertext, and key as complex and random as possible.
- Confusion is the property that each bit of the ciphertext depends on several bits of the key, and changing one bit of the key changes many bits of the ciphertext. This can be achieved by using substitution operations, such as S-boxes, in the round function.
- Diffusion is the property that each bit of the ciphertext depends on several bits of the plaintext, and changing one bit of the plaintext changes many bits of the ciphertext. This can be achieved by using transposition operations, such as P-boxes, in the round function.
- Fiestal structure is a common design for block ciphers, where each round consists of four operations: subkey mixing, substitution, permutation, and swapping. The subkey mixing combines the round key with the input block using XOR. The substitution and permutation provide confusion and diffusion, respectively. The swapping exchanges the left and right halves of the block, except for the last round.
- Data Encryption Standard (DES) is a widely used block cipher that was standardized by NIST in 1977. It has a block size of 64 bits, a key size of 56 bits, and 16 rounds of fiestal structure. It is vulnerable to brute force attacks and differential cryptanalysis, and has been replaced by AES.
- Strength of DES depends on the key size, the number of rounds, and the resistance to cryptanalysis. The key size of 56 bits is too small for modern computing power, and can be broken by exhaustive search in a few hours. The number of rounds of 16 is considered adequate, but not optimal, for the block size of 64 bits. The resistance to differential cryptanalysis is moderate, but not high, as the probability of finding a differential characteristic is about 2^-47